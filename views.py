# views.py
from flask import abort, jsonify, render_template, request, redirect, url_for, send_file, make_response

from app import app

import os
import sys
import csv
import json
import uuid
import requests


sys.path.insert(0, "./src")

import deepnovo_config
import deepnovo_model
import deepnovo_worker_db
import deepnovo_worker_denovo
import deepnovo_worker_io
import deepnovo_worker_test
import deepnovo_main_modules

def write_single_mgf(mz, peaks, charge, output_filename):
    with open(output_filename, "w") as output_mgf:
        output_mgf.write("BEGIN IONS\n")
        output_mgf.write("TITLE=TESTQUERY\n")
        output_mgf.write("PEPMASS=%f\n" % (mz))
        output_mgf.write("CHARGE=%d+\n" % (charge))
        output_mgf.write("SCANS=1\n")
        output_mgf.write("RTINSECONDS=471.167652\n")
        output_mgf.write("SEQ=UNKNOWN\n")

        for peak in peaks:
            output_mgf.write("%s %s\n" % (str(peak[0]), str(peak[1])))

        output_mgf.write("END IONS\n")


@app.route('/', methods=['GET'])
def default():
    peaks_list = json.loads(request.args['peaks'])
    precursor_mz = float(request.args['precursormz'])
    charge = int(request.args['charge'])

    #Creating processing folder
    processing_uuid = str(uuid.uuid4())
    processing_directory = os.path.join(app.config["UPLOAD_FOLDER"], processing_uuid)
    os.mkdir(processing_directory)

    #writing out spectrum
    temporary_mgf_filename = os.path.join(processing_directory, "query.mgf")
    write_single_mgf(precursor_mz, peaks_list, charge, temporary_mgf_filename)

    print(processing_directory, temporary_mgf_filename)

    #Changing parameters appropriately
    deepnovo_config.FLAGS.mgf_dir = processing_directory
    deepnovo_config.FLAGS.train_dir = "./model"
    deepnovo_config.FLAGS.beam_search = True
    deepnovo_config.FLAGS.beam_size = 5
    deepnovo_config.FLAGS.decode_dir = processing_directory
    deepnovo_config.FLAGS.topk = True

    output_file_pathname = os.path.join(processing_directory, "query_out.txt")

    deepnovo_main_modules.multi_decode(input_dir=processing_directory)

    return_list = []

    with open(output_file_pathname) as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")

        for row in reader:
            output_dict = {}
            output_dict["output_score"] = row["output_score"]
            output_dict["output_seq"] = row["output_seq"].replace(",", "")
            output_dict["scan"] = row["scan"]

            return_list.append(output_dict)

    return json.dumps(return_list)

import os
import sys

input_mgf_filename = sys.argv[1]
output_mgf_filename = sys.argv[2]


spectrum_lines = []
keep_spectrum = True

blacklist = ["PROTEIN=", "SCANS=", "SCAN=", "SCORE=", "FDR=", "COLLISION_ENERGY=", "FILENAME=", "MSLEVEL="]

with open(output_mgf_filename, "w") as output_file:
    for line in open(input_mgf_filename):
        if any(s in line for s in blacklist):
            continue

        if "BEGIN IONS" in line:
            spectrum_lines = []
            keep_spectrum = True

        if "PEPMASS=" in line:
            spectrum_lines.append("TITLE=XXX")

        spectrum_lines.append(line.rstrip().replace("\t", " "))

        if "CHARGE=" in line:
            spectrum_lines.append("SCANS=XXX")
            spectrum_lines.append("RTINSECONDS=100")

        if "END IONS" in line:
            if keep_spectrum:
                output_file.write("\n".join(spectrum_lines))

        if "SEQ=" in line:
            peptide_sequence = line.split("=")[1].rstrip()
            if "+" in peptide_sequence:
                keep_spectrum = False
                continue
            if "-" in peptide_sequence:
                keep_spectrum = False
                continue
            print(peptide_sequence)

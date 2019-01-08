FROM tensorflow/tensorflow:1.2.0

RUN pip install biopython
RUN pip install pyteomics
RUN pip install numba
RUN pip install sigopt

# Web Server Dependencies
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install flask
RUN pip install requests
RUN pip install gunicorn
RUN pip install xmltodict

COPY ./*sh /app/
COPY ./*py /app/
COPY ./src /app/src
WORKDIR /app

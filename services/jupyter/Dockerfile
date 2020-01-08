FROM jupyter/scipy-notebook
USER root

VOLUME /home/jovyan/data
RUN chmod -R 777 /home/jovyan/data

RUN rm -rf /home/jovyan/work

RUN mkdir -m 777 -p /home/jovyan/conf
COPY . /home/jovyan/conf/
RUN chmod -R 777 /home/jovyan/conf

RUN pip install minio redis urllib3 PyMySql
RUN apt-get update \
    && apt-get install -y curl

EXPOSE 8888

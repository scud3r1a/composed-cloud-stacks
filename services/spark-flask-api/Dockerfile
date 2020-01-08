FROM gettyimages/spark:latest

# Renew env variables
ENV SPARK_VERSION 2.3.1
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
ENV PATH $PATH:${SPARK_HOME}/bin

# Set workdir and version header script
WORKDIR $SPARK_HOME
COPY ./version.py $SPARK_HOME/version.py

# Place container init bash script and no-info conf
# RUN mkdir $SPARK_HOME/handler
# COPY ./spark-noinfo.sh $SPARK_HOME/spark-noinfo.sh
# COPY ./flask-spark-noinfo.sh $SPARK_HOME/flask-spark-noinfo.sh
# RUN chmod +x $SPARK_HOME/spark-noinfo.sh
# RUN chmod +x $SPARK_HOME/flask-spark-noinfo.sh
# COPY ./log4j.properties.noinfo $SPARK_HOME/handler/log4j.properties

# Flask API
RUN pip install Flask jsonify requests pandas
RUN mkdir /api
COPY ./api/* /api/
COPY ./flask-spark-noinfo.sh $SPARK_HOME/flask-spark-noinfo.sh
RUN chmod +x $SPARK_HOME/flask-spark-noinfo.sh

# Create data sharing folder
VOLUME /data

# Web UI
EXPOSE 4040

# Flask API
EXPOSE 5000

# By default, print version (header)
# ENTRYPOINT ["bash", "spark-noinfo.sh"]
# CMD ["version.py"]

CMD ["bash", "flask-spark-noinfo.sh"]
# CMD ["version.py"]

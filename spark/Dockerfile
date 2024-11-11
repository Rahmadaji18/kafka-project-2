FROM bitnami/spark:latest

ENV SPARK_HOME=/opt/bitnami/spark
ENV PATH=$SPARK_HOME/bin:$PATH

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install pyspark

COPY spark_script.py /opt/spark_script.py

RUN mkdir /opt/models
VOLUME /opt/models

WORKDIR $SPARK_HOME

CMD ["spark-submit", "/opt/spark_script.py"]

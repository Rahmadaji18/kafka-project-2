FROM python:3.8-slim
RUN pip install kafka-python
COPY producer.py /kafka/producer.py
COPY consumer.py /kafka/consumer.py
WORKDIR /kafka

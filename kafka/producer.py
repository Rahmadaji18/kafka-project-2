from kafka import KafkaProducer
import time
import random

producer = KafkaProducer(bootstrap_servers='kafka:9092')
with open('dataset.txt') as f:
    for line in f:
        producer.send('test-topic', value=line.encode())
        time.sleep(random.uniform(0.5, 1.5))  # Random sleep for simulation

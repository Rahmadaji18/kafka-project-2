from kafka import KafkaConsumer
import time

consumer = KafkaConsumer('test-topic', bootstrap_servers='kafka:9092', auto_offset_reset='earliest')
batch_size = 100
batch = []
batch_id = 1

for message in consumer:
    batch.append(message.value.decode())
    if len(batch) >= batch_size:
        with open(f'batch_{batch_id}.txt', 'w') as f:
            f.write("\n".join(batch))
        batch_id += 1
        batch = []

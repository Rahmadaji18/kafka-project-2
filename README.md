# Kelompok 5

| Nrp | Anggota Kelompok |
| --- | --- |
| 5027221013 | Rizki Ramadhani |
| 5027221031 | Gavriel Pramuda Kurniaadi |
| 5027221034 | Rahmad Aji Wicaksono |


## Project Big Data and Lakehouse - Diabetes Prediction with Kafka & Spark ML
Project ini mensimulasikan pemrosesan data stream menggunakan Apache Kafka dan Apache Spark ML untuk membuat model prediksi diabetes. Data di-stream dari Kafka Producer ke Kafka Server dan diproses dalam batch oleh Kafka Consumer, kemudian digunakan oleh Spark untuk melatih beberapa model Machine Learning.

# 1. Persiapan

## 1.1 Setup
Gunakan docker-compose.yml berikut untuk menyiapkan Apache Kafka dan Zookeeper.

```yml
services:
  zookeeper:
    image: "bitnami/zookeeper:latest"
    container_name: zookeeper
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
    ports:
      - "2181:2181"

  kafka:
    image: "bitnami/kafka:latest"
    container_name: kafka
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
      - ALLOW_PLAINTEXT_LISTENER=yes
      - KAFKA_LISTENERS=PLAINTEXT://:9092
      - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
    ports:
      - "9092:9092"
    depends_on:
      - zookeeper
```

Jalankan container Docker dengan perintah berikut.
```
docker-compose up --build
```

## 1.2 Topik
Masuk ke container Kafka.
```
docker exec -it kafka bash
```
Buat topik bernama server-kafka
```
kafka-topics.sh --create --topic server-kafka --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 
```
Cek apakah topik sudah berhasil dibuat.
```
kafka-topics.sh --list --bootstrap-server localhost:9092
```

# 2. Streaming Data dengan Kafka
## 2.1 Menjalankan Kafka Procedur
kafka_producer.py akan membaca dataset dan mengirimkan data per baris ke Kafka dengan jeda acak.
```
python3 kafka/producer.py
```
## 2.2 Menjalankan Kafka Consumer
Buka terminal baru dan jalankan kafka_consumer.py untuk membaca data dari Kafka dan menyimpannya dalam batch.
```
python3 kafka/consumer.py
```
Output akan disimpan dalam folder batch/ sesuai dengan jumlah data yang diterima per batch.

# 3. Training Model dengan Spark ML
## 3.1 Spark
Aktifkan virtual environment.
```
python3 -m venv venv
source venv/bin/activate
```
## 3.2 Melatih Model
Script spark_script.py akan memproses setiap batch data dari folder batch/, melakukan preprocessing, melatih model, dan menyimpannya di folder models/.

Jalankan perintah berikut untuk melatih model.
```
python3 spark/spark_script.py
```
Model yang dilatih akan disimpan sebagai model_1, model_2, dan seterusnya, sesuai dengan batch yang diproses.

# 4. API dan Endpoint
## 4.1 Menjalankan API
Jalankan API yang meng-host model dan mengizinkan akses melalui endpoint.
```
python3 api/api.py
```
API akan berjalan pada localhost:5000. Setiap model dapat diakses melalui endpoint /prediction/<model_id> .
## 4.2 Request dan Response
Gunakan curl untuk mengirim data input ke model.

### Model 1
#### Request
```
curl -X POST http://localhost:5000/prediction/1  \
 -H "Content-Type: application/json"               \
 -d '{
        "age": 65,
        "hypertension": 1,
        "heart_disease": 1,
        "bmi": 30.5,
        "HbA1c_level": 8.0,
        "blood_glucose_level": 160,
        "gender_index": 1,
        "smoking_history_index": 2
    }'
```
#### Response
```
{
  "diabetes": 1,
  "model": 1
}
```
### Model 2
#### Request
```
curl -X POST http://localhost:5000/prediction/2  \
 -H "Content-Type: application/json"               \
 -d '{
        "age": 65,
        "hypertension": 1,
        "heart_disease": 1,
        "bmi": 30.5,
        "HbA1c_level": 8.0,
        "blood_glucose_level": 160,
        "gender_index": 1,
        "smoking_history_index": 2
    }'
```
#### Response
```
{
  "diabetes": 1,
  "model": 2
}
```
### Model 3
#### Request
```
curl -X POST http://localhost:5000/prediction/3  \
 -H "Content-Type: application/json"               \
 -d '{
        "age": 65,
        "hypertension": 1,
        "heart_disease": 1,
        "bmi": 30.5,
        "HbA1c_level": 8.0,
        "blood_glucose_level": 160,
        "gender_index": 1,
        "smoking_history_index": 2
    }'
```
#### Response
```
{
  "diabetes": 1,
  "model": 3
}
```
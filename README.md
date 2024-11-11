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

```
Code
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
Buat topik bernama kafka-server ? .
```
Code 
```
Cek apakah topik sudah berhasil dibuat.
```
kafka-topics.sh --list --bootstrap-server localhost:9092
```

# 2. Streaming Data dengan Kafka
## 2.1 Menjalankan Kafka Procedur
kafka_producer.py akan membaca dataset dan mengirimkan data per baris ke Kafka dengan jeda acak.
```
python3 kafka_producer.py
```
## 2.2 Menjalankan Kafka Consumer
Buka terminal baru dan jalankan kafka_consumer.py untuk membaca data dari Kafka dan menyimpannya dalam batch.
```
python3 kafka_consumer.py
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
Script train_model.py ? akan memproses setiap batch data dari folder batch/, melakukan preprocessing, melatih model, dan menyimpannya di folder models/.

Jalankan perintah berikut untuk melatih model.
```
Code python3 spark_ml/train_model.py
```
Model yang dilatih akan disimpan sebagai model_1, model_2, dan seterusnya, sesuai dengan batch yang diproses.

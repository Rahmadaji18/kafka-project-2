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
Gunakan docker-compose.yml berikut untuk menyiapkan Apache Kafka dan Zookeeper:

```
Code
```

Jalankan container Docker dengan perintah berikut:
```
docker-compose up --build
```

## 1.2 Kafka
Masuk ke container Kafka:
```
docker exec -it kafka bash
```
Buat topik bernama kafka-server ? :
```
Code 
```
Cek apakah topik sudah berhasil dibuat:
```
kafka-topics.sh --list --bootstrap-server localhost:9092
```

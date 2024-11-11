from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

spark = SparkSession.builder.appName("ModelTraining").getOrCreate()

for batch_id in range(1, 4):  # Adjust based on number of batches
    df = spark.read.csv(f'batch_{batch_id}.txt', inferSchema=True, header=False)
    assembler = VectorAssembler(inputCols=df.columns, outputCol="features")
    dataset = assembler.transform(df)
    kmeans = KMeans().setK(3).setSeed(1)
    model = kmeans.fit(dataset)
    model.save(f'model_{batch_id}')

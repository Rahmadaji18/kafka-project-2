from flask import Flask, request, jsonify
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.ml.linalg import Vectors
from pyspark.sql import SparkSession
import os

app = Flask(__name__)

# Initialize Spark session
spark = SparkSession.builder \
    .appName("FlaskSparkMLApp") \
    .master("local[*]") \
    .getOrCreate()

MODEL_PATH = "spark/models/"

def load_model(model_name):
    model_path = os.path.join(MODEL_PATH, model_name)
    if os.path.exists(model_path):
        return RandomForestClassificationModel.load(model_path)
    else:
        return None

# Prepare features for the model based on the new variables
def prepare_features(data):
    features = [
        data.get("age", 0),
        data.get("hypertension", 0),
        data.get("heart_disease", 0),
        data.get("bmi", 0),
        data.get("HbA1c_level", 0),
        data.get("blood_glucose_level", 0),
        data.get("gender_index", 0),
        data.get("smoking_history_index", 0)
    ]
    return Vectors.dense(features)

@app.route("/prediction/<model_id>", methods=["POST"])
def predict(model_id):
    data = request.json
    input_vector = prepare_features(data)

    model_name = 'model_' + model_id
    model = load_model(model_name)

    if not model:
        return jsonify({"error": f"Model {model_id} not found"}), 404

    # Perform prediction
    prediction = model.predict(input_vector)

    return jsonify({"model": int(model_id), "diabetes": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)

    spark.stop()

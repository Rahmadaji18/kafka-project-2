from flask import Flask, request, jsonify
import joblib  # Assuming models are saved as pickle files

app = Flask(__name__)
models = {
    1: joblib.load('model_1.pkl'),
    2: joblib.load('model_2.pkl'),
    3: joblib.load('model_3.pkl')
}

@app.route('/predict', methods=['POST'])
def predict():
    model_id = int(request.json.get('model_id'))
    data = request.json.get('data')
    prediction = models[model_id].predict([data])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

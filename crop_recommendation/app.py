from flask import Flask, request, render_template
import pickle
import pandas as pd




app = Flask(__name__)







# Load the trained model
with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_crop(input_data):
    # Ensure input_data is a DataFrame with the same structure as the training data
    input_df = pd.DataFrame([input_data], columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    prediction = model.predict(input_df)
    return prediction[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = {
            'N': float(request.form['N']),
            'P': float(request.form['P']),
            'K': float(request.form['K']),
            'temperature': float(request.form['temperature']),
            'humidity': float(request.form['humidity']),
            'ph': float(request.form['ph']),
            'rainfall': float(request.form['rainfall'])
        }
        predicted_crop = predict_crop(input_data)
        return render_template('result.html', prediction=predicted_crop)

if __name__ == '__main__':
    app.run(debug=True)










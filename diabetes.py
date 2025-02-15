import pickle
import numpy as np
from flask import Flask, request, render_template

# Load the trained model
with open('diabetes.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('diabetes.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        features = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]

        features = np.array(features).reshape(1, -1)  # Convert to NumPy array
        prediction = model.predict(features)  # Get prediction

        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

        return render_template('diabetes.html', prediction_text=f"Prediction: {result}")

    except:
        return render_template('diabetes.html', prediction_text="Error in input. Please enter valid values.")

if __name__ == '__main__':
    app.run(debug=True)

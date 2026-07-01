import pickle
import numpy as np
import pandas as pd
import os
from datetime import datetime

# Load model
model = pickle.load(open("heart_model.pkl", "rb"))

# Load scaler
scaler = pickle.load(open("scaler.pkl", "rb"))


def predict_patient(data):

    data = np.array(data).reshape(1, -1)

    data = scaler.transform(data)

    prediction = model.predict(data)[0]

    return prediction


def generate_report(patient, prediction):

    if prediction == 1:

        risk = "HIGH RISK"

        advice = """
• Consult a Cardiologist immediately.
• Reduce oily food.
• Exercise regularly.
• Monitor Blood Pressure.
• Monitor Cholesterol.
"""

    else:

        risk = "LOW RISK"

        advice = """
• Continue healthy lifestyle.
• Exercise regularly.
• Maintain balanced diet.
• Annual health check-up recommended.
"""

    report = f"""

============================

PATIENT HEALTH REPORT

============================

Patient Name : {patient['name']}

Age : {patient['age']}

Prediction : {risk}

Recommendations:

{advice}

Generated On :

{datetime.now()}

"""

    return report


def save_log(patient, prediction):

    patient["Prediction"] = prediction

    patient["Date"] = datetime.now()

    df = pd.DataFrame([patient])

    if os.path.exists("patient_logs.csv"):

        df.to_csv("patient_logs.csv", mode="a", header=False, index=False)

    else:

        df.to_csv("patient_logs.csv", index=False)
import streamlit as st
from agent import predict_patient, generate_report, save_log

st.title("❤️ Intelligent Heart Disease AI Agent")

st.write("Enter Patient Details")

name = st.text_input("Patient Name")

age = st.number_input("Age", 1, 120)

sex = st.selectbox("Sex", [0,1])

cp = st.number_input("Chest Pain Type")

trestbps = st.number_input("Resting Blood Pressure")

chol = st.number_input("Cholesterol")

fbs = st.selectbox("Fasting Blood Sugar", [0,1])

restecg = st.number_input("Rest ECG")

thalach = st.number_input("Maximum Heart Rate")

exang = st.selectbox("Exercise Induced Angina", [0,1])

oldpeak = st.number_input("Old Peak")

slope = st.number_input("Slope")

ca = st.number_input("Major Vessels")

thal = st.number_input("Thal")

if st.button("Analyze Patient"):

    features = [
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]

    prediction = predict_patient(features)

    patient = {
        "name": name,
        "age": age
    }

    save_log(patient, prediction)

    report = generate_report(patient, prediction)

    if prediction == 1:

        st.error("⚠ High Risk of Heart Disease")

    else:

        st.success("✅ Low Risk")

    st.text(report)
import streamlit as st
import pickle
import numpy as np

# Load model
with open('titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)

# --- UI ---
st.title("🚢 Titanic Survival Predictor")
st.write("Masukkan data penumpang untuk memprediksi peluang selamat.")

# Input form
pclass = st.selectbox("Kelas Tiket", [1, 2, 3], 
                       format_func=lambda x: f"Kelas {x}")

sex = st.radio("Jenis Kelamin", ["Male", "Female"])
sex_encoded = 0 if sex == "Male" else 1

age = st.slider("Usia", min_value=1, max_value=80, value=30)

sibsp = st.number_input("Jumlah Saudara/Pasangan di Kapal", 
                         min_value=0, max_value=8, value=0)

parch = st.number_input("Jumlah Orang Tua/Anak di Kapal", 
                         min_value=0, max_value=6, value=0)

fare = st.number_input("Harga Tiket (£)", 
                        min_value=0.0, max_value=600.0, value=32.0)

# Predict
if st.button("Prediksi"):
    input_data = np.array([[pclass, sex_encoded, age, sibsp, parch, fare]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.divider()

    if prediction == 1:
        st.success(f"✅ Prediksi: **SELAMAT**")
    else:
        st.error(f"❌ Prediksi: **TIDAK SELAMAT**")

    st.metric("Peluang Selamat", f"{probability[1]*100:.1f}%")
    st.metric("Peluang Tidak Selamat", f"{probability[0]*100:.1f}%")
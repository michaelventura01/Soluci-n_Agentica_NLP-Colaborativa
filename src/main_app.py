import streamlit as st
from src.data_loader import load_data, preprocess_data
from src.recommender import get_recommendations

st.title("Fitness & Nutrition Recommender")

df = preprocess_data(load_data("data/fitness_dataset.csv"))

age = st.slider("Edad", 18, 70, 30)
bmi = st.slider("BMI", 15.0, 35.0, 22.5)
fat = st.slider("% Grasa corporal", 5.0, 40.0, 20.0)
freq = st.slider("Días/semana de entrenamiento", 1, 7, 4)
exp = st.slider("Nivel de experiencia (1-5)", 1, 5, 2)

user_profile = {
    "age": age,
    "bmi": bmi,
    "fat_percentage": fat,
    "workout_frequency_(days/week)": freq,
    "experience_level": exp
}

if st.button("Obtener recomendaciones"):
    recs = get_recommendations(df, user_profile)
    st.dataframe(recs)
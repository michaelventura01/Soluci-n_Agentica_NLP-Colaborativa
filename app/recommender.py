# src/recommender.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

def get_recommendations(df: pd.DataFrame, user_profile: dict, n=5):
    features = ['Age', 'BMI', 'Fat_Percentage', 
                'Workout_Frequency (days/week)', 'Experience_Level']
    
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])

    user_df = pd.DataFrame([user_profile])
    user_scaled = scaler.transform(user_df[features])
    
    sim = cosine_similarity(user_scaled, X)[0]
    df['similarity'] = sim
    
    top = df.sort_values(by='similarity', ascending=False).head(n)
    return top[['Workout_Type', 'diet_type', 'Calories_Burned', 'similarity']]
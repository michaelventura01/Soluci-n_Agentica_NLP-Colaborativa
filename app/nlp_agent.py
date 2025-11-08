from get_recommendations import Recommender

def ask(user_profile: dict, n=5):
    recommendations = get_recommendations(df, user_profile, n=n)
    response = "Según tu perfil, te recomiendo las siguientes opciones:\n\n"
    for i, row in recommendations.iterrows():
        response += (f"- Ejercicio: {row['Workout_Type']}\n"
                      f"  Dieta: {row['diet_type']}\n"
                      f"  Calorías quemadas aproximadas: {row['Calories_Burned']:.1f}\n"
                      f"  Similitud con tu perfil: {row['similarity']:.2f}\n\n")
    return response
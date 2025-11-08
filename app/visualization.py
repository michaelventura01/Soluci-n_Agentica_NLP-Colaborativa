import seaborn as sns
import matplotlib.pyplot as plt

def plot_efficiency_by_experience(df):
    sns.boxplot(data=df, x='experience_level', y='efficiency')
    plt.title("Eficiencia calórica por nivel de experiencia")
    plt.show()

def plot_diet_vs_calories(df):
    sns.barplot(data=df, x='diet_type', y='calories', errorbar=None)
    plt.xticks(rotation=45)
    plt.title("Promedio de calorías por tipo de dieta")
    plt.show()
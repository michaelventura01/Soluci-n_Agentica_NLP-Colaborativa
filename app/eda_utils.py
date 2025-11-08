import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def describe_data(df: pd.DataFrame):
    print("Dimensiones:", df.shape)
    display(df.describe().T)
    display(df.head())

def plot_distributions(df: pd.DataFrame):
    fig, axs = plt.subplots(2, 2, figsize=(10,8))
    sns.histplot(df['BMI'], kde=True, ax=axs[0,0])
    sns.histplot(df['Fat_Percentage'], kde=True, ax=axs[0,1])
    sns.histplot(df['Calories_Burned'], kde=True, ax=axs[1,0])
    sns.histplot(df['efficiency'], kde=True, ax=axs[1,1])
    axs[0,0].set_title('BMI')
    axs[0,1].set_title('% Grasa corporal')
    axs[1,0].set_title('Calorías quemadas')
    axs[1,1].set_title('Eficiencia calórica')
    plt.tight_layout()
    plt.show()

def corr_heatmap(df: pd.DataFrame):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(12,8))
    sns.heatmap(corr, cmap='coolwarm')
    plt.title('Matriz de correlaciones')
    plt.show()
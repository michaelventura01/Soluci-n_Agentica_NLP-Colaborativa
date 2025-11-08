import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df['bmi_gap'] = df['BMI_calc'] - df['BMI']
    df['efficiency'] = df['Calories_Burned'] / df['Session_Duration (hours)']
    return df
import pandas as pd

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    # Perform any necessary preprocessing here
    return df

if __name__ == "__main__":
    df = preprocess_data('../data/ratings.csv')
    print(df.head())

import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('../data/ratings.csv')
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)

# Train-test split
trainset, testset = train_test_split(data, test_size=0.25)

# Build and train the model
algo = SVD()
algo.fit(trainset)

# Save the trained model
import pickle
with open('../models/svd_model.pkl', 'wb') as f:
    pickle.dump(algo, f)

from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open('../models/svd_model.pkl', 'rb') as f:
    algo = pickle.load(f)

# Load the dataset
df = pd.read_csv('../data/ratings.csv')

def get_recommendations(user_id, num_recommendations=5):
    movie_ids = df['movie_id'].unique()
    user_ratings = [(movie_id, algo.predict(user_id, movie_id).est) for movie_id in movie_ids]
    user_ratings.sort(key=lambda x: x[1], reverse=True)
    recommendations = [movie_id for movie_id, _ in user_ratings[:num_recommendations]]
    return recommendations

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id'))
    recommendations = get_recommendations(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

# congenial-train
## Movie Recommendation System

This repository contains a movie recommendation system using collaborative filtering.

## Structure
- `data/ratings.csv`: Dataset containing user ratings for movies.
- `models/recommendation_model.py`: Script for training and saving the recommendation model.
- `app/api.py`: Flask app to serve recommendations.
- `utils/data_preprocessing.py`: Script for data preprocessing (if needed).
- `requirements.txt`: List of dependencies.
- `.gitignore`: Files and directories to ignore in the repository.
- `config.py`: Configuration file for paths and settings.

## Setup Instructions
1. Clone the repository:
   
   ``` git clone https://github.com/yourusername/movie-recommendation-system.git‘``
change directory/
   cd movie-recommendation-system```

  3. train dependencies 

```pip install -r requirements.txt```




3. train the model 

```python models/recommendation_model.py```


Run the flask app 

```python app/api.py```

 
 Make a request to get recommendations:

```curl "http://127.0.0.1:5000/recommend?user_id=1"```

 
 ## config.py

  Configuration file for paths and settings.
	Example content:

```DATA_PATH = 'data/ratings.csv'```
```MODEL_PATH = 'models/svd_model.pkl```




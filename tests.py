import os
from model.utils import *

expected_genres = {
    'track_1.mp3': 'Hip-Hop',
    'track_2.mp3': 'Jazz',
    'track_4.mp3': 'Pop',
    'track_5.mp3': 'Rock',
    'track_7.mp3': 'Rock',
    'track_6.mp3': 'Soundtrack',
}

valid_files = [
    file
    for file in os.listdir('tests/')
    if file != 'track_8.mp3' and file != 'track_3.wav'
]

#Test --predict_genre
model = load_model()
for file in valid_files:
    predicted_genre, _ = predict_genre("tests/" + file, model)
    actual_genre = expected_genres[file]
    assert predicted_genre == expected_genres[file]

for file in ['track_8.mp3', 'track_3.mp3']:
    genre, probabilities = predict_genre("tests/track_8.mp3", model)
    assert ((genre is None) and (probabilities is None))

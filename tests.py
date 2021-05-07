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

#Test --check_mp3
assert check_valid_mp3('tests/track_3.wav') == False
assert check_valid_mp3('tests/track_8.mp3') == False
assert check_valid_mp3('tests/track_7.mp3') == True

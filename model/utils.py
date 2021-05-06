import numpy as np
import os
import tensorflow as tf

from librosa import load, power_to_db, zero_crossings
from librosa.beat import tempo
from librosa.feature import melspectrogram, spectral_flatness
from librosa.onset import onset_strength
from pydub import AudioSegment
from random import randrange

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Added for reference...
# ----------------------------------------------------
# file_location = input("Enter File Model Location: ")
# model = tf.keras.models.load_model(file_location)

# model_architecture = model.to_json()
# with open("model/model_architecture.json", 'w') as json_file:
#     json_file.write(model_architecture)
#     model.save_weights("model/model_weights.h5")
#-----------------------------------------------------

def load_model():
    with open('model/model_architecture.json', 'r') as json_file:
        model = tf.keras.models.model_from_json(json_file.read())
        model.load_weights("model/model_weights.h5")

        return model

def compute_melspectrogram(y, sr):
    return power_to_db(melspectrogram(y=y, sr=sr), ref=np.max)

def compute_tempo(y, sr):
    return float(tempo(onset_envelope=onset_strength(y, sr=sr), sr=sr))

def compute_zero_crossing_rate(y):
    return sum(zero_crossings(y)) / len(zero_crossings(y))

def compute_average_spectral_flatness(y):
    return np.mean(spectral_flatness(y=y))

def predict_genre(file, model):
    audio = AudioSegment.from_file(file)
    audio_length = len(audio)

    if audio_length < 10000:
        return None, None
    elif audio_length > 10000:
        i = randrange(audio_length - 10000)
    else:
        i = 0
    j = i + 10000

    audio_sample = audio[i:j]
    audio_sample.export("cache.wav", format="wav")

    y, sr = load("cache.wav")

    melspectrogram = compute_melspectrogram(y, sr)
    melspectrogram = melspectrogram.reshape(
        1, *melspectrogram.shape, 1
    )

    extracted_features = np.array(
        [
            [compute_tempo(y, sr)],
            [compute_zero_crossing_rate(y)],
            [compute_average_spectral_flatness(y)],
        ]
    )
    extracted_features = extracted_features.reshape(
        1, *extracted_features.shape
    )
    probabilities = model.predict([melspectrogram, extracted_features])
    probabilities = probabilities.flatten()

    index = int(probabilities.argmax())
    genre = {
        0: 'Hip-Hop',
        1: 'Jazz',
        2: 'Pop',
        3: 'Rock',
        4: 'Soundtrack'
    }

    return genre[index], probabilities

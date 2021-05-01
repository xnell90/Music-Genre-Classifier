import numpy as np
import tensorflow as tf

from librosa import load, power_to_db, zero_crossings
from librosa.beat import tempo
from librosa.feature import melspectrogram, spectral_flatness
from librosa.onset import onset_strength

# Added for reference...
# ----------------------------------------------------
# file_location = input("Enter File Model Location: ")
# model = tf.keras.models.load_model(file_location)

# model_architecture = model.to_json()
# with open("model/model_architecture.json", 'w') as json_file:
#     json_file.write(model_architecture)
#     model.save_weights("model/model_weights.h5")
#-----------------------------------------------------

GENRES = {
    0: 'hip-hop',
    1: 'jazz',
    2: 'pop',
    3: 'rock',
    4: 'soundtrack'
}

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

def predict_genre(file_location):
    y, sr = load(file_location)
    model = load_model()

    melspectrogram = compute_melspectrogram(y, sr)
    extracted_features = np.array(
        [
            [compute_tempo(y, sr)],
            [compute_zero_crossing_rate(y)],
            [compute_average_spectral_flatness(y)],
        ]
    )
    probabilities = model.predict([melspectrogram, extracted_features])
    index = int(probabilities.argmax(axis=1))

    return GENRES[index]

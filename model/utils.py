import tensorflow as tf

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

def compute_melspectrogram():
    pass

def compute_tempo():
    pass

def compute_zero_crossing_rate():
    pass

def compute_average_spectral_flatness():
    pass

def predict_genre():
    pass

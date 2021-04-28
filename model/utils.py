import tensorflow as tf

def split_model():
    file_location = input("Enter File Model Location: ")
    model = tf.keras.models.load_model(file_location)

    model_architecture = model.to_json()
    with open("model/model_architecture.json", 'w') as json_file:
        json_file.write(model_architecture)

    model.save_weights("model/model_weights.h5")

def load_model():
    with open('model/model_architecture.json', 'r') as json_file:
        model = tf.keras.models.model_from_json(json_file.read())
        model.load_weights("model/model_weights.h5")

        return model

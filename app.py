import pandas as pd
from model.utils import *

print("-------------------------------------")
file_location = input("Enter File Location: ")
valid_mp3 = check_valid_mp3(file_location)

if valid_mp3:
    model = load_model()
    genre, probabilities = predict_genre(file_location, model)
    table = pd.DataFrame(
        {
            "Genre": ["Hip-Hop", "Jazz", "Pop", "Rock", "Soundtrack"],
            "Probability": list(probabilities.round(2))
        }
    )
    print("Predicted Genre: ", genre)
    print("-------------------------------------")
    print(table)
    print("-------------------------------------")
else:
    print("Error: The File Location Must Have The Following: ")
    print(" * The file location must point to an mp3 file.")
    print(" * The audio file must be at least 10 seconds long.")
    print("-------------------------------------")

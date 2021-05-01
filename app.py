import pandas as pd
from model.utils import *

print("-------------------------------------")
file_location = input("Enter File Location: ")
genre, probabilities = predict_genre(file_location)
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

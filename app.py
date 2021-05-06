import pandas as pd
import streamlit as st

from model.utils import *

st.title("Music Genre Classifier")
file = st.file_uploader(
    "Select an mp3 file to classify a track's genre: ", type=["mp3"]
)
if file:
    model = load_model()
    genre, probabilities = predict_genre(file, model)

    no_genre = genre is None
    no_probabilities = genre is None

    if no_genre and no_probabilities:
        st.write("Error: Please enter an mp3 file that is at least 10 seconds long.")
    else:
        st.write("Predicted Genre: ", genre)
        probability_table = pd.DataFrame(
            {
                "Genre": ["Hip-Hop", "Jazz", "Pop", "Rock", "Soundtrack"],
                "Probability": list(probabilities)
            }
        )

        st.table(probability_table)

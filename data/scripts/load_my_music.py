
# Pop           ----------- sample 2 ten seconds segments (.wav) format from music file
# Rock          ----------- sample 2 ten seconds segments (.wav) format from music file
# Soundtrack    ----------- sample 3 ten seconds segments (.wav) format from music file
# Hip-Hop       ----------- sample 6 ten seconds segments (.wav) format from music file
# Jazz          ----------- sample 6 ten seconds segments (.wav) format from music file
import os
import pandas as pd

from pydub import AudioSegment
from random import randrange
from tqdm import tqdm
from urllib.parse import unquote

my_music_metadata_df = pd.read_csv("my_music_metadata_(m).csv")
parent_working_dr = os.path.dirname(os.getcwd())
num_tracks = len(my_music_metadata_df)

for i in tqdm(range(num_tracks)):
    row = my_music_metadata_df.iloc[i]

    file_location = str(row['Location'])
    file_location = unquote(file_location).replace("file://", "")

    track_id = str(row['Track ID'])

    genre = row['Genre']
    genre_folder = genre.lower() + "/"

    if genre in ["Pop", "Rock"]: num_samples = 2
    elif genre == "Soundtrack": num_samples = 3
    else: num_samples = 6

    track_name = str(row['Name'])

    for _ in range(num_samples):
        audio = AudioSegment.from_file(file_location)

        start = randrange(len(audio) -  10000)
        end = start + 10000
        audio_sample = audio[start:end]

        new_filename = "0" + "_" + track_id + "_" +str(_) + ".wav"
        folder_location = parent_working_dr + "/genres/" + genre_folder

        audio_sample.export(folder_location + new_filename, format="wav")

import argparse
import pandas as pd
import os

from pydub import AudioSegment
from random import randrange

fma_small_metadata = pd.read_csv('fma_small_metadata.csv')
parser = argparse.ArgumentParser(description = 'Sampling From FMA Small Dataset By Genre')

parser.add_argument("--n_rock", type = int, default = 0, required = False)
parser.add_argument("--n_pop", type = int, default = 0, required = False)

args = parser.parse_args()

n_rock = args.n_rock
n_pop = args.n_pop

no_input = True
parent_working_dr = os.path.dirname(os.getcwd())

for n_genre, genre in [(n_rock, 'rock'), (n_pop, 'pop')]:
    if n_genre != 0:
        no_input = False
        genre_filter = fma_small_metadata.genre_top == genre.capitalize()
        track_id_samples = fma_small_metadata[genre_filter].sample(frac=1).head(n_genre)['track_id']

        for track_id in track_id_samples:
            formatted_track_id = '{:06d}'.format(track_id)
            file_location = 'fma_small/' + formatted_track_id[0:3] + '/' + formatted_track_id + '.mp3'
            audio = AudioSegment.from_file(file_location)

            start = randrange(len(audio) -  10000)
            end = start + 10000
            audio_sample = audio[start:end]

            new_filename = "1" + "_" + formatted_track_id + "_0.wav"
            folder_location = parent_working_dr + "/genres/" + genre + "/"

            audio_sample.export(folder_location + new_filename, format="wav")

if no_input:
    print("Error! Please define the genre you want to sample, along with the number of samples")

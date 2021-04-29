# Personal Music Collection

My personal music collection comes from an iTunes library. To extract the tracks from it into a specific format (10 second .wav file):
* I exported an xml file called **my_music_library.xml**, as it contains metadata about all my tracks in my music library.
* Next I ran the **load_personal_music_metadata.py** script so that you will have the necessary metadata in a tabular format (**my_music_metadata.csv**). I did a bit of exploratory data analysis and relabelled the tracks' genre based on the ablum and artist (**data_extraction.ipynb**, **my_music_metadata_(m).csv**). 
* Finally, after EDA and relabelling, I ran the **load_personal_music.py** script that will extract a 10 second segments from each track and save it as a .wav file.

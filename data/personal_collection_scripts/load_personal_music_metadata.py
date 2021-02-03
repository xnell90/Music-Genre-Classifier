'''
To extract your music metadata from the music app (Apple), you can export an xml
file that describes all of your songs (file -> library -> export library). From
there run the script below with the correct name of the xml file. After running
the script, you will have the data in the form of an csv file.
'''

import xml.etree.ElementTree as ET
import pandas as pd

#Create the tracklist from the xml tree
tree = ET.parse('my_music_library.xml') #<--- Insert the name of the xml file
root = tree.getroot()

main_dict = root.findall('dict')

for item in list(main_dict[0]):
    if item.tag == "dict":
        tracks_dict = item
        break

tracklist = list(tracks_dict.findall('dict'))

#Save the dataframe from dictionary as a csv file
music_data = {
    "Track ID": [],
    "Name": [],
    "Artist": [],
    "Album": [],
    "Genre": [],
    "Location": [],
    "Kind": [],
    "Size": [],
    "Total Time": []
}

for track in tracklist:
    track_info = list(track)
    for i in range(len(track_info)):
        if track_info[i].text in music_data.keys():
            name = track_info[i].text
            value = track_info[i + 1].text
            music_data[name].append(value)

music_df = pd.DataFrame.from_dict(music_data)
music_df.to_csv("my_music_metadata.csv", index=False)

'''
source: https://leojosefm.medium.com/python-analyzing-itunes-library-97bec60e13cb
'''

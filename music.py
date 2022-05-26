import music_tag
import os
import shutil
from pathvalidate import sanitize_filename

SOURCE = "D:\\Music 2022\\"

def mp3gen():
    for root, dirs, files in os.walk(SOURCE):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)

def organize():
    metadata = music_tag.load_file(mp3file)
    artist = sanitize_filename(str(metadata["artist"]))
    album = sanitize_filename(str(metadata["album"]))
    year = str(metadata["year"])
    os_file_name = mp3file.split("\\")[-1]
    new_folder_name = os.path.join(SOURCE, artist,  f"{year} - {album}")
    old_file_location = os.path.join(mp3file)
    new_file_location = os.path.join(new_folder_name, os_file_name)
    if not os.path.exists(new_folder_name):
        os.makedirs(new_folder_name)
    shutil.move(old_file_location, new_file_location)

def print_song(mp3file):
    metadata = music_tag.load_file(mp3file)
    song_name = metadata["tracktitle"]
    print(song_name)


for mp3file in mp3gen():
    print_song(mp3file)
    organize()
    
        

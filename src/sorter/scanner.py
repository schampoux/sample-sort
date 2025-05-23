from pathlib import Path 
import os 
import shutil


SOUND_TYPE_MAP = {
    "kick": "Kicks",
    "snare": "Snares",
    "clap": "Claps",
    "hat": "Hihats",
    "perc": "Percussion",
    "cymbal": "Cymbals",
    "808": "Tonal/808s",
    "bass": "Tonal/Bass_Shots",
    "synth": "Tonal/Synths",
    "piano": "Tonal/Piano",
    "loop": "Loops",
    "fx": "FX",
    "impact": "FX/Impacts",
    "rise": "FX/Risers",
    "vocal": "Vocals",
    "vox": "Vocals",
}

def classify_sound(file_name: Path ) -> str:
    name = file_name.lower()
    for key, value in SOUND_TYPE_MAP.items():
        if key in name: 
            return value
        else: 
            return "Misc"
            
def move_file(base_dir, dest_file_dir, file_name, input_dirpath):
    input_file_location = os.path.join(input_dirpath, file_name)
    print(input_file_location)


def main():
    packs = 'trial-run/packs' # "sounds/packs"
    base = '/Users/spun/Documents/music-prod/splice' 

    for sound_pack in os.listdir(os.path.join(base, packs)):
        sound_pack_path = os.path.join(base, packs, sound_pack)
        for dirpath, dirnames, filenames in os.walk(sound_pack_path):
            if filenames:
                # print(dirpath, dirnames, filenames,"\n")
                for file_name in filenames: 
                    move_file(base_dir)
        # dest_file_dir = classify_sound(path)
        


if __name__ =="__main__":
    main()
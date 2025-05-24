from pathlib import Path 
import os 
import shutil
import logging
import logging

logging.basicConfig(level=logging.DEBUG)

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

def classify(path: Path, rules) -> str:
    for pattern, category in rules:
        if pattern.search(path):
            return category 
    return "Uncategorized"

def move_file(base_dir, dest_file_dir, file_name, input_dirpath):
    input_file_location = os.path.join(input_dirpath, file_name)
    print(input_file_location)


def main():
    packs_path = '/home/spunion/Documents/splice' # "sounds/packs"
    base_path = '~/spunion/Documents/' 
    output_path = '~/spunion/Documents/sorted-dir'

    logging.log(logging.INFO, msg='Begin loop through sound packs:')
    packs = os.listdir(packs_path)
    for sound_pack in packs:

        sound_pack_path = os.path.join(base_path, packs_path, sound_pack)

        logging.log(logging.INFO,msg=f"Current pack: {sound_pack}")
        for dirpath, dirnames, filenames in os.walk(sound_pack_path):
            if filenames:
                logging.log(logging.INFO, msg=f"This subfolder {filenames} contains {len(filenames)} files.")
                # print(dirpath, dirnames, filenames,"\n")
                for file_name in filenames: 
                    pass
        # dest_file_dir = classify_sound(path)
        


if __name__ =="__main__":
    main()
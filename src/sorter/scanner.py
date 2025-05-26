from pathlib import Path 
from typing import List 
import os 
# import shutil
import logging
from sorter.utils import create_output_dict, fill_path, load_rules

logging.basicConfig(level=logging.DEBUG)



def classify(path: Path, rules) -> str:
    for pattern, category in rules:
        if pattern.search(path):
            return category 
    return "Uncategorized"

def classify_packs(dir: str) -> tuple[List[str], dict[str, str]]:
    packs = os.listdir(dir)
    unclassified_packs = []
    classified_packs = create_output_dict()

    for sound_pack in packs:
        sound_pack_path = os.path.join(dir, sound_pack)
        for dirpath, dirnames, filenames in os.walk(sound_pack_path):
            if filenames: 

                if ".DS_Store" in filenames:
                    if len(filenames) ==1:
                        continue 
                    filenames.remove(".DS_Store")

                classification_dir = classify(path = dirpath, rules = load_rules())     

                for file_name in filenames: 
                    classification_file = classify(path = os.path.join(dirpath[-1], file_name), rules = load_rules())
                    if classification_dir == "Uncategorized" and classification_file =="Uncategorized":
                        unclassified_packs.append(os.path.join(dirpath, file_name))
                        print("File and Directory remain Uncategorized, continuing\n", "Directory: ", dirpath, "\nFile Name: ", file_name, "\n")
                    full_path = os.path.join(dirpath, file_name)
                    classified_packs[classification_file].append(full_path)


        # dest_file_dir = classify_sound(path)
    return unclassified_packs, classified_packs

def move_file(base_dir, dest_file_dir, file_name, input_dirpath):
    input_file_location = os.path.join(input_dirpath, file_name)
    print(input_file_location)

def main():
    # mac
    # sound_packs_base_dir = '/Users/spun/Documents/music-prod/splice/trial-run/packs' # "sounds/packs"
    # output_path = '/Users/spun/Documents/music-prod/splice/sorted-sounds'
    
    # Linux
    sound_packs_base_dir = '/home/spunion/Documents/splice' 
    output_path = '/Users/spun/Documents/music-prod/splice/sorted-sounds'

    unclassif, classif = classify_packs(dir = sound_packs_base_dir)
        
if __name__ =="__main__":
    main()
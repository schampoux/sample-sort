from pathlib import Path 
from typing import DefaultDict, List 
import os 
import shutil
import logging
from sorter.utils import create_output_dict, fill_path 

logging.basicConfig(level=logging.DEBUG)



def classify(path: Path, rules) -> str:
    for pattern, category in rules:
        if pattern.search(path):
            return category 
    return "Uncategorized"

def classify_packs(dir: 'str') -> tuple[List[str], dict[str, str]]:
    packs = os.listdir(dir)
    unclassified_packs = []
    classified_packs = create_output_dict()

    for sound_pack in packs:

        sound_pack_path = os.path.join(base_path, packs_path, sound_pack)

        for dirpath, dirnames, filenames in os.walk(sound_pack_path):
            if filenames: 

                if ".DS_Store" in filenames:
                    if len(filenames) ==1:
                        continue 
                    filenames.remove(".DS_Store")

                classification_dir = classify(path = dirpath, rules = load_rules())     
                if classification_dir == "Uncategorized":
                    print(f"Current directory {dirpath} Uncategorized, cannot parse directory name for naming convention.")
                    for file in filenames: 
                        unclassified_packs.append(os.path.join(dirpath, file))
                    continue

                for file_name in filenames: 
                    print("split dirpath: ",dirpath.split('/'))
                    print("file_name: ", file_name)
                    classification_file = classify(path = os.path.join(dirpath[-1], file_name), rules = load_rules())
                    full_path = fill_path(os.path.join(dirpath, file_name))
                    classified_packs[classification_file].append(full_path)

                    # classified_packs.append(classification_file, full_path)
                    print("dir class: ", classification_dir, "\nfile class: ",classification_file, "\n")

        # dest_file_dir = classify_sound(path)
    return unclassified_packs, classified_packs

def move_file(base_dir, dest_file_dir, file_name, input_dirpath):
    input_file_location = os.path.join(input_dirpath, file_name)
    print(input_file_location)


def main():
    packs_path = '/Users/spun/Documents/music-prod/splice/trial-run/packs' # "sounds/packs"
    base_path = '/Users/spun/Documents/music-prod/splice' 
    output_path = '/Users/spun/Documents/music-prod/splice/sorted-sounds'
    
    unclassif, classif = classify_packs(dir = packs_path)
        
if __name__ =="__main__":
    main()
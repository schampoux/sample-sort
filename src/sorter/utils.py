import yaml 
import re 
from pathlib import Path 
from collections import defaultdict
from typing import DefaultDict, List 

def load_rules(path='./rules.yaml'):
    with open(path, 'r') as f: 
        config=yaml.safe_load(f)
    compiled_rules=[
        (re.compile(rule['pattern']), rule['category'])
        for rule in config['rules']
    ]
    return compiled_rules

def create_output_dict() -> DefaultDict[str, List]:
    compiled_rules = load_rules()
    labels = []
    for i in compiled_rules:
        labels.append(str(i[-1]))

    labels
    dct = defaultdict(list)
    for i in labels:
        dct[i]=[]
    return dct 

def fill_path(path: str):
    path.replace(' ', '-')
    return path 
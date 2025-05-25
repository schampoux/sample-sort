import yaml 
import re 
from pathlib import Path 

def load_rules(path='./rules.yaml'):
    with open(path, 'r') as f: 
        config=yaml.safe_load(f)
    compiled_rules=[
        (re.compile(rule['pattern']), rule['category'])
        for rule in config['rules']
    ]
    return compiled_rules

def fill_path(path: str):
    path.replace(' ', '-')
    return path 
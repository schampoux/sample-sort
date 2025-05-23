import yaml 
import re 

def load_rules(path='./rules.yaml'):
    with open(path, 'r') as f: 
        config=yaml.safe_load(f)
    compiled_rules=[
        (re.compile(rule['pattern']), rule['category'])
        for rule in config['rules']
    ]
    return compiled_rules
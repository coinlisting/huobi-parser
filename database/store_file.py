import json
import os
from json.decoder import JSONDecodeError

def writing_file(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)
def reading_file(file):
    if not os.path.exists(file):
        with open(file, 'w'):
            pass
    with open(file, "r") as f:
        try:
            data = json.load(f)
            return data
        except JSONDecodeError:
            return None
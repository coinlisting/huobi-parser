import json
from json.decoder import JSONDecodeError

def writing_file(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, ensure_ascii=False,indent=2)
def reading_file(file):
    with open(file, "r") as f:
        try: 
            return json.load(f)
        except JSONDecodeError:
            return {"TEXT":''}

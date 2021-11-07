import json

def writing_file(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
def reading_file(file):
    with open(file, "r") as f:
        return json.load(f)
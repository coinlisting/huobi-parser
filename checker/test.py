import json
data = {}
data['NAME'] = 'RARE2'
data['LINK'] = 'https://test.com/test2'
data['IS_LATEST'] = 'True'
with open('../coins/last_announced.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
# f = open('../coins/last_anounced.txt', 'w+')
# f.write('test2')
# f.close()
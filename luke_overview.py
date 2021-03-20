import json, pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
DATA_ROOT = PROJECT_ROOT / 'data'
#path = "/data/cad.json"

with open (DATA_ROOT/"cad.json") as f:
    data = json.load(f)

for d in data["data"]:
    #print(d[3])
    if "2000-Jan-01" in d[3]:
        print(d)

#print(data)
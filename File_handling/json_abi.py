import json

data = [
    {"Name" : "Abi", "Age" : "20", "City" : "Tvm"},
    {"Name" : "Abijith", "Age" : "21", "City" : "kollam"},
    {"Name" : "Achu", "Age" : "22", "City" : "Kochi"},
]

with open("json_abi.json","w") as f:
    json.dump(data, f ,indent=4)
    
with open("json_abi.json", "r") as f:
    read_data = json.load(f)
    for row in read_data:
        print(row)
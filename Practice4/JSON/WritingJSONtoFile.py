import json

data = {
    "name": "Ismail",
    "age": 17
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

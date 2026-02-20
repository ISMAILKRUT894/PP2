import json

python_data = {
    "name": "Ismail",
    "age": 17
}

json_string = json.dumps(python_data)

print(json_string)
print(type(json_string))

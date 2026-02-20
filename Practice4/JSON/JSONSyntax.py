import json
json_string = '{"name": "Ismail", "age": 17}'

data = json.loads(json_string)

print(data)
print(type(data))

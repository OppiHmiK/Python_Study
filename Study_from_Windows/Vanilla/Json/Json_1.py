import json

with open('rulu.json') as json_file:
    json_data = json.load(json_file)

json_string = json_data["json_string"]
print(json_string)

json_number = json_data["json_number"]
print(json_number)

json_array = json_data["json_array"]
print(json_array)

json_object = json_data["json_object"]
print(json_object)

json_bool = json_data["json_bool"]
print(json_bool)

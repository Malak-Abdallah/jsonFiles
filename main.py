import json

# json data type


# numbers:
# --> {"age": 20}

# boolean:
# --> {"results": true}

# null:
# --> {"name": null}

# JSON string
# string must be in double quotes
# --> employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'

people_string ='''{
    "people":[{
        "name":"John smith",
        "phone":"615-555-7164",
        "emails":["johnsmith@hotmail.com","john_smith@workpalce.com"],
        "has_license":false

},
{
        "name":"jane doe",
        "phone":"560-555-5153",
        "emails":null,
        "has_licence":true
}
]
}'''


# print(type(people_string))

# from json to python : json.loads
# Convert string to Python dict
data= json.loads(people_string)
'''
print(data)
print(type(data))

print(type(data['people']))
for person in data['people']:
    print(person)
    # each one of them is an object so i can access specific value
    print(person['name'])
'''

#from python to json

new_json_object = json.dumps(data, indent=2, sort_keys=True)
# indent is just for formatting the result
print(new_json_object)
print(type(new_json_object))

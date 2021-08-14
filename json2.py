import json

# red from json file
with open('states.json') as f:
    data = json.load(f) # without s

for state in data['states']:
    # print(state['name'],state['abbreviation'])
    del state['area_codes']

#write to json file:
with open('new_states.json','w') as f:
    json.dump(data, f, indent=2)




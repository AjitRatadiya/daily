import json

d = {'a': 'abc', 't': 123, 'sg': 43}

json_data = json.dumps(d)
data = json.loads(json_data)
print(json_data)
print(data)
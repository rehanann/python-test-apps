import json

d = {}

d["name"] = "luke"
d["age"] = "3"
# print(json.dumps(d, indent=4))
with open('json2.json', 'w') as fp:
    fp.write(json.dumps(d, indent=4))


with open('json2.json') as fp:
    data = json.load(fp)

print(data)


d = {}

d["name"] = "Matt"
d["age"] = "34"

data = json.dumps(d)

print(data)

with open('json2.json', 'a') as f:
    json.loads(d)

d["name"] = "chris"
d["age"] = "5"

with open('json2.json', 'a') as f:
    f.write(json.dumps(d, indent=4, separators=(". ", " = ")))


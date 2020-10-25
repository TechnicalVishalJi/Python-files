import json

data = '{"chai":"anda", "bewakoof":"ek"}'
print(data)

ok = json.loads(data)
print(ok['chai'])

data = {"chai":"anda", "zebra":"Thik hai", "bewakoof":False}
print(json.dumps(data, sort_keys=True))

#json.load is used to read the content of a file given at some location
with open ("os.py") as x:
    print(json.load(x))
  
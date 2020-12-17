import json

with open("state.json", "w+") as rf:
    data = json.load(rf)
    print(data)

data["led"] = not data["led"]
json.dump(data, rf)
print(data)

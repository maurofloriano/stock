import json

future = []
file="tweets1.json"
with open(f"labeled/{file}") as f:
    json_files = json.loads(f.read(), )
    for js in json_files:
        future.append(js)

future_labeled = []

for i in future:
    print(i["tweet"] + "\n")
    text = input("prompt: ") 
    if(text != "i"):
        j = i
        j["sentiment"] = text
        future_labeled.append(j)


with open(f"labeled/labeled_{file}", "w+") as f:
    f.write("[\n")
    for i in future_labeled:
        f.write(f"{json.dumps(i, ensure_ascii=False)},")
        f.write("\n")
    f.write("]")      
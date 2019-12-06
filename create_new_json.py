import json

files = [
    "bolsavalores20191001.json",
    "bolsavalores20191008.json",
    "bolsavalores20191014.json",
    "bolsavalores20191015.json",
    "bolsavalores20191020.json",
    "ibovespa20191001.json",
    "ibovespa20191008.json",
    "ibovespa20191014.json",
    "ibovespa20191015.json",
    "ibovespa20191020.json",
    "mercadoacoes20191001.json",
    "mercadoacoes20191008.json",
    "mercadoacoes20191014.json",
    "mercadoacoes20191015.json",
    "mercadoacoes20191020.json",
    "mercadofinanceiro20191001.json",
    "mercadofinanceiro20191008.json",
    "mercadofinanceiro20191014.json",
    "mercadofinanceiro20191015.json",
    "mercadofinanceiro20191020.json",
]

future = []

for file in files:
    print(file)
    with open(f"s3/{file}") as f:
        json_files = json.loads(f.read())
        for js in json_files:
            future.append({"tweet": js["tweet"], "sentiment": "undefined"})


int_max = 500
count = 0
i = 0
l = 0

while i < len(future):
    l = l+1
    name_file = f"labeled/tweets{l}.json"
    print(f"starting file with name {name_file}")
    with open(name_file, "w+") as f:
        f.write("[\n")
        count = 0
        while count < int_max and i < len(future):
            f.write(f"{json.dumps(future[i], ensure_ascii=False)},")
            f.write("\n")
            i = i + 1
            count = count + 1
        f.write("]")

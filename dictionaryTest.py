
d = {"a": 0, "b": 1, "c": 2}

key

print(d)

for key, value in d.items():
    # print(key, value)
    print(f"{key} : {value}")

print(d['a'], d['c']) # 0 2

d['a'] += 10
d['c'] += 20
print(d['a'], d['c']) #

kv = {10: 0, 20: 1, 30: "hello"}
print("keys: ", kv.keys())
print("values: ", kv.values())

string = "This is a string"
a = [{"name": 1}]
b = []
for i in a:
    b += [i.copy()]
print(b)
# b = a.copy()
b[0]["age"] = 4
print(a)
print(b)

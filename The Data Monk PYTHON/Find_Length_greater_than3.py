string_val = "The data monk is monk"
d = 3
l = []
for i in string_val.split():
    if len(i) > d:
        l.append(i)

print(l)
ns = " ".join(l)
print(ns)
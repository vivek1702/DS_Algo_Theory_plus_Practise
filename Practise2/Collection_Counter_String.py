from collections import Counter

sent = "the data monk will help in making in data science career"

recive = sent.split()
m = Counter(recive)
print(m)
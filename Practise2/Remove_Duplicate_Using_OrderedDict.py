# Orderdict and set both can be use to remove duplicate fromstring

from collections import OrderedDict, Counter

string1 = "the data monk helps in data science in course"


b = " ".join(OrderedDict.fromkeys(string1))
print(b)
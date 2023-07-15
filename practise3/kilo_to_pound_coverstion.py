def weight_to_pounds(tup):
  kilo = round(tup/2.2, 2)
  return kilo

tup = (173, 152, 119, 250)
coverted_output = list(map(weight_to_pounds, tup))
print(coverted_output)
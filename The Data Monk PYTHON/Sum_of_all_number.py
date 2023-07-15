def sum_of_all_num(a,b):
  s = 0
  for i in range(a,b+1):
    s += i
    
  return s
  
print(sum_of_all_num(10,99))
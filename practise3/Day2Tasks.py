#Task1
n = 1
while n <= 20:
  if n % 2 != 0:
    print(n)
    
  n += 1


#Task2
msg = input()
while msg != 'STOP':
  break

#Task3
n = int(input())
prime = 1
for i in range(2, int(n/2)+1):
    if n%i == 0:
        prime = 0
    
if prime == 0:
    print(False)
else:
    print(True)


#Task4
# palindrome check
def palindrome_check(n):
    b = ""
    for i in reversed(range(len(n))):
        b += n[i]

    return b
    # if a == n:
    #     return "Entered value is a palindrome"
    

a = input()
print(palindrome_check(a))


#Task 5
for i in range(21, 899):
  if i**2 > 899:
    break 
  print(i, ":", i**2)
print("Thats all folks!!")


#Task 6
# if a word is odd then first letter capital, else if word is odd then reverse the word 
s = list(map(str, input().split(" ")))
l = []
for i in range(0, len(s)):
    if i%2 == 0:
        l.append(s[i].capitalize())
    else:
        l.append(s[i][::-1])

print(*l)



#Task 7
num = 153
x = num
t = 0
while num != 0:
  a = num % 10
  t += a**3
  num = num//10
  
if t == x:
  print(t, "is an armstrong number ")
        


















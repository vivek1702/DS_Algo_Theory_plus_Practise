#Given two integers M & N, calculate and return their multiplication using recursion. 
# You can only use subtraction and addition for your calculation. No other operators are allowed.

def Multiplication_of_numbers(M,N):
    if N==0:
        return 0
    
    smalloutput = Multiplication_of_numbers(M, N-1)
    output = smalloutput + M
    return output

M = int(input(  ))
N = int(input(  ))
print(Multiplication_of_numbers(M,N))
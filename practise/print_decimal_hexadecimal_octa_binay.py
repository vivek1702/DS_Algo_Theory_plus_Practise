import math

def print_formatted(number):

    for i in range(1, number+1):
        print(math.trunc(i).rjust(2,""),"",oct(i)[2:],"",hex(i).upper()[2:],"",bin(i)[2:])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
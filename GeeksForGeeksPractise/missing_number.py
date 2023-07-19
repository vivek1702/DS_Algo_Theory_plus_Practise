def missingNumber(array,n):
    # create an empty array
    # temp = [0] * (n+1)
    
    # #iteration and store value in temp table as 1 if integer is present in it
    # for i in range(0,n):
    #     temp[array[i]-1] = 1

    # for i in range(0,n+1):
    #     if temp[i] == 0:
    #         return i+1
        
#another approach
    total = (n+1) * (n+2)//2  #here put single /
    sum_val = sum(array)
    return total - sum_val #return int(total-sum_val)

        
A = [6,1,2,8,3,4,7,10,5]
# A = [2]
n = len(A)
print(missingNumber(A,n))

            
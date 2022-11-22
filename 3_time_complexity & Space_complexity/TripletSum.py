def tripletSum(arr, n, num) :
    arr.sort()
    count = 0
    for i in range(n-2):
        target = num-arr[i]  # now this is my new target for pair sum
        
        l = i + 1
        r = n-1
        
        while l<r:
            psum = arr[l]+arr[r]
            
            if psum < target:
                l+=1
            elif psum > target:
                r-=1
            else:
                
                if arr[l]==arr[r]:
                    c = r-l+1
                    count += (c*(c-1)//2)
                    break
                
                newleft = l+1
                newright = r-1
                
                while newleft<=newright and arr[newleft]==arr[l]:
                    newleft+=1
                
                while newleft<=newright and arr[newright]==arr[r]:
                    newright-=1
                
                count += (newleft-l)*(r-newright)
                
                l = newleft
                r = newright
                

    return count




arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
num = 12
print(tripletSum(arr, n, num))
if __name__ == '__main__':
    #taking the string input
    num = input()
    #initalizing set to another variable
    num1 = set()
    #ranging taken input
    for i in range(0, int(num)):
        #taking string input inside loop for num times 
        country_name  = input()
        #set add values
        num1.add(country_name)

    result = len(num1)
    print(result)
    


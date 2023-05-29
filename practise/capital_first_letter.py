
def solve(s):
    nsl = []
    for i in s.split(' '):
        nsl.append(i.capitalize())
        
    ns = ' '.join(nsl)
    return ns
    

if __name__ == '__main__':


    s = input()

    result = solve(s)
    print(result)

  
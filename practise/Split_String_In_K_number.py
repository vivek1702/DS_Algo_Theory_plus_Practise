import textwrap


def merge_the_tools(string, k):
    arr = textwrap.wrap(string, k)
    
    for i in range(len(arr)):
        ll = []
        for j in arr[i]:
            if j not in ll:
                ll.append(j)

        print("".join(ll))
    # print(ll)
        


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
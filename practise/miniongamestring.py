def minion_game(string):
    v = ['A','E','I','O','U']
    k = 0
    s = 0
    for i in range(len(string)):
        if string[i] in v:
            k+=len(string) - i
        else:
            s+=len(string) - i
    if s > k:
        print("Stuart"+" "+ "%d" %s)
    elif k>s:
        print("Kevin"+" "+ "%d" %k)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

#minion games problem here given a string and two players are their
#if letter starts with vowel the player2 makes substring
#if it starts with consonents then player1 makes sustring
#we need to find the count of each player substring, whoever made the more number of substring wins
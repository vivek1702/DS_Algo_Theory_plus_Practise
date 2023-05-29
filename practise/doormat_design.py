if __name__ == '__main__':
    
    n = int(input())
    m = n*3
    design = ""
    
#top cone
for i in range(1, n, 2):
    design += (i * ("."+"|"+".")).center(m,"_")+"\n"

for i in range(1):
    design += "WELCOME".center(m,"_")+"\n"

for i in reversed(range(1, n, 2)):
    design += (i * ("."+"|"+".")).center(m,"_")+"\n"
    
print(design)
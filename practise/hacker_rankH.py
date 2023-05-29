if __name__ == '__main__':

    width = int(input())
    design = ""

#top crown
for i in range(1, width*2, 2):
    design += (i * "H").center(width*2-1, " ") + "\n"

#topn square
s1 = (width * 'H').center(width * 2 - 1 , " ") + (width * 2 + 1) * " "
for i in range(width + 1):
    design = design + (2 * s1) + '\n'

s2 = (width * 5 * 'H').center(width * 6 - 1 , " ")

for i in range(0 , width , 2):
    design = design + s2 + '\n'

s3 = (width * 'H').center(width * 2 - 1 , " ") + (width * 2 + 1) * " "
for i in range(width + 1):
    design = design + (2 * s3) + '\n'

for i in reversed(range(1, width*2, 2)):
    design += (width * 4)*" " +(i * "H").center(width*2-1, " ") + "\n"



print(design)

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

def interpret(command):
    l = ''
    a=''
    for i in command:
        if i == "G":
            l += 'G'
        elif i == '(' or i == 'a' or i == 'l':
            a += i
        elif i == ')' and a == '(al':
            a = ''
            l += 'al'
        elif i == ')' and a == '(':
            a = ''
            l += 'o'
    return l

# optimal solution would be using regurlar experssion 're.sub('\(\)', 'o', re.sub('\(al\)', 'al', command))'
# or replace 'command.replace('()','o').replace('(al)','al')' 
# but this will not work for many different scenrio


inp = "G()()()()(al)"
# "G()(al)"
print(interpret(inp))

import re

def function(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

x = int(input())
for _ in range(x):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", function,input()))
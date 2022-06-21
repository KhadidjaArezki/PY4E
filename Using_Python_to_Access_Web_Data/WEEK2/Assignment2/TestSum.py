import re
hand=open('C:/Users/PC/Documents/Assignment1/regex_sum_42.txt')
sum=0
for line in hand:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    for n in x:
        print(n)
        sum+=int(n)
print(sum)


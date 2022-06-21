import re
hand=open('C:/Users/PC/Documents/Assignment1/regex_sum_917813.txt')
num=list()
for line in hand:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    if len(x)>=1:
        for n in x:
            n=int(n)
            print(n)
            num.append(n)
print(sum(num))

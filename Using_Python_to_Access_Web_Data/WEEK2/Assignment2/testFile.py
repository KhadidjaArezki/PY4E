text='Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative 7 and rewarding activity.  You can write programs for many reasons, ranging from making your living to solving 8837 a difficult data analysis problem to having fun to helping 128 someone else solve a problem.  This book assumes that everyone needs to know how to program ...'
sum=0
import re
words=text.split()
print(words)
num=re.findall('[0-9]+',text)
print(num)
for n in num:
    sum+=int(n)
print(sum)

#version 2
text='Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative 7 and rewarding activity.  You can write programs for many reasons, ranging from making your living to solving 8837 a difficult data analysis problem to having fun to helping 128 someone else solve a problem.  This book assumes that everyone needs to know how to program ...'
import re
#words=text.split()
#print(words)
num=re.findall('[0-9]+',text)
print(num)
for i in range(len(num)):
    num[i]=int(num[i])
print(sum(num))
#oneliner
#print([int(n) for n in re.findall('[0-9]+',text)])

import re
hand=[line.rstrip() for line in open('C:/Users/PC/Documents/Assignment1/regex_sum_917813.txt').read()]
print(sum([int(n) for n in re.findall('[0-9]+',line for line in hand)]))
#line.rstrip() for line in 'C:/Users/PC/Documents/Assignment1/regex_sum_917813.txt'.read()
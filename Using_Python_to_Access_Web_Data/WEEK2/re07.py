# Search for lines that have an at sign between characters
# The characters must be a letter or number
import re
hand = open('C:/Users/PC/Documents/Khadidja/INF 0706 BTS RESEAU CI/Courses/PY4E/Using Python to Access Web Data/WEEK2/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@[a-zA-Z]\S+', line)
    if len(x) > 0:
        print(x)

# Search for lines that contain 'Author:' followed by any characters,
# an at sign, and any non whitespace character
# Then print the character group that follows the at sign
import re
hand = open('C:/Users/PC/Documents/Khadidja/INF 0706 BTS RESEAU CI/Courses/PY4E/Using Python to Access Web Data/WEEK2/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('Author:.*@(\S+)', line)
    if not x: continue
    print(x)

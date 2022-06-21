# Search for lines that contain 'From'
import re
hand = open('C:/Users/PC/Documents/Khadidja/INF 0706 BTS RESEAU CI/Courses/PY4E/Using Python to Access Web Data/WEEK2/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

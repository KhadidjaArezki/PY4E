import sqlite3
import string
import zlib

conn1 = sqlite3.connect('C:/Users/PC/Documents/bookRevs.sqlite')
cur1 = conn1.cursor()
title = 'The Da Vinci Code'
copies = []
cur1.execute('SELECT id FROM Products WHERE title = ?', (title,))
for row in cur1:
    copies.append(row[0])
print(copies)

counts = dict()
reviews = 0
cur1.execute('SELECT product_id, headline FROM Reviews')
for row in cur1:
    if row[0] in copies:
        headline = zlib.decompress(row[1])
        #print(type(headline))
        headline = headline.decode('utf8', 'ignore')
        headline = headline.translate(str.maketrans('','',string.punctuation))
        headline = headline.translate(str.maketrans('','','1234567890'))
        headline = headline.strip()
        headline = headline.lower()
        words = headline.split()
        for word in words:
            if len(word) < 4 : continue
            counts[word] = counts.get(word,0) + 1
        reviews+=1
        if reviews%10000 == 0:
            print(reviews, 'reviews')
    # print('Done gathering reviews for copy:', copy)

conn1.commit()
conn1.close()

sort_words = sorted(counts, key=counts.get, reverse=True)
#print(head_words[:20])

best = [counts[word] for word in sort_words[:100]]
highest = max(best)
lowest = min(best)
print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('bookword.js','w')
fhand.write("bookword = [")
first = True
for k in sort_words[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)                # text normalisation for js

    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to bookword.js")
print("Open bookword.htm in a browser to see the vizualization")

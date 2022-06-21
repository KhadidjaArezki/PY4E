import sqlite3

conn1 = sqlite3.connect('C:/Users/PC/Documents/bookRevs.sqlite')
cur1 = conn1.cursor()

titles = {}
title_id = 1
count = 0
print('Traversing Products and Filling up titles ---')

while title_id <= 779710:
    cur1.execute('SELECT title FROM Products where id = ?', (title_id,))
    title = cur1.fetchone()[0]
    if title not in titles:
        titles[title] = [[title_id], 0, 0.0]
    else:
        titles[title][0].append(title_id)
    title_id+=1 
    if title_id % 10000 == 0:
        print( title_id,'rows traversed' )
print('Done')

print('titles length',len(titles))

print('Traversing Reviews and Filling up titles ---')
traversed = 0
curr = conn1.cursor()
curr.execute('SELECT product_id, rating FROM Reviews')
for row in  curr:
    #print(row)
    product_id = row[0]
    rating = row[1]
    cur1.execute('SELECT title FROM Products WHERE id = ?', (product_id,))
    title = cur1.fetchone()[0]
    titles[title][1]+=1
    titles[title][2]+=float(rating)
    traversed+=1
    if traversed%10000 == 0:
       print(traversed, ' rows traversed') 
    #print(titles[title])
print('Done')
conn1.commit()
conn1.close()  

# for title in titles:
#     print(title, titles[title])
#     count+=1
#     if count == 20:
#         break

count = 0
conn2 = sqlite3.connect('C:/Users/PC/Documents/uniqBooks.sqlite')
cur2 = conn2.cursor()
cur2.execute('CREATE TABLE IF NOT EXISTS Books (title TEXT, num_copies INTEGER, num_reviews INTEGER, avg_rating REAL)')
for title in titles:
    #print(title, titles[title])
    num_copies = len(titles[title][0])
    num_reviews = titles[title][1]
    avg_rating = round(titles[title][2] / num_reviews, 1)
    try:
        cur2.execute('INSERT INTO Books (title, num_copies, num_reviews, avg_rating) VALUES (?, ?, ?, ?)',(title, num_copies, num_reviews, avg_rating))
        count+=1
        if count % 10000 == 0:
            conn2.commit()
            print(count, 'rows inserted')
    except KeyboardInterrupt:
        conn2.commit()
        conn2.close()
        break

conn2.commit()
conn2.close()  



# for item in titles.items():
#     if product_id in item[1][0]:
#         title = item[0]



#         try:
#             cur1.execute('SELECT id FROM Products WHERE title= ?', (title,))
#             copies= []
#             for i in cur1.fetchall():
#                 copies.append(*i)
#             print('copies ids list: ',copies)
#             ratings = []
#             for copy in copies:
#                 cur1.execute('SELECT rating FROM Reviews WHERE product_id = ?', (copy,))
#                 for i in cur1.fetchall():
#                     ratings.append(*i)
#                 #print(ratings)
#             num_reviews = len(ratings)
#             avg_rating = round(sum(ratings)/ num_reviews, 1)
#             titles[title] = [len(copies), num_reviews, avg_rating]
#             print(titles[title])
#             title_id+=1       
#             cur2.execute('INSERT INTO Books (title, num_copies, num_reviews, avg_rating) VALUES (?, ?, ?, ?)',(title, titles[title][0], titles[title][1], titles[title][2]) )
#             count+=1
#             if count % 1000 == 0:
#                 conn2.commit()
#                 print(count, 'rows inserted')
#         except KeyboardInterrupt:
#             conn2.commit()
#             conn2.close()
#             break
#     else:
#         continue
# conn2.commit()
# conn2.close()  

            
import csv
#import sqlite3
#import zlib
# import gzip
filename = "C:/Users/PC/Documents/Khadidja/Courses/PY4E/Capstone_RPandVDatawithPython/WEEK5/amazon_reviews_us_Books/amazon_reviews_us_Books_v1_02.tsv"
# conn = sqlite3.connect('C:/Users/PC/Documents/bookRevs.sqlite')
# cur = conn.cursor()
# cur.executescript('''CREATE TABLE IF NOT EXISTS Products (id  INTEGER NOT NULL PRIMARY KEY  UNIQUE, product_id TEXT UNIQUE, title TEXT);
#                      CREATE TABLE IF NOT EXISTS Customers (id  INTEGER NOT NULL PRIMARY KEY  UNIQUE, customer_id TEXT UNIQUE);
#                      CREATE TABLE IF NOT EXISTS Reviews (product_id INTEGER, customer_id INTEGER, review_id TEXT UNIQUE, rating INTEGER, helpful_votes INTEGER, 
#                        total_votes INTEGER, verified_purchase VARCHAR(1), date TEXT, headline BLOB, body BLOB)
#                    ''')

# count = 0
with open(filename, encoding="utf8", newline='') as tsv_file:
    # gzip_tsv = gzip.GzipFile(fileobj=tsv_file)
#    read_tsv = csv.DictReader(tsv_file, delimiter="\t")        
    print(len(tsv_file.readlines()))                                             
#     for i, row in enumerate(read_tsv):
#         if i < 2770599:
#             continue
#         else:
#             try:
   
#                 product = row['product_id']
#                 title = row['product_title']
#                 customer = int(row['customer_id'])
#                 rating = int(row['star_rating'])
#                 review_id = row['review_id']
#                 helpful = int(row['helpful_votes'])
#                 total = int(row['total_votes'])
#                 verified = row['verified_purchase']
#                 date = row['review_date']
#                 headline = zlib.compress(row['review_headline'].encode())         
#                 body = zlib.compress(row['review_body'].encode())
#                 #print(product,title,customer,rating,review_id,helpful,total,verified,date)

#                 cur.execute('''INSERT OR IGNORE INTO Products (product_id, title) VALUES (?, ?)''', (product, title))
#                 cur.execute('''INSERT  OR IGNORE INTO Customers (customer_id) VALUES (?)''', (customer,))
#                 cur.execute('''SELECT id FROM Customers WHERE customer_id = ?''', (customer,))
#                 customer_id = cur.fetchone()[0]
#                 cur.execute('''SELECT id FROM Products WHERE product_id = ?''', (product,))
#                 product_id = cur.fetchone()[0]
#                 cur.execute('''INSERT INTO Reviews (product_id, customer_id, review_id, rating, helpful_votes, total_votes, verified_purchase, date,
#                                 headline, body) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (product_id, customer_id, review_id, rating, helpful, total, verified, date, headline, body))
#                 count+=1
#                 if count % 10000 == 0:
#                     conn.commit()
#                     print(count, 'rows inserted')

#             except KeyboardInterrupt:
#                 conn.commit()
#                 conn.close()        
#             except:
#                 pass
# conn.commit()
# conn.close()        
        

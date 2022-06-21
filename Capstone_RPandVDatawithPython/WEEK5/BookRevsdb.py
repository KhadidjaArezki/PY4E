import csv
import sqlite3

filename = 'C:/Users/PC/Documents/Khadidja/Courses/PY4E/Capstone_RPandVDatawithPython/WEEK5/Books.csv'
conn= sqlite3.connect('reviewsdb.sqlite')
cur=conn.cursor()
cur.executescript('''CREATE TABLE IF NOT EXISTS Products (id INTEGER  PRIMARY KEY UNIQUE, product_id TEXT UNIQUE);
                    CREATE TABLE IF NOT EXISTS Customers (id INTEGER  PRIMARY KEY UNIQUE, customer_id TEXT UNIQUE);
                    CREATE TABLE IF NOT EXISTS Reviews (product_id INTEGER, customer_id INTEGER, rating REAL, unixtime INTEGER)''')

count = 0 
products = []
with open (filename, newline='') as csvfile:
    csvreader= csv.DictReader(csvfile,fieldnames=['product_id', 'customer_id', 'rating', 'time'])
    for row in csvreader:        
        product = row['product_id']
        if len(products) < 200 and product not in products:
            products.append(product)
            print(products)
        
        if product in products:
            customer = row['customer_id']
            rating = float(row['rating'])
            time = int(row['time'])       
            cur.execute('''INSERT OR IGNORE INTO Products (product_id) VALUES (?)''', (product,))
            cur.execute('''INSERT  OR IGNORE INTO Customers (customer_id) VALUES (?)''', (customer,))
            cur.execute('''SELECT id FROM Products WHERE product_id = ?''', (product,))
            product_id = cur.fetchone()[0]
            cur.execute('''SELECT id FROM Customers WHERE customer_id = ?''', (customer,))
            customer_id = cur.fetchone()[0]
            cur.execute('''INSERT INTO Reviews (product_id, customer_id, rating, unixtime) VALUES (?, ?, ?, ?)''', (product_id, customer_id, rating, time))
            count+=1
            #print(product, customer, rating, time)
            if count % 250 == 0:
                conn.commit()
                print(count,' reviews inserted')
            if count == 55000:
                break

cur.executescript('''SELECT Products.product_id, Customers.customer_id, Reviews.rating FROM Reviews JOIN Products JOIN Customers 
ON Reviews.product_id = Products.id AND Reviews.customer_id = Customers.id  ORDER BY Reviews.rating DESC, Products.id LIMIT 100 ''')    
        

 
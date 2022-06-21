import sqlite3
import re
conn = sqlite3.connect('Assignment2.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)')
cur.execute('DELETE FROM Counts')

dict_dom=dict()
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'C:\\Users\\PC\\Documents\\Khadidja\\Courses\\PY4E\\Using Databases with Python\\WEEK2\\mbox.txt'
fh = open(fname)
for line in fh:
    domains=re.findall('From .*@([a-z.]+)', line)
    if domains is not []:
        for org in domains:
            #dict_dom[org]=dict_dom.get(org,0)+1
            cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''',(org,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
            

conn.commit()       
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
itr=cur.execute(sqlstr)
for row in itr:
    print(str(row[0]), row[1])

cur.close() 

#for org in dict_dom:
    #print(org, dict_dom[org])
    

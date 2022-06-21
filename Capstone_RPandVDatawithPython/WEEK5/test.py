# import csv
# import sqlite3
# import zlib
# # import gzip
# #filename = "C:/Users/PC/Documents/Khadidja/Courses/PY4E/Capstone_RPandVDatawithPython/WEEK5/sample_us.tsv"
# conn = sqlite3.connect('testdb.sqlite')
# cur = conn.cursor()
# cur.executescript('''CREATE TABLE IF NOT EXISTS test (id  INTEGER NOT NULL PRIMARY KEY  UNIQUE, int INTEGER)''')

# #sqlite3 amzBookRevsdb.sqlite ".recover" | sqlite3 bookRevs.sqlite
# # with open(filename, encoding="utf8", newline='') as tsv_file:
# #     read_tsv = csv.DictReader(tsv_file, delimiter="\t")                                                                                          
# #     for row in read_tsv:
#           if i < 514255:
#             continue
#         else:
#             try:
# try:
#     rating = int('s')
# except :
#     pass
# cur.execute('''INSERT INTO test (int) VALUES (?)''', (rating,))
# conn.close()        
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1+l2
print(l3)
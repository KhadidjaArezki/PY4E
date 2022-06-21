import csv
import sqlite3

conn= sqlite3.connect('resumesdb.sqlite')
cur=conn.cursor()
cur.executescript('''DROP TABLE IF EXISTS Resumes;
                  CREATE TABLE Resumes(id INTGER UNIQUE, name TEXT, gender TEXT, ethnicity TEXT, quality TEXT, call TEXT, city TEXT, 
                   jobs INTEGER, experience INTEGER, honors TEXT, volunteer TEXT, military TEXT, holes TEXT, school TEXT, email TEXT, 
                   computer TEXT, special TEXT, college TEXT, minimum TEXT, equal TEXT, wanted TEXT, requirements TEXT, reqexp TEXT, 
                   reqcomm TEXT, reqeduc TEXT, reqcomp TEXT, reqorg TEXT, industry TEXT)''')
count=0
with open('C:/Users/PC/Documents/Khadidja/Courses/PY4E/Capstone_RPandVDatawithPython/WEEK3/ResumeNames.csv', newline='') as csvfile:
    csvreader= csv.DictReader(csvfile,fieldnames=[product, customer, rating, time])
    for row in csvreader: 
        #valist=[]
        #for value in row.values():
            #valist.append(value)
        cur.execute('''INSERT INTO Resumes(id,name,gender,ethnicity,quality,call,city,jobs,experience,honors,volunteer,military,holes,
                        school,email,computer,special,college,minimum,equal,wanted,requirements,reqexp,reqcomm,reqeduc,reqcomp,reqorg,industry) 
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(row['resume'],row['name'],row['gender'],row['ethnicity'],
                        row['quality'],row['call'],row['city'],row['jobs'],row['experience'],row['honors'],row['volunteer'],row['military'],
                        row['holes'],row['school'],row['email'],row['computer'],row['special'],row['college'],row['minimum'],row['equal'],
                        row['wanted'],row['requirements'],row['reqexp'],row['reqcomm'],row['reqeduc'],row['reqcomp'],row['reqorg'],row['industry']))
                            #valist[0],valist[1],valist[2],valist[3],valist[4],valist[5],valist[6],valist[7],valist[8],valist[9],valist[10],valist[11],valist[12],valist[13],valist[14],valist[15],valist[16],valist[17],valist[18],valist[19],valist[20],valist[21],valist[22],valist[23],valist[24],valist[25],valist[26],valist[27]))
        
        count+=1
        if count % 50 == 0 :
            conn.commit()
            print('Fifty rows inserted')
        
conn.close()

        #datastr=','.join(row)
        #datalist= datastr.split(',')
        #print(datalist[2]+datalist[3]+datalist[5])
        #if (row['ethnicity']=='afam') and(row['gender']=='female'):
            #print(row['name'].strip()+'\t',row['gender'])
            #count+=1
    #print('Total num of female afams: ',count)
        
        

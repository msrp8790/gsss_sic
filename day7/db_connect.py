import pymysql

connection = pymysql.Connect(host = 'localhost',user = 'root',password = 'msrp@8790',database = 'prerana_db',port = 3306,charset = 'utf8')

if connection:
    print('Database connected')
else:
    print('Database connection failed')
connection.close()
print('Database disconnected')

import pymysql

def connect_db():
    try:
        conn = pymysql.Connect(host = 'localhost',user = 'root',password = 'msrp@8790',database = 'prerana_db',port = 3306,charset = 'utf8')
        print('Database connected')
        return conn
    except:
        print('Database connection failed')

def disconnect_db(connection):
    connection = connect_db()
    if connection:
        connection.close()
        print('Database disconnected')


#coding=utf-8
import  MySQLdb
db=MySQLdb.connect( host = '192.188.0.34',
    port = 3306,
    user = 'root',
    passwd = '28320071',
    db = 'dbkunchi',
    charset='utf-8')
cursor = db.cursor()
cursor.execute("select * from tuser")
data=cursor.fetchone()
print data
db.close()

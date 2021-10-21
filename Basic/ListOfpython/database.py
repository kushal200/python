import pymysql
db=pymysql.connect(host="localhost",user="root",password="")
sql="create database db"
cursor=db.cursor()
cursor.execute(sql)
db.commit()

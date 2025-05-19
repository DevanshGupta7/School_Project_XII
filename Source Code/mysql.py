import mysql.connector as sqltor
import service1

mydb = sqltor.connect(
    host="localhost",
    user="Admin",
    password="123456",
    daatabase="UserData"
)
result = service1.Service1.display_report()

mycur = mydb.cursor()
mycur.execute("create database if not exists UserData")
mycur.execute("create table User(Result varchar(100))")
mycur.execute("insert into User values(result)")
mydb.commit()
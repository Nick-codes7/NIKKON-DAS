import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="",
    database="library"
)
mycursor=mydb.cursor()
'''mycursor.execute("Create database Library")'''
'''mycursor.execute("Create table books(number_of_books int(2) PRIMARY KEY AUTO_INCREMENT, book_name varchar(155), quantity varchar(155), price varchar(10), author varchar(120))")'''
sql="Insert into books(number_of_books,book_name,quantity,price,author)values(%s,%s,%s,%s,%s)"
val=[
    ('',"The Hobbit","1pc","1050rs","J.R.R.Tolkien"),
    ('',"To The Light House","5pc","579rs","Virginia Woolf"),
    ('',"Crime and Punishment","2pc","750rs","Fyodor Dostoevsky"),
    ('',"The Great Indian Novel","3pc","900rs","Shashi Tharoor")
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Database created successfully")
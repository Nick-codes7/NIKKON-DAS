import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="",
    database="studentmanagement"
)
mycursor=mydb.cursor()
'''mycursor.execute("Create database Studentmanagement")'''
'''mycursor.execute("Create table students (id int(2) PRIMARY KEY AUTO_INCREMENT, name varchar(155), address varchar(155), phone varchar(10), contact_person varchar(120))")'''
sql="Insert into students(id,name,address,phone,contact_person)values(%s,%s,%s,%s,%s)"
val=[
    ('',"Nikkon Das","Kurseong","8016225995","Mr.P.Das"),
    ('',"Kashyap Thakuri","Kurseong","9880911620","Mr.K.Thakuri"),
    ('',"Dipankar Paul","Siliguri","98809116768","Mr.P.Paul"),
    ('',"Faraz Asim","Kurseong","9880911620","Mr.K.Asim")
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Database created succesfully")
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="",
    database="kitchen"
)
mycursor=mydb.cursor()
'''mycursor.execute("Create database Kitchen")'''
'''mycursor.execute("Create table recipe(number_of_recipes int(2) PRIMARY KEY AUTO_INCREMENT, food_name varchar(155), quantity varchar(155), ingredients varchar(10), cook_name varchar(120))")'''
sql="Insert into recipe(number_of_recipes,food_name,quantity,ingredients,cook_name)values(%s,%s,%s,%s,%s)"
val=[
    ('',"Chicken Butter Masala","250ml","Chicken","Nikkon Das"),
    ('',"Paneer Lababdar","500ml","Paneer","Nikkon Das"),
    ('',"Masala Dosa","100ml","Potatoes","Balasupram Gopal Ayyer"),
    ('',"Uttapam","150ml","Onions","Balaswami Muthuswami Viru Gopal Ayyer")
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Database created successfully")
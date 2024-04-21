import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password ="",
    database="inventory"
)
mycursor=mydb.cursor()
'''mycursor.execute("Create database Inventory")'''
'''mycursor.execute("Create table management(number_of_products int(2) PRIMARY KEY AUTO_INCREMENT, name varchar(155), quantity varchar(155), date varchar(10), contact_number varchar(120))")'''
sql="Insert into management(number_of_products,name,quantity,date,contact_number)values(%s,%s,%s,%s,%s)"
val=[
    ('',"Water Bottle","1000pc","12/04/2024","8016225995"),
    ('',"Handkerchief","500pc","1/04/2024","9873452178"),
    ('',"Books","200pc","2/04/2021","7645324516"),
    ('',"Powerbank","300pc","1/04/2023","8754632415")
    ]
mycursor.executemany(sql,val)
mydb.commit()
print("Database created successfully")
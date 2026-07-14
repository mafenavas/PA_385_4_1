import mysql.connector as dbconnect

from mysql.connector import Error

try:
    myconnection = dbconnect.connect(host='localhost',database='registrationdb',user='root',password='password')

    if myconnection.is_connected():
        print('Successfully Connected to MySQL database')
        cursor = myconnection.cursor()

        create_table = "CREATE TABLE IF NOT EXISTS `user_table` (`email` varchar(100) NOT NULL,\
        `Name` varchar(50) NOT NULL,\
        `Password` varchar(50) NOT NULL)"

        cursor.execute(create_table)

        mysql_insert_query = """INSERT INTO user_table (email, Name, Password) 
                           VALUES (%s, %s, %s) """

        records_to_insert = [('ywbaek@perscholas.org', 'young', 'letsgomets'),
                            ('mcordon@perscholas.org', 'marcial', 'perscholas'),
                            ('mhaseeb@perscholas.org', 'haseeb', 'platform')]
   
        cursor.executemany(mysql_insert_query, records_to_insert)
        myconnection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")

except Error as e:
        print("Error while connecting to Database", e)
finally:
        if myconnection.is_connected():
            cursor.close()
            myconnection.close()
        print("Database connection is closed")
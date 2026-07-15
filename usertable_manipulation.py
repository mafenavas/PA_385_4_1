import mysql.connector as dbconnect

from mysql.connector import Error

def generate_user_table():
    try:
        myconnection = dbconnect.connect(host='localhost',database='registrationdb',user='root',password='password')

        if myconnection.is_connected():
            print('Successfully Connected to MySQL database')
            cursor = myconnection.cursor()

            create_table = "CREATE TABLE IF NOT EXISTS `user_table` (`email` varchar(100) PRIMARY KEY,\
            `Name` varchar(50) NOT NULL,\
            `Password` varchar(50) NOT NULL)"

            cursor.execute(create_table)

    except Error as e:
            print("Error while connecting to Database", e)
    finally:
            if myconnection.is_connected():
                cursor.close()
                myconnection.close()
            print("Database connection is closed")

def get_all_users():
    try:
        myconnection = dbconnect.connect(host='localhost',database='registrationdb',user='root',password='password')

        if myconnection.is_connected():
            print('Successfully Connected to MySQL database')
            cursor = myconnection.cursor()

            mysql_insert_query = """INSERT IGNORE INTO user_table (email, Name, Password) 
                            VALUES (%s, %s, %s) """

            records_to_insert = [('ywbaek@perscholas.org', 'young', 'letsgomets'),
                                ('mcordon@perscholas.org', 'marcial', 'perscholas'),
                                ('mhaseeb@perscholas.org', 'haseeb', 'platform')]
    
            cursor.executemany(mysql_insert_query, records_to_insert)
            myconnection.commit()
            print(cursor.rowcount, "Record inserted successfully into user_table table")

    except Error as e:
            print("Error while connecting to Database", e)
    finally:
            if myconnection.is_connected():
                cursor.close()
                myconnection.close()
            print("Database connection is closed")

def get_user_by_name(name):
    try:
        myconnection = dbconnect.connect(host='localhost',database='registrationdb',user='root',password='password')
        
        if myconnection.is_connected():
            print('Successfully Connected to MySQL database')
            cursor = myconnection.cursor()

            mysql_query_get_user = f"""SELECT email, password
            FROM user_table
            WHERE name = '{name}'""";

            cursor.execute(mysql_query_get_user)
            record_1 = cursor.fetchall()
            print(record_1)

    except Error as e:
        print("Error while connecting to Database", e)
    finally:
        if myconnection.is_connected():
                cursor.close()
                myconnection.close()
        print("Database connection is closed")

def validate_user(email, password):
    try:
        myconnection = dbconnect.connect(host='localhost',database='registrationdb',user='root',password='password')
        
        if myconnection.is_connected():
            print('Successfully Connected to MySQL database')
            cursor = myconnection.cursor()

            mysql_query_validate_user = f"""SELECT name
            FROM user_table
            WHERE email = '{email}' AND password = '{password}'""";

            cursor.execute(mysql_query_validate_user)
            record_2 = cursor.fetchall()
            print(record_2)

    except Error as e:
        print("Error while connecting to Database", e)
    finally:
        if myconnection.is_connected():
                cursor.close()
                myconnection.close()
        print("Database connection is closed")

def update_user(email, name, password):
    try:
        myconnection = dbconnect.connect(host='localhost',database='registrationdb',user='root',password='password')
        
        if myconnection.is_connected():
            print('Successfully Connected to MySQL database')
            cursor = myconnection.cursor()

            mysql_query_update_user = f"""UPDATE user_table
            SET name = '{name}'
            WHERE email = '{email}' AND password = '{password}'""";

            cursor.execute(mysql_query_update_user)
            myconnection.commit()
            print(cursor.rowcount, "Record updated successfully into user_table table")

    except Error as e:
        print("Error while connecting to Database", e)
    finally:
        if myconnection.is_connected():
                cursor.close()
                myconnection.close()
        print("Database connection is closed")



get_user_by_name('marcial')
validate_user('mhaseeb@perscholas.org', 'platform')
update_user('mcordon@perscholas.org', 'jose', 'perscholas')
     



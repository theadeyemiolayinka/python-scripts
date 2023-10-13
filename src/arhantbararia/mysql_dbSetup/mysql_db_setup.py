import mysql.connector
from mysql.connector import errorcode
import getpass

class InvalidUserName(Exception):
    # raised when invalud username for db is input
    pass



if __name__ == "__main__":

    try:
        host_address = input("Enter Host Address of Mysql User (default = localhost): ")
        if not host_address:
            host_address = 'localhost'

        host_port = input("Enter Mysql Server port (default = 3306): ")
        if not host_port:
            host_port = 3306
        else:
            host_port = int(host_port)


        username = input("Enter Username: ")
        if not username:
            raise InvalidUserName
        
        #print("Enter Password:", end = " ")
        password = getpass.getpass()
        print('\n')
    
    except InvalidUserName:
        print("Please Enter a valid username:")
    
    except Exception as error:
        print("Error: ", error )

    

    
    else:
        try:

            server_connection = mysql.connector.connect(
                host = host_address,
                user = username,
                port = host_port,
                passwd = password
            )
        
        except Exception as error:
            if (error.errno == errorcode.ER_ACCESS_DENIED_ERROR):
                print("Invalid Username or Password --  ACCESS DENIED")
            else:
                print("Error: ", error)
            
            exit(0)
        
        print("connected to server")

        db_name = input("Enter Database name: ")
        if not db_name:
            print("Database name not provided")
            exit(0)


        try:
            query = f"CREATE DATABASE {db_name}"
            cursor = server_connection.cursor()
            cursor.execute(query)
            
        except Exception as error:
            print("Cannot Create DATAB " , error )
        else:
            print("Database Created!")
        

        server_connection.close()
            



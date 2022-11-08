import mysql.connector as conn
import logging as lg

lg.basicConfig(filename='create-table', level=lg.INFO)
  
try :
  lg.info("Trying to establish connection")
  my_db = conn.connect(host="localhost", database="db1", user="mahotpal1", passwd="Abc@12345", use_pure=True)
  print("Enter the table name!")
  table_name = input()
  query = "CREATE TABLE "+table_name+"(Studentid INT(10) AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(60), LastName VARCHAR(10), RegistrationDate Date, Class VARCHAR(20), SECTION VARCHAR(10));"
  cur = my_db.cursor()
  try :
    cur.execute(query)
  except Exception as E:
    print("Error creating Table")
    lg.error("Error creating Table. Please try again!")
    print(E)
  else:
    print("Created table successfully.")
except Exception as e :
  print(e)
  lg.error("Error creating table")
  print("Error in creating establishment")


#cur1.execute("select * from table1")
#cur1.fetchall() - > this will return all values in form of list of tuples.

import mysql.connector as conn

try :
  mydb = conn.connect(host="localhost", user="mahotpal1", passwd="Abc@12345", use_pure=True)
  print("Enter Database name!")
  db_name = input()
  query = "CREATE DATABASE "+db_name+";"
  print(query)
  cursor = mydb.cursor()
  try :
    e = cursor.execute(query)
  except:
    print("Error creating database")
  else:
    print("Database created successfully.")
except Exception as e:
  print(e)
  mydb.close()
  
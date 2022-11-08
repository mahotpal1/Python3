import mysql.connector as conn

try :
  mydb = conn.connect(host="localhost", user="mahotpal1", passwd="Abc@12345", use_pure=True)
  #Check if connection is established

  query = "SHOW DATABASES"

  cursor = mydb.cursor() #create a cursor to execute queries
  cursor.execute(query)
  print(cursor.fetchall())

except Exception as e:
  mydb.close()
  print(str(e))
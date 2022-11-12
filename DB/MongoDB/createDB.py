import pymongo

url = "mongodb://localhost:27017/"
db_name = "test01"
#Establish a connection with mongoDB
client = pymongo.MongoClient(url)

#Create a DB:
db = client[db_name]

#create a collection:
collection = db["My_collection1"]

#Insert multiple data:
list_of_records = [{'Company_Name': 'iVishal',
                    'product': 'Affordable AI',
                    'courseOffered': 'Machine Learning with Deployment'},
                    {'Company_Name': 'iHarsh',
                    'product': 'Full Stack WEb Developer',
                    'courseOffered': 'Full Stack Web Developer'},
                    {'Company_Name': 'iLakshya',
                    'product': 'FlaskWeb',
                    'courseOffered': 'Casandra'}
                    ]
rec = collection.insert_many(list_of_records)
#rec = collection.insert_one(insert_data)
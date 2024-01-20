from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://yaz:1234@cluster0.uspsoud.mongodb.net/"

def get_database():
   client = MongoClient(CONNECTION_STRING)
   return client['Schedule_Optimization']

def get_Collection():
    return dbname["ScheduleCollectionName"]

dbname = get_database()
collection_name = get_Collection()
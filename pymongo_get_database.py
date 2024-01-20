from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://yaz:1234@cluster0.uspsoud.mongodb.net/"

def get_database():
   client = MongoClient(CONNECTION_STRING)
 
   return client['Schedule_Optimization']
  
if __name__ == "__main__":     
   dbname = get_database()
   print(dbname.split)
from pymongo import MongoClient
import pandas as pd

CONNECTION_STRING = "mongodb+srv://yaz:1234@cluster0.uspsoud.mongodb.net/"
df = pd.read_csv("ScheduleInfo.csv")

def get_database():
   client = MongoClient(CONNECTION_STRING)
   return client['Schedule_Optimization']

def get_Collection():
    return dbname["ScheduleCollectionName"]

dbname = get_database()
collection_name = get_Collection()

def dataframe_to_list_of_dicts(df):
    result_list = []
    for index, row in df.iterrows():
        registration_time = row.iloc[0]
        time_processed = row.iloc[1]
        vehicle_type = row.iloc[2]
        
        result_dict = {
            'Datetime_Issued': registration_time,
            'Datetime_Requested': time_processed,
            'vehicle_type': vehicle_type
        }
        result_list.append(result_dict)
    
    return result_list

data = dataframe_to_list_of_dicts(df)
#print(data)

with MongoClient(CONNECTION_STRING, connect=False) as client:
    db = client.Schedule_Optimization
    tools = db.ScheduleCollectionName
    result = tools.insert_many(data)

if __name__ == "__main__":     
    dbname = get_database()
    documents = collection_name.find()
    print("Documents in the collection:")
    for doc in documents:
        print(doc)


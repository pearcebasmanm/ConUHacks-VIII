from pymongo import MongoClient
import pandas as pd

CONNECTION_STRING = "mongodb+srv://yaz:07022000@cluster0.uspsoud.mongodb.net/"
df = pd.read_csv("ScheduleInfo.csv")

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
    

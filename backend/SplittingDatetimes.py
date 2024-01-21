import pandas as pd
import numpy as np
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://yaz:1234@cluster0.uspsoud.mongodb.net/"

bays = {'compact': 1, 'medium': 1, 'full-size': 1, 'class 1 truck': 1, 'class 2 truck': 1}
GeneralBays = {'General1': 1, 'General2': 1, 'General3': 1, 'General4': 1, 'General5': 1} 
processing_times = {'compact': 30, 'medium': 30, 'full-size': 30, 'class 1 truck': 60, 'class 2 truck': 120}
revenues = {'compact': 150, 'medium': 150, 'full-size': 150, 'class 1 truck': 250, 'class 2 truck': 700}
Availabilities = {'compact': 420, 'medium': 420, 'full-size': 420, 'class 1 truck': 420, 'class 2 truck': 420, 'General': 420}
NumberofServicedCustomers = {'compact': 0, 'medium': 0, 'full-size': 0, 'class 1 truck': 0, 'class 2 truck': 0}
NumberofTurnedAwayCustomers = {'compact': 0, 'medium': 0, 'full-size': 0, 'class 1 truck': 0, 'class 2 truck': 0}

df = pd.read_csv("ScheduleInfo.csv", header=None, names=['Datetime_Issued', 'Datetime_Requested', 'vehicle_type'])

df['Datetime_Issued'] = pd.to_datetime(df['Datetime_Issued'])
df['Datetime_Requested'] = pd.to_datetime(df['Datetime_Requested'])

df['year_Issued'] = df['Datetime_Issued'].dt.year
df['month_Issued'] = df['Datetime_Issued'].dt.month
df['day_Issued'] = df['Datetime_Issued'].dt.day
df['hour_Issued'] = df['Datetime_Issued'].dt.hour
df['minute_Issued'] = df['Datetime_Issued'].dt.minute

df['year_Requested'] = df['Datetime_Requested'].dt.year
df['month_Requested'] = df['Datetime_Requested'].dt.month
df['day_Requested'] = df['Datetime_Requested'].dt.day
df['hour_Requested'] = df['Datetime_Requested'].dt.hour
df['minute_Requested'] = df['Datetime_Requested'].dt.minute

df['minute_Sum'] = df['minute_Requested'] + 60 * df['hour_Requested']

df['is_WalkIn'] = np.where(
    (df['day_Requested'] == df['day_Issued']) & (df['month_Requested'] == df['month_Issued']), True, False
)

df = df.sort_values(['month_Requested', 'day_Requested', 'hour_Requested', 'minute_Requested'], ascending=[True, True, True, True])

df_condition_WalkIn = df[df['is_WalkIn'] == True]
df_condition_Scheduled = df[df['is_WalkIn'] == False]
    
total_revenue = 0
total_lost_revenue = 0

for index, row in df_condition_WalkIn.iterrows():
    vehicle_type = row[2]
    processing_time = processing_times[vehicle_type]
    revenue = revenues[vehicle_type]
    
    if row[13] + processing_time > 1140 or row[13] < 420:
        total_lost_revenue += revenue 
        NumberofTurnedAwayCustomers[vehicle_type] += 1
        continue 
        
    if row[13] >= Availabilities[vehicle_type]: 
        if  bays[vehicle_type] == 0:
            bays[vehicle_type] += 1
    
    if bays[vehicle_type] > 0:
        bays[vehicle_type] = 0
        total_revenue += revenues[vehicle_type]
        Availabilities[vehicle_type] += processing_time
        NumberofServicedCustomers[vehicle_type] += 1
        
    else:
        total_lost_revenue += revenue
        NumberofTurnedAwayCustomers[vehicle_type] += 1
        continue 

for index, row in df_condition_Scheduled.iterrows():
    
    vehicle_type = row[2]
    processing_time = processing_times[vehicle_type]
    revenue = revenues[vehicle_type]
    
    if row[13] + processing_time > 1140 or row[13] < 420:
        total_lost_revenue += revenue
        NumberofTurnedAwayCustomers[vehicle_type] += 1
        continue
    
    if row[13] >= Availabilities[vehicle_type]:
        if GeneralBays['General1'] == 0: GeneralBays['General1'] = 1
        elif GeneralBays['General2'] == 0: GeneralBays['General2'] = 1
        elif GeneralBays['General3'] == 0: GeneralBays['General3'] = 1
        elif GeneralBays['General4'] == 0: GeneralBays['General4'] = 1
        elif GeneralBays['General5'] == 0: GeneralBays['General5'] = 1
        else: continue

    if GeneralBays['General1'] == 1:
        GeneralBays['General1'] = 0
        total_revenue += revenue
        Availabilities[vehicle_type] += processing_time
        NumberofServicedCustomers[vehicle_type] += 1
    elif GeneralBays['General2'] == 1: 
        GeneralBays['General2'] = 0
        total_revenue += revenue
        Availabilities[vehicle_type] += processing_time
        NumberofServicedCustomers[vehicle_type] += 1
    elif GeneralBays['General3'] == 1: 
        GeneralBays['General3'] = 0
        total_revenue += revenue
        Availabilities[vehicle_type] += processing_time
        NumberofServicedCustomers[vehicle_type] += 1
    elif GeneralBays['General4'] == 1: 
        GeneralBays['General4'] = 0
        total_revenue += revenue
        Availabilities[vehicle_type] += processing_time
        NumberofServicedCustomers[vehicle_type] += 1
    elif GeneralBays['General5'] == 1:
        GeneralBays['General5'] = 0
        total_revenue += revenue
        Availabilities[vehicle_type] += processing_time
        NumberofServicedCustomers[vehicle_type] += 1
    else:
        total_lost_revenue += revenue
        NumberofTurnedAwayCustomers[vehicle_type] += 1
        continue 

'''print(total_revenue)
print(total_lost_revenue)

print(NumberofServicedCustomers)
print(NumberofTurnedAwayCustomers)'''


def dataframe_to_list_of_dicts(df):
    result_list = []
    for index, row in df.iterrows():
        registration_time =  row.iloc[0]
        time_processed    =  row.iloc[1]
        vehicle_type      =  row.iloc[2]
        year_Issued       =  row.iloc[3]
        month_Issued      =  row.iloc[4]
        day_Issued        =  row.iloc[5]
        hour_Issued       =  row.iloc[6]
        minute_Issued     =  row.iloc[7]
        year_Requested    =  row.iloc[8]
        month_Requested   =  row.iloc[9]
        day_Requested     =  row.iloc[10]
        hour_Requested    =  row.iloc[11]
        minute_Requested  =  row.iloc[12]
        minute_Sum        =  row.iloc[13]
        is_WalkIn         =  row.iloc[14]
        
        result_dict = {
            'Datetime_Issued'    : registration_time,
            'Datetime_Requested' : time_processed,
            'vehicle_type'       : vehicle_type,
            'year_Issued'        : year_Issued,
            'month_Issued'       : month_Issued,
            'day_Issued'         : day_Issued,
            'hour_Issued'        : hour_Issued,
            'minute_Issued'      : minute_Issued,
            'year_Requested'     : year_Requested,
            'month_Requested'    : month_Requested,
            'day_Requested'      : day_Requested,
            'hour_Requested'     : hour_Requested,
            'minute_Requested'   : minute_Requested,
            'minute_Sum'         : minute_Sum,
            'is_WalkIn'          : is_WalkIn
        }
        
        result_list.append(result_dict)
    
    return result_list

data = dataframe_to_list_of_dicts(df)

with MongoClient(CONNECTION_STRING, connect=False) as client:
    db = client.Schedule_Optimization
    tools = db.ScheduleCollectionName
    result = tools.insert_many(data)
    

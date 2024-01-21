import pandas as pd
import numpy as np


bays = {'Compact': 1, 'Medium': 1, 'FullSize': 1, 'Truck1': 1, 'Truck2': 1, 'General': 5}
processing_times = {'Compact': 30, 'Medium': 30, 'FullSize': 30, 'Truck1': 60, 'Truck2': 120}
revenues = {'Compact': 150, 'Medium': 150, 'FullSize': 150, 'Truck1': 250, 'Truck2': 750}
Availabilities = {'Compact': 420, 'Medium': 420, 'FullSize': 420, 'Truck1': 420, 'Truck2': 420, 'General': 420}

df = pd.read_csv("ScheduleInfo.csv", header=None, names=['Datetime_Issued', 'Datetime_Requested', 'vehicle_type'])
#print(df)

df['Datetime_Issued'] = pd.to_datetime(df['Datetime_Issued'])

df['year_Issued'] = df['Datetime_Issued'].dt.year
df['month_Issued'] = df['Datetime_Issued'].dt.month
df['day_Issued'] = df['Datetime_Issued'].dt.day
df['hour_Issued'] = df['Datetime_Issued'].dt.hour
df['minute_Issued'] = df['Datetime_Issued'].dt.minute

df['Datetime_Requested'] = pd.to_datetime(df['Datetime_Requested'])

df['year_Requested'] = df['Datetime_Requested'].dt.year
df['month_Requested'] = df['Datetime_Requested'].dt.month
df['day_Requested'] = df['Datetime_Requested'].dt.day
df['hour_Requested'] = df['Datetime_Requested'].dt.hour
df['minute_Requested'] = df['Datetime_Requested'].dt.minute

df['minute_Sum'] = df['minute_Requested'] + 60 * df['hour_Requested']

df['is_WalkIn'] = np.where(
    (df['day_Requested'] == df['day_Issued']) & (df['month_Requested'] == df['month_Issued']),
    True,
    False
)

df = df.sort_values(['month_Requested', 'day_Requested', 'hour_Requested', 'minute_Requested'], ascending=[True, True, True, True])
total_revenue = 0
for index, row in df.iterrows():
    
    car_type = row['CarType']
    processing_time = processing_times[car_type]
    revenue = revenues[car_type]
    priority = row['Priority']
    
    if df["minuteSum"] + processing_time > 1140 or df["minuteSum"] < 420: continue 
    
    #if bays[car_type] == 0 or bays['General'] == 0:
    
    if df["minute_Sum"] >= Availabilities[car_type]:
        if bays[car_type] < 1:
            bays['General'] += 1
        else:
            bays[car_type] += 1
        continue

    if bays[car_type] > 0:
        bays[car_type] = 0
        total_revenue += revenue
        Availabilities[car_type] += processing_time
        
    elif bays['General'] > 0:
        bays['General'] -= 1
        total_revenue += revenue
        temp = Availabilities['General']
        Availabilities['General'] += processing_time
        Availabilities['General'] = min(temp, Availabilities['General'])
    else:
        total_revenue -= revenue
        continue 

print(df)


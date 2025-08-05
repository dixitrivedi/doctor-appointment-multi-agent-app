import pandas as pd
from datetime import datetime

def convert_datetime_format(dt_str):
        dt = datetime.strptime(dt_str, "%d-%m-%Y %H:%M")
        return dt.strftime("%d-%m-%Y %#H:%M")

df = pd.read_csv("data/availability.csv")

print(df.shape)

# print(df[df['doctor_name']=="john doe" and df['date_slot']==])

print(df[df['date_slot']==convert_datetime_format("06-08-2024 08:00")])
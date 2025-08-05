import pandas as pd
from typing import Literal
from datetime import datetime
from langchain_core.tools import tool
from app.schemas.models import *

@tool
def set_appointment(desired_date: DateTimeModel, id_number: IdentificationNumberModel, doctor_name: Literal['kevin anderson','robert martinez','susan davis','daniel miller','sarah wilson','michael green','lisa brown','jane smith','emily johnson','john doe']):
    """
    Set appointment or slot with the doctor.
    The parameters MUST be mentioned by the user in the query.
    """
    df = df = pd.read_csv(r"data/availability.csv")
 
    def convert_datetime_format(dt_str):
        dt = datetime.strptime(dt_str, "%d-%m-%Y %H:%M")
        return dt.strftime("%d-%m-%Y %#H:%M")
    
    case = df[(df['date_slot'] == convert_datetime_format(desired_date.date))&(df['doctor_name'] == doctor_name)&(df['is_available'] == True)]


    if len(case) == 0:
        print("In if")
        return "No available appointments for that particular case"
    else:
        print("In else")
        df.loc[(df['date_slot'] == convert_datetime_format(desired_date.date))&(df['doctor_name'] == doctor_name) & (df['is_available'] == True), ['is_available','patient_to_attend']] = [False, id_number.id]
        df.to_csv(f'data/availability.csv', index = False)
        return "Successfully done"
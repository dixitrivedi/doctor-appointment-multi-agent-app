import pandas as pd
from typing import Literal
from langchain_core.tools import tool
from app.schemas.models import *

@tool
def check_availability_by_specialization(desired_date: DateModel, specialization: Literal["general_dentist", "cosmetic_dentist", "prosthodontist", "pediatric_dentist","emergency_dentist","oral_surgeon","orthodontist"]):
    """
    Checking the database if we have availability for the specific specialization.
    The parameters should be mentioned by the user in the query
    """
    df = df = pd.read_csv(r"data/availability.csv")
    df['date_slot_time'] = df['date_slot'].apply(lambda input: input.split(' ')[-1])
    rows = df[(df['date_slot'].apply(lambda input: input.split(' ')[0]) == desired_date.date) & (df['specialization'] == specialization) & (df['is_available'] == True)].groupby(['specialization', 'doctor_name'])['date_slot_time'].apply(list).reset_index(name='available_slots')

    if len(rows) == 0:
        output = "No availability in the entire day"
    else:
        def convert_to_am_pm(time_str):
            time_str = str(time_str)
            hours, minutes = map(int, time_str.split(":"))
            period = "AM" if hours < 12 else "PM"
            hours = hours % 12 or 12
            return f"{hours}:{minutes:02d} {period}"
        
        output = f'This availability for {desired_date.date}\n'
        for row in rows.values:
            output += row[1] + ". Available slots: \n" + ', \n'.join([convert_to_am_pm(value)for value in row[2]])+'\n'

    return output
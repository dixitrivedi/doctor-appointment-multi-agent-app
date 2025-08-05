import pandas as pd
from typing import Literal
from langchain_core.tools import tool
from app.schemas.models import *
from app.toolkit.cancel_appointment import cancel_appointment
from app.toolkit.set_appointment import set_appointment

@tool
def reschedule_appointment(old_date: DateTimeModel, new_date: DateTimeModel, id_number: IdentificationNumberModel, doctor_name: Literal['kevin anderson','robert martinez','susan davis','daniel miller','sarah wilson','michael green','lisa brown','jane smith','emily johnson','john doe']):
    """
    Rescheduling an appointment.
    The parameters MUST be mentioned by the user in the query.
    """
    df = df = pd.read_csv(r"data/availability.csv")
    available_for_desired_date = df[(df['date_slot'] == new_date.date)&(df['is_available'] == True)&(df['doctor_name'] == doctor_name)]
    if len(available_for_desired_date) == 0:
        return "Not available slots in the desired period"
    else:
        cancel_appointment.invoke({'date':old_date, 'id_number':id_number, 'doctor_name':doctor_name})
        set_appointment.invoke({'desired_date':new_date, 'id_number': id_number, 'doctor_name': doctor_name})
        return "Successfully rescheduled for the desired time"

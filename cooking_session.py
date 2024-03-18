import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid

def cooking_session_table(num_rows):
    #generate random data
    grams_used = np.random.randint(0, 13000, size=num_rows)
    cumulative_mass = np.cumsum(grams_used)
    start_times = datetime.now() - timedelta(days=np.random.randint(0, 50)) 
    start_time_unix_format = start_times.timestamp()  

    data=pd.DataFrame({'Customer_id':[str(uuid.uuid4().int)[:7] for _ in range(num_rows)],
                       'Meter_id':["KE0"+str(uuid.uuid4().int)[:7] for _ in range(num_rows)],
                       'Start_time':[start_time_unix_format for _ in range(num_rows)],
                       'Grams_used':grams_used,
                       'Cumulative_mass':cumulative_mass,
                       'Received_on':[datetime.now() - timedelta(days=np.random.randint(0, 50)) for _ in range(num_rows)]
                
                    #    'Validity':[]

                       })

     #create a unique id
    data['Uniq_id'] = data.apply(lambda row: generate_unique_ids(row), axis=1)
    
    #check validity of cooking session
    # data['Validity'] = data.apply(lambda row: is_session_valid(row), axis=1)
    data['Validity'] =  data.index % 2 == 0
    
    return data

   
def generate_unique_ids(row):
    return(row['Customer_id'] + row['Meter_id'] + str(int(row['Start_time'])))

def is_session_valid(row):
    #convert timestamp into datetime
    # received_on_datetime = datetime.fromtimestamp(row['Received_on'])
    start_time_datetime = datetime.fromtimestamp(row['Start_time'])
    
    return(row['Received_on'] - start_time_datetime).days <=3


def save_into_excel(data, filename):
    #convert DataFrame into excel
    data.to_excel(filename, index=False)

   
save_into_excel(cooking_session_table(110),"Generated cooking sessions data.xlsx")








    



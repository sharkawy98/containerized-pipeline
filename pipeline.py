import pandas as pd
from subprocess import call
from sqlalchemy import create_engine


def generate_sensors_data():
    '''Runs a bash script to produce sensors data'''
    call('./generate_sensors_data.sh')

def extract_sensors_data(filename):    
    return pd.read_csv(filename)
    
def transform_sensors_data(sensors_df):
    sensors_df['timestamp'] = pd.to_datetime(sensors_df['timestamp'])
    sensors_df = sensors_df.sort_values(by=['timestamp', 'sensor'], ignore_index=True)
    return sensors_df

def load_to_postgres(sensors_df):
    engine = create_engine('postgresql://root:root@pg-database:5432/sensors')
    try:
        sensors_df.to_sql('data', con=engine, if_exists='replace', index_label='id')
    except Exception as e:
        print('Error occured:', e)
    return 'Data loaded into PostgreSQL database successfully.'


if __name__ == "__main__":
    generate_sensors_data()
    sensors_df = extract_sensors_data('sensors_data.csv')
    sensors_df = transform_sensors_data(sensors_df)
    msg = load_to_postgres(sensors_df)
    print(msg)

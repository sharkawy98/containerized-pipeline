import pandas as pd
from subprocess import call


def generate_sensors_data():
    '''Runs a bash script to produce sensors data'''
    call('./generate_sensors_data.sh')

def extract_sensors_data(filename):    
    return pd.read_csv(filename)
    
def transform_sensors_data(sensors_df):
    sensors_df['timestamp'] = pd.to_datetime(sensors_df['timestamp'])
    sensors_df = sensors_df.sort_values(by=['timestamp', 'sensor'], ignore_index=True)
    return sensors_df


if __name__ == "__main__":
    generate_sensors_data()
    sensors_df = extract_sensors_data('sensors_data.csv')
    sensors_df = transform_sensors_data(sensors_df)
    print(sensors_df.head(8))

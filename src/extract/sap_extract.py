from pyrfc import Connection
import pandas as pd
import json

def sap_connection():
    with open('config/sap_config.json') as f:
        sap_config = json.load(f)
    return Connection(**sap_config)

def extract_data(table_name):
    conn = sap_connection()
    result = conn.call('RFC_READ_TABLE', QUERY_TABLE=table_name)
    columns = [field['FIELDNAME'] for field in result['FIELDS']]
    data = [list(row['WA'].split('|')) for row in result['DATA']]
    df = pd.DataFrame(data, columns=columns)
    return df

# Example usage
if __name__ == "__main__":
    df = extract_data('MATERIALS')
    print(df.head())

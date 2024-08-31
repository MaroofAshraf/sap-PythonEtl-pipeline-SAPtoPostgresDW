from sqlalchemy import create_engine
import pandas as pd

def load_to_postgres(df, table_name):
    engine = create_engine('postgresql://user:password@localhost/sap_data')
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Example usage
if __name__ == "__main__":
    df = pd.read_csv('data/transformed_materials.csv')
    load_to_postgres(df, 'materials')

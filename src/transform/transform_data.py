import pandas as pd

def transform_data(df):
    # Apply necessary transformations, e.g., data type conversions, aggregations, etc.
    df['MATERIAL'] = df['MATERIAL'].astype(str)
    df['PRICE'] = pd.to_numeric(df['PRICE'], errors='coerce')
    return df

# Example usage
if __name__ == "__main__":
    df = pd.read_csv('data/materials.csv')
    transformed_df = transform_data(df)
    print(transformed_df.head())

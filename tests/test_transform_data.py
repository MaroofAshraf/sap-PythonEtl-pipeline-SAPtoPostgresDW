import unittest
import pandas as pd
from src.transform.transform_data import transform_data

class TestTransformData(unittest.TestCase):

    def test_transform_data(self):
        # Create a mock DataFrame to test the transformation
        data = {'MATERIAL': ['001', '002'], 'PRICE': ['100', '200']}
        df = pd.DataFrame(data)
        transformed_df = transform_data(df)
        
        # Check if the transformations were applied correctly
        self.assertTrue(pd.api.types.is_numeric_dtype(transformed_df['PRICE']))
        self.assertEqual(transformed_df['MATERIAL'].dtype, 'object')

if __name__ == '__main__':
    unittest.main()

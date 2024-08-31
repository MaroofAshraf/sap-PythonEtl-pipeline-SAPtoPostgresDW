import unittest
import pandas as pd
from sqlalchemy import create_engine
from src.load.load_to_postgres import load_to_postgres

class TestLoadToPostgres(unittest.TestCase):

    def setUp(self):
        # Set up a test database
        self.engine = create_engine('postgresql://user:password@localhost/sap_data_test')
        self.connection = self.engine.connect()
        self.connection.execute("CREATE TABLE IF NOT EXISTS test_table (MATERIAL TEXT, PRICE NUMERIC)")

    def tearDown(self):
        # Clean up after each test
        self.connection.execute("DROP TABLE IF EXISTS test_table")
        self.connection.close()

    def test_load_to_postgres(self):
        # Create a mock DataFrame to test loading
        data = {'MATERIAL': ['001', '002'], 'PRICE': [100, 200]}
        df = pd.DataFrame(data)
        
        # Load the DataFrame into the test PostgreSQL table
        load_to_postgres(df, 'test_table')
        
        # Check if the data was loaded correctly
        result = self.connection.execute("SELECT * FROM test_table").fetchall()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['MATERIAL'], '001')
        self.assertEqual(result[0]['PRICE'], 100)

if __name__ == '__main__':
    unittest.main()

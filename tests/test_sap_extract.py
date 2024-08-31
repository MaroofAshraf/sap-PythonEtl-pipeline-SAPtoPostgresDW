import unittest
from src.extract.sap_extract import extract_data

class TestSapExtract(unittest.TestCase):

    def test_extract_data(self):
        # Test extracting data from a specific SAP table
        df = extract_data('MATERIALS')
        self.assertIsNotNone(df)
        self.assertTrue(len(df) > 0)
        self.assertIn('MATERIAL', df.columns)

if __name__ == '__main__':
    unittest.main()

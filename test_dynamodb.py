import unittest
from your_module.dynamodb_utils import load_data_from_dynamodb

class TestDynamoDBLoading(unittest.TestCase):
    def test_load_data(self):
        df = load_data_from_dynamodb('YOUR_TABLE_NAME')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertNotEqual(df.shape[0], 0)  # Ensures data is loaded

if __name__ == '__main__':
    unittest.main()

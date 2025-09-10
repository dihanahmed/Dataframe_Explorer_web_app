import unittest
import pandas as pd
import sys
import os
from pandas.util.testing import assert_frame_equal

# Ensure the path to src is in the system path
if os.path.abspath(".") not in sys.path: 
    sys.path.append(os.path.abspath("."))
from src.text import TextColumn

class TestTextColumn(unittest.TestCase):
    def setUp(self):
        # Load test data for country codes
        self.test_data = pd.read_csv('https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv')

    def tearDown(self):
        # Clean up after each test
        del self.test_data
    
    def test_get_name(self):
        # Test retrieving column name
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = 'ISO3166-1-Alpha-3'
        result = text_col.get_name()
        
        self.assertEqual(result, expected_output)

    def test_get_unique(self):
        # Test unique value count in the column
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].nunique()
        result = text_col.get_unique()
        
        self.assertEqual(result, expected_output)
        
    def test_get_missing(self):
        # Test count of missing values in the column
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].isnull().sum()
        result = text_col.get_missing()
        
        self.assertEqual(result, expected_output)         
        
    def test_get_empty(self):
        # Test count of empty strings in the column
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = (df['ISO3166-1-Alpha-3'] == '').sum()
        result = text_col.get_empty()
        
        self.assertEqual(result, expected_output)

    def test_get_whitespace(self):
        # Test rows containing only whitespace characters
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].str.isspace().sum()
        result = text_col.get_whitespace()
        
        self.assertEqual(result, expected_output)

    def test_get_lowercase(self):
        # Test rows that are all lowercase
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].str.islower().sum()
        result = text_col.get_lowercase()
        
        self.assertEqual(result, expected_output)

    def test_get_uppercase(self):
        # Test rows with all uppercase letters
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].str.isupper().sum()
        result = text_col.get_uppercase()
        
        self.assertEqual(result, expected_output)

    def test_get_alphabet(self):
        # Test rows containing only alphabetic characters
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].str.isalpha().sum()
        result = text_col.get_alphabet()
        
        self.assertEqual(result, expected_output)
        
    def test_get_digit(self):
        # Test rows that contain only numeric characters
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].str.isdigit().sum()
        result = text_col.get_digit()
        
        self.assertEqual(result, expected_output)

    def test_get_mode(self):
        # Test mode (most common value) in the column
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        expected_output = df['ISO3166-1-Alpha-3'].mode().iloc[0]
        result = text_col.get_mode()
        
        self.assertEqual(result, expected_output)

    def test_get_frequent(self):
        # Test the DataFrame of top frequent values and their percentage
        df = pd.DataFrame(self.test_data)
        text_col = TextColumn(col_name='ISO3166-1-Alpha-3', serie=df['ISO3166-1-Alpha-3'])
        
        # Calculate expected frequent values manually for comparison
        value_counts = df['ISO3166-1-Alpha-3'].value_counts().head(20)
        expected_output = pd.DataFrame({
            'value': value_counts.index,
            'occurrence': value_counts.values,
            'percentage': value_counts.values / len(df['ISO3166-1-Alpha-3'])
        })

        result = text_col.get_frequent()
        
        # Compare expected and result data frames without index
        assert_frame_equal(result.reset_index(drop=True), expected_output.reset_index(drop=True))

if __name__ == '__main__':
    unittest.main()


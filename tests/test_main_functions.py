from intakeinformer import intakeinformer

'''
test the main functionalities provided by get_calories_for_food_query() and dri_benchmark() functions. Testing these functions can be a bit challenging because they involve user input and API calls. 
'''

import unittest
from unittest.mock import patch
from intakeinformer.main_functions import get_calories_for_food_query, dri_benchmark
import pandas as pd

class TestMainFunctions(unittest.TestCase):

    @patch('intakeinformer.main_functions._fetch_food_data')
    @patch('intakeinformer.main_functions.get_user_food_selection')
    def test_get_calories_for_food_query(self, mock_selection, mock_fetch):
        # Mock the _fetch_food_data function to return a predefined DataFrame
        mock_fetch.return_value = pd.DataFrame({'description': ['Apple', 'Banana'], 
                                                'foodNutrients': [{'foodNutrientId': 1008, 'value': 52},
                                                                  {'foodNutrientId': 1008, 'value': 89}]})

        # Mock the get_user_food_selection function to return a predefined selection
        mock_selection.side_effect = lambda x: x.iloc[0]

        # Call the function
        result = get_calories_for_food_query("apple", "banana")

        # Define the expected result
        expected_result = {'Apple': 52.0, 'Banana': 89.0, 'total': 141.0}

        # Check if the result matches the expected result
        self.assertEqual(result, expected_result)

    @patch('intakeinformer.main_functions._fetch_food_data')
    @patch('intakeinformer.main_functions.get_user_food_selection')
    @patch('intakeinformer.main_functions.get_user_life_stage')
    def test_dri_benchmark(self, mock_life_stage, mock_selection, mock_fetch):
        # Similar to the above, mock the dependent functions
        # And then call dri_benchmark with the mock data
        # Check if the function performs as expected
        pass  # Implementation will depend on how dri_benchmark is structured

if __name__ == '__main__':
    unittest.main()

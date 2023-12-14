import pandas as pd
import pytest
from unittest.mock import patch
from intakeinformer.data_fetching import get_user_food_selection  

# Sample data to mock a DataFrame returned by _fetch_food_data
sample_data = {
    'description': ['Apple Variety 1', 'Apple Variety 2', 'Apple Variety 3'],
    'brandOwner': ['Brand A', 'Brand B', 'Brand C'],
    'servingSize': [100, 150, 120],
}

@pytest.mark.parametrize("user_input, expected_index", [
    ("1", 0),  # User selects the first item
    ("2", 1),  # User selects the second item
    ("3", 2),  # User selects the third item
    ("0", None),  # Invalid selection (out of range)
    ("invalid", None),  # Non-integer input
])
def test_get_user_food_selection(user_input, expected_index):
    food_df = pd.DataFrame(sample_data)
    with patch('builtins.input', return_value=user_input):
        selected_food = get_user_food_selection(food_df)

    if expected_index is None:
        assert selected_food is None, "Expected no selection"
    else:
        assert selected_food.equals(food_df.iloc[expected_index]), f"Expected selection at index {expected_index}"

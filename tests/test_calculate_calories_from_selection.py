import pandas as pd
from intakeinformer.data_processing import calculate_calories_from_selection

def test_calculate_calories_from_selection():
    # Mock data for selected_items
    selected_banana = {
        'description': 'Banana',
        'foodNutrients': [
            {'nutrientId': 1008, 'value': 89},
            {'nutrientId': 1005, 'value': 22.84},
            {'nutrientId': 1004, 'value': 0.33},
            {'nutrientId': 1003, 'value': 1.09}
        ],
        'servingSize': 100
    }

    selected_apple = {
        'description': 'Apple',
        'foodNutrients': [
            {'nutrientId': 1008, 'value': 52},
            {'nutrientId': 1005, 'value': 13.81},
            {'nutrientId': 1004, 'value': 0.17},
            {'nutrientId': 1003, 'value': 0.26}
        ],
        'servingSize': 100
    }

    selected_orange = {
        'description': 'Orange',
        'foodNutrients': [
            {'nutrientId': 1008, 'value': 47},
            {'nutrientId': 1005, 'value': 11.75},
            {'nutrientId': 1004, 'value': 0.12},
            {'nutrientId': 1003, 'value': 0.94}
        ],
        'servingSize': 100
    }

    # Convert mock data to DataFrame rows
    selected_items = [pd.Series(selected_banana), pd.Series(selected_apple), pd.Series(selected_orange)]

    # Execute function
    result = calculate_calories_from_selection(selected_items)

    # Assert
    assert result == {'Banana': 89.0, 'Apple': 52.0, 'Orange': 47.0, 'total': 188.0}, "Calorie calculation did not match expected values"

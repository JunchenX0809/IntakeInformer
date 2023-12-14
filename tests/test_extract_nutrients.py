import pytest
from intakeinformer.data_processing import extract_nutrients

def test_extract_nutrients():
    # Mock input for food_nutrients
    mock_nutrients = [
        {'nutrientId': 1004, 'nutrientName': 'Total lipid (fat)', 'value': 0.2},
        {'nutrientId': 1003, 'nutrientName': 'Protein', 'value': 1.1},
        {'nutrientId': 1005, 'nutrientName': 'Carbohydrate, by difference', 'value': 14.3},
        {'nutrientId': 1079, 'nutrientName': 'Fiber, total dietary', 'value': 2.4},
        {'nutrientId': 1087, 'nutrientName': 'Calcium, Ca', 'value': 5},
        {'nutrientId': 1089, 'nutrientName': 'Iron, Fe', 'value': 0.36},
        {'nutrientId': 1092, 'nutrientName': 'Potassium, K', 'value': 107},
        {'nutrientId': 1093, 'nutrientName': 'Sodium, Na', 'value': 1},
        {'nutrientId': 1104, 'nutrientName': 'Vitamin A, IU', 'value': 54},
        {'nutrientId': 1162, 'nutrientName': 'Vitamin C, total ascorbic acid', 'value': 6.2},
        {'nutrientId': 1114, 'nutrientName': 'Vitamin D', 'value': 0},
        {'nutrientId': 1175, 'nutrientName': 'Vitamin B-12', 'value': 0.00}
    ]

    # Expected output
    expected_output = {
        'Carbohydrate(g/d)': 14.3,
        'Total Fiber(g/d)': 2.4,
        'Fat(g/d)': 0.2,
        'Proteinb(g/d)': 1.1,
        'Calcium (mg/d)': 5,
        'Iron (mg/d)': 0.36,
        'Potassium (mg/d)': 107,
        'Sodium (mg/d)': 1,
        'Vitamin A(μg/d)a': 54,
        'Vitamin C(mg/d)': 6.2,
        'Vitamin D(μg/d)b,c': 0,
        'Vitamin B12(μg/d)': 0.00
    }

    # Run the function with the mock data
    output = extract_nutrients(mock_nutrients)

    # Check if the output matches the expected output
    assert output == expected_output, f"Expected {expected_output}, but got {output}"

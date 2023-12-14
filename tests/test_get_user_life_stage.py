import pytest
from unittest.mock import patch
from intakeinformer.data_fetching import get_user_life_stage

@pytest.mark.parametrize("inputs, expected", [
    (["1", "1"], ('Infants', '0–6 mo')),
    (["1", "2"], ('Infants', '6–12 mo')),
    (["2", "1"], ('Children', '1–3 y')),
    (["3", "3"], ('Males', '19–30 y')),
    (["3", "4"], ('Males', '31–50 y')),
    (["4", "2"], ('Females', '14–18 y')),
    (["4", "3"], ('Females', '19–30 y'))
])
def test_get_user_life_stage(inputs, expected):
    with patch('builtins.input', side_effect=inputs):
        life_stage_info = get_user_life_stage()
    assert life_stage_info == expected, f"Expected {expected}, got {life_stage_info}"

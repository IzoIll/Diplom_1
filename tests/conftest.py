import pytest
from unittest.mock import Mock

@pytest.fixture()
def bun():
    bun = Mock()
    bun.get_name.return_value = "Bulochka"
    bun.get_price.return_value = 5.0
    return bun

@pytest.fixture()
def ingredient_sauce():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "Mayonez"
    sauce.get_price.return_value = 10.0
    return sauce

@pytest.fixture()
def ingredient_fill():
    fill = Mock()
    fill.get_type.return_value = "FILLING"
    fill.get_name.return_value = "Kotletka"
    fill.get_price.return_value = 30.0
    return fill

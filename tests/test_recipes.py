import pytest
from recipes import (
    calculate_portion_factor,
    adjust_ingredient_amount,
    scale_recipe,
    calculate_calories_per_serving,
)

# 1. Використання @pytest.mark.parametrize та pytest.approx
@pytest.mark.parametrize(
    "orig, target, expected",
    [
        (2, 4, 2.0),
        (4, 2, 0.5),
        (3, 5, 1.6666666666666667),
    ],
)
def test_calculate_portion_factor_parametrize(orig, target, expected):
    result = calculate_portion_factor(orig, target)
    assert result == pytest.approx(expected)


# 2. Перевірка розрахунку одного інгредієнта для звичайних додатних чисел
@pytest.mark.parametrize(
    "amount, factor, expected",
    [
        (100.0, 2.0, 200.0),
        (250.5, 0.5, 125.25),
    ],
)
def test_adjust_ingredient_amount(amount, factor, expected):
    assert adjust_ingredient_amount(amount, factor) == pytest.approx(expected)


# 3. Перевірка маштабування всього рецепта
def test_scale_recipe():
    pancakes = {" борошно": 200.0, "молоко": 300.0, "яйця": 2.0}
    scaled = scale_recipe(pancakes, original_servings=2, target_servings=4)
    
    assert scaled[" борошно"] == pytest.approx(400.0)
    assert scaled["молоко"] == pytest.approx(600.0)
    assert scaled["яйця"] == pytest.approx(4.0)


def test_calculate_calories_per_serving():
    assert calculate_calories_per_serving(1200.0, 4) == pytest.approx(300.0)


# 4. Використання pytest.raises(ValueError) для некоректних даних
@pytest.mark.parametrize(
    "orig, target",
    [
        (0, 4),
        (2, -1),
        (-2, 0),
    ],
)
def test_calculate_portion_factor_raises(orig, target):
    with pytest.raises(ValueError):
        calculate_portion_factor(orig, target)


def test_adjust_ingredient_amount_raises():
    with pytest.raises(ValueError):
        adjust_ingredient_amount(-50.0, 2.0)
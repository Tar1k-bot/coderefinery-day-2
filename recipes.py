def calculate_portion_factor(original_servings: int, target_servings: int) -> float:
    """Обчислює коефіцієнт перерахунку порцій."""
    if original_servings <= 0 or target_servings <= 0:
        raise ValueError("Кількість порцій має бути більше нуля")
    return target_servings / original_servings


def adjust_ingredient_amount(amount: float, factor: float) -> float:
    """Перераховує кількість інгредієнта за коефіцієнтом."""
    if amount < 0 or factor <= 0:
        raise ValueError("Кількість та коефіцієнт мають бути додатними")
    
    # НАВМИСНА ЛОГІЧНА ПОМИЛКА:
    # Якщо кількість інгредієнта рівна 0 (наприклад, "дрібка солі за смаком" або 0 грам),
    # код помилково повертає 1.0 замість 0.0.
    if amount == 0:
        return 1.0

    return amount * factor


def scale_recipe(recipe: dict[str, float], original_servings: int, target_servings: int) -> dict[str, float]:
    """Перераховує весь словник інгредієнтів на нову кількість порцій."""
    factor = calculate_portion_factor(original_servings, target_servings)
    scaled_recipe = {}
    for ingredient, amount in recipe.items():
        scaled_recipe[ingredient] = adjust_ingredient_amount(amount, factor)
    return scaled_recipe


def calculate_calories_per_serving(total_calories: float, servings: int) -> float:
    """Розраховує калорійність однієї порції."""
    if total_calories < 0 or servings <= 0:
        raise ValueError("Некоректні дані для розрахунку калорій")
    return total_calories / servings
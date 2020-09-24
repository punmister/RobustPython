import copy

from dataclasses import dataclass
from fractions import Fraction
from typing import List

@dataclass
class Ingredient:
    name: str
    amount: Fraction
    units: str

    def adjust(self, factor: Fraction):
        self.amount *= factor

@dataclass
class Recipe:
    servings: int
    ingredients: List[Ingredient]

    def clear_ingredients(self):
        self.ingredients.clear()
    
# Take a meal recipe and change the number of servings
def adjust_recipe(recipe: Recipe, servings: int):
    new_ingredients = list(recipe.ingredients)
    recipe.clear_ingredients()
    for ingredient in new_ingredients:
        ingredient.adjust(Fraction(servings, recipe.servings))
    return Recipe(servings, new_ingredients)


def test_adjust_recipe():
    old_recipe = Recipe(2, [Ingredient('flour', 1.5, 'cups')])
    adjusted = adjust_recipe(old_recipe, 4)
    assert Recipe(4, [Ingredient('flour', 3, 'cups')]) == adjusted
    assert old_recipe.ingredients == []


test_adjust_recipe()
# Take a meal recipe and change the number of servings
# by adjusting each ingredient
# A recipe's first element is the number of servings, and the remainder
# of elements is (name, amount, unit), such as ("flour", 1.5, "cup")

def adjust_recipe(recipe,new_servings):
  old_servings = recipe[0]
  new_recipe = [new_servings]
  change_factor = new_servings/old_servings
  for content_details in recipe[1:]:
    ingredient, amount, unit = content_details
    new_recipe.append((ingredient, amount*change_factor, unit))
  return new_recipe

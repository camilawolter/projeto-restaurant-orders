import pandas
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.create_dishes(source_path)

    def create_dishes(self, source_path: str):
        dishes = set()
        dishes_df = pandas.read_csv(source_path)

        previous_dish = None
        dish = None

        for dish_name, price, ingredient, amount in dishes_df.itertuples(
            index=False
        ):

            if dish_name != previous_dish:
                if previous_dish is not None:
                    dishes.add(dish)
                previous_dish = dish_name
                dish = Dish(dish_name, float(price))

            dish.add_ingredient_dependency(Ingredient(ingredient), amount)

        dishes.add(dish)

        return dishes

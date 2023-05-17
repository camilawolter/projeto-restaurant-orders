import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import (Ingredient, Restriction)


# Req 2
def test_dish():
    with pytest.raises(ValueError):
        Dish("Torrada", -1)
    with pytest.raises(TypeError):
        Dish("Torrada", "15")

    torrada = Dish("Torrada", 12)
    macarrao = Dish("Macarrão", 40)

    torrada.add_ingredient_dependency(Ingredient("queijo mussarela"), 2)

    assert torrada.name == "Torrada"
    assert torrada.price == 12
    assert torrada.__repr__() == "Dish('Torrada', R$12.00)"
    assert torrada.__hash__() == hash(torrada)
    assert hash(torrada) != hash(macarrao)
    assert torrada.__eq__(macarrao) is False
    assert torrada.__eq__(torrada) is True
    assert torrada.recipe.get(Ingredient("queijo mussarela")) == 2
    assert torrada.get_ingredients() == {Ingredient("queijo mussarela")}
    assert torrada.get_restrictions() == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }

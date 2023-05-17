from src.models.ingredient import (Ingredient, Restriction)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ovo = Ingredient("ovo")
    camarao = Ingredient("camarão")

    assert camarao.restrictions == {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
    }
    assert camarao.name == "camarão"
    assert camarao.__hash__() == hash("camarão")
    assert hash(camarao != ovo)
    assert camarao.__repr__() == "Ingredient('camarão')"
    assert camarao.__eq__(ovo) is False
    assert camarao.__eq__(camarao) is True

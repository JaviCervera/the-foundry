import pytest

from src.model.resource import Resource


class Money(Resource):
    pass


class Gold(Resource):
    pass


def test_can_create_resource_from_int():
    assert int(Resource(0)) == 0


def test_can_add_resources_of_same_kind():
    res = Money(1) + Money(2)
    assert int(res) == 3
    assert type(res).__name__ == "Money"


def test_can_convert_resource_to_str():
    assert str(Resource(1)) == "Resource(1)"
    assert str(Money(10)) == "Money(10)"
    assert str(Gold(25)) == "Gold(25)"


def test_cannot_create_resource_with_non_int_amount():
    with pytest.raises(ValueError):
        Resource(1.5)


def test_cannot_create_resource_with_negative_amount():
    with pytest.raises(ValueError):
        Resource(-1)


def test_cannot_add_resources_of_different_type():
    with pytest.raises(ValueError):
        Money(1) + Gold(2)

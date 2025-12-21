import pytest

from src.model.metal import Metal, MetalError


def test_can_create_metal_from_int():
    assert int(Metal(0)) == 0


def test_can_add_metal_resources():
    assert Metal(1) + Metal(2) == Metal(3)


def test_can_convert_resource_to_str():
    assert str(Metal(10)) == "Metal(10)"


def test_cannot_create_metal_with_non_int_amount():
    with pytest.raises(MetalError) as exc:
        Metal(1.5)
    assert str(exc.value) == "Metal amount must be int, not float"


def test_cannot_create_metal_with_negative_amount():
    with pytest.raises(MetalError) as exc:
        Metal(-1)
    assert str(exc.value) == "Metal amount cannot be negative, got -1"


def test_cannot_add_other_type_to_metal():
    with pytest.raises(MetalError) as exc:
        Metal(1) + 2
    assert str(exc.value) == "Cannot add int to Metal"

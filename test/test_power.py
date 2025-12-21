import pytest

from src.model.power import Power, PowerError


def test_can_create_power_from_int():
    assert int(Power(1)) == 1


def test_can_compare_powers():
    assert Power(1) < Power(2)
    assert Power(2) > Power(1)
    assert Power(1) == Power(1)
    assert Power(1) != Power(2)


def test_can_covert_power_to_str():
    assert str(Power(5)) == "Power(5)"


def test_cannot_create_non_int_power():
    with pytest.raises(PowerError) as exc:
        Power(1.0)
    assert str(exc.value) == "Power must be int, not float"


def test_cannot_create_non_positive_power():
    with pytest.raises(PowerError) as exc:
        Power(0)
    assert str(exc.value) == "Power must be positive, got 0"

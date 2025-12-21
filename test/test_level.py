import pytest

from src.model.level import Level, LevelError


def test_can_create_level_from_int():
    assert int(Level(1)) == 1


def test_can_add_levels():
    assert Level(1) + Level(1) == Level(2)


def test_can_covert_level_to_str():
    assert str(Level(5)) == "Level(5)"


def test_cannot_create_non_int_level():
    with pytest.raises(LevelError) as exc:
        Level(None)
    assert str(exc.value) == "Level must be int, not NoneType"


def test_cannot_create_non_positive_level():
    with pytest.raises(LevelError) as exc:
        Level(0)
    assert str(exc.value) == "Level must be positive, got 0"


def test_cannot_add_int_to_level():
    with pytest.raises(LevelError) as exc:
        Level(1) + 1
    assert str(exc.value) == "Cannot add int to Level"

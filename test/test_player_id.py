import pytest

from src.model.player_id import PlayerId, PlayerIdError


def test_can_create_player_id_from_int():
    assert int(PlayerId(1)) == 1


def test_can_convert_player_id_to_str():
    assert str(PlayerId(1)) == "PlayerId(1)"


def test_cannot_create_non_int_player_id():
    with pytest.raises(PlayerIdError) as exc:
        PlayerId(1.5)
    assert str(exc.value) == "PlayerId must be int, not float"


def test_cannot_create_non_positive_player_id():
    with pytest.raises(PlayerIdError) as exc:
        PlayerId(0)
    assert str(exc.value) == "PlayerId must be positive, got 0"

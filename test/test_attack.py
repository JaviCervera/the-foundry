from src.action.attack import attack
from src.model.level import Level
from src.model.metal import Metal
from src.model.player import Player
from src.model.player_id import PlayerId


def test_attacker_wins_attack_if_has_more_power():
    attacker = Player(id=PlayerId(1), metal=Metal(0), mine_level=Level(2), military_level=Level(1))
    defendant = Player(id=PlayerId(2), metal=Metal(0), mine_level=Level(1), military_level=Level(1))
    assert attack(attacker, defendant).victory is True


def test_attacker_loses_attack_if_has_less_power():
    attacker = Player(id=PlayerId(1), metal=Metal(0), mine_level=Level(1), military_level=Level(1))
    defendant = Player(id=PlayerId(2), metal=Metal(0), mine_level=Level(2), military_level=Level(1))
    assert attack(attacker, defendant).victory is False


def test_if_attacker_earns_30_percent_of_enemy_metal_on_victory():
    attacker = Player(id=PlayerId(1), metal=Metal(10), mine_level=Level(2), military_level=Level(1))
    defendant = Player(
        id=PlayerId(2), metal=Metal(100), mine_level=Level(1), military_level=Level(1)
    )
    result = attack(attacker, defendant)
    assert result.attacker.metal == Metal(40)
    assert result.defendant.metal == Metal(70)


def test_attacker_loses_10_percent_of_metal_on_defeat():
    attacker = Player(
        id=PlayerId(1), metal=Metal(100), mine_level=Level(1), military_level=Level(1)
    )
    defendant = Player(
        id=PlayerId(2), metal=Metal(100), mine_level=Level(2), military_level=Level(1)
    )
    result = attack(attacker, defendant)
    assert result.attacker.metal == Metal(90)
    assert result.defendant.metal == Metal(100)

from src.model.level import Level
from src.model.metal import Metal
from src.model.player import Player
from src.model.player_id import PlayerId
from src.model.power import Power


def test_power_is_mine_level_plus_twice_military_level():
    player = Player(id=PlayerId(1), metal=Metal(0), mine_level=Level(3), military_level=Level(5))
    assert player.power == Power(13)

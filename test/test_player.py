from core.level import Level
from core.metal import Metal
from core.player import Player
from core.player_id import PlayerId
from core.power import Power


def test_power_is_mine_level_plus_twice_military_level():
    player = Player(id=PlayerId(1), metal=Metal(0), mine_level=Level(3), military_level=Level(5))
    assert player.power == Power(13)

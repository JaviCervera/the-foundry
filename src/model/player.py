from dataclasses import dataclass

from .level import Level
from .metal import Metal
from .player_id import PlayerId
from .power import Power
from .timestamp import Timestamp


@dataclass(frozen=True)
class Player:
    id: PlayerId
    metal: Metal
    mine_level: Level
    military_level: Level
    last_upgrade_time: Timestamp = Timestamp(0.0)

    @property
    def power(self) -> Power:
        return Power(int(self.mine_level) + 2 * int(self.military_level))

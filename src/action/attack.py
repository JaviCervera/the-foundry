from dataclasses import dataclass

from ..model.player import Player


@dataclass(frozen=True)
class AttackResult:
    victory: bool
    attacker: Player
    defendant: Player


def attack(attacker: Player, defendant: Player) -> AttackResult:
    if attacker.power > defendant.power:
        loot = defendant.metal * 0.3
        attacker = Player(
            attacker.id, attacker.metal + loot, attacker.mine_level, attacker.military_level
        )
        defendant = Player(
            defendant.id, defendant.metal - loot, defendant.mine_level, defendant.military_level
        )
        victory = True
    else:
        attacker = Player(
            attacker.id, attacker.metal * 0.9, attacker.mine_level, attacker.military_level
        )
        victory = False
    return AttackResult(victory, attacker, defendant)

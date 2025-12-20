# The Foundry

A simple MMO with a stateless server architectures.

Tech stack:

* Python 3.12
* Raylib 5.5

## 1. Core loop

1. Generate resources over time
2. Spend resources to upgrade a base
3. Use upgraded base to gain power
4. Combat with other players

## 2. Game elements

### Resources

* Metal
* Energy
* Credits?

Generated automatically every X seconds. Stored up to a cap.

### Base

* Each player has a single base
* Can increase level:
  * Increase resource production
  * Unlocks something new?
* Each base can have 2 buildings

### Buildings

* Mine (increases resource generation)
* Factory (increases military power)

## 3. Combat

* Each player has a unique stat: Power (`base_level` + `military_building_level`)

### Attack rule

```python
def attack(player, enemy):
    if player.power() > enemy.power():
        loot = enemy.metal * 0.3
        player.metal += loot
        enemy.metal -= loot
        return "Victory"
    else:
        player.metal *= 0.9
        return "Defeat"
```

TODO: Add randomness

## 4. Time mechanics

* Building upgrades takes time.
* Attacks require travel time.

Examples:

* Update mine: 5 minutes.
* Attack: Resolves in 60 seconds.

## 5. UI

* Top row: resources
* Main view: Base state.
* Bottom row: Upgrade mine. Upgrade military. Attack button (select target, confirm).

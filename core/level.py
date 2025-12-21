from dataclasses import dataclass


class LevelError(Exception):
    pass


@dataclass(frozen=True)
class Level:
    _level: int

    def __post_init__(self) -> None:
        if not isinstance(self._level, int):
            raise LevelError(f"Level must be int, not {type(self._level).__name__}")
        if self._level < 1:
            raise LevelError(f"Level must be positive, got {self._level}")

    def __add__(self, other: "Level") -> "Level":
        if not isinstance(other, Level):
            raise LevelError(f"Cannot add {type(other).__name__} to Level")
        return Level(self._level + other._level)

    def __int__(self) -> int:
        return self._level

    def __str__(self) -> str:
        return f"Level({self._level})"

from dataclasses import dataclass


class PowerError(Exception):
    pass


@dataclass(frozen=True)
class Power:
    _power: int

    def __post_init__(self) -> None:
        if not isinstance(self._power, int):
            raise PowerError(f"Power must be int, not {type(self._power).__name__}")
        if self._power < 1:
            raise PowerError(f"Power must be positive, got {self._power}")

    def __int__(self) -> int:
        return self._power

    def __str__(self) -> str:
        return f"Power({self._power})"

    def __lt__(self, other: "Power") -> bool:
        return self._power < other._power

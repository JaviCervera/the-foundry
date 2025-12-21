from dataclasses import dataclass


class MetalError(Exception):
    pass


@dataclass(frozen=True)
class Metal:
    _amount: int

    def __post_init__(self) -> None:
        if not isinstance(self._amount, int):
            raise MetalError(f"Metal amount must be int, not {type(self._amount).__name__}")
        if self._amount < 0:
            raise MetalError(f"Metal amount cannot be negative, got {self._amount}")

    def __add__(self, other: "Metal") -> "Metal":
        if not isinstance(other, Metal):
            raise MetalError(f"Cannot add {type(other).__name__} to Metal")
        return Metal(self._amount + other._amount)

    def __sub__(self, other: "Metal") -> "Metal":
        if not isinstance(other, Metal):
            raise MetalError(f"Cannot subtract {type(other).__name__} from Metal")
        return Metal(self._amount - other._amount)

    def __mul__(self, scalar: int | float) -> "Metal":
        return Metal(int(self._amount * scalar))

    def __int__(self) -> int:
        return self._amount

    def __str__(self) -> str:
        return f"Metal({self._amount})"

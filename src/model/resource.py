from dataclasses import dataclass


@dataclass(frozen=True)
class Resource:
    _amount: int

    def __post_init__(self) -> None:
        if not isinstance(self._amount, int):
            raise ValueError(f"Resource.amount must be int, not {type(self._amount).__name__}")
        if self._amount < 0:
            raise ValueError(f"Resource.amount cannot be negative, got {self._amount}")

    def __add__(self, other: "Resource") -> "Resource":
        if not isinstance(other, type(self)):
            raise ValueError(
                f"Can't add resources of types {type(self).__name__} and {type(other).__name__}"
            )
        return type(self)(self._amount + other._amount)

    def __int__(self) -> int:
        return self._amount

    def __str__(self) -> str:
        return f"{type(self).__name__}({self._amount})"

from dataclasses import dataclass
from datetime import datetime


class TimestampError(Exception):
    pass


@dataclass(frozen=True)
class Timestamp:
    _ts: float

    def __post_init__(self) -> None:
        if isinstance(self._ts, datetime):
            object.__setattr__(self, "_ts", self._ts.timestamp())
        elif not isinstance(self._ts, float):
            raise TimestampError(
                f"Timestamp must be initialized with float or datetime, got {type(self._ts).__name__}"
            )

    def __add__(self, other: "Timestamp") -> "Timestamp":
        if not isinstance(other, Timestamp):
            raise TimestampError(f"Cannot add {type(other).__name__} to Timestamp")
        return Timestamp(self._ts + other._ts)

    def __float__(self) -> float:
        return self._ts

    def __str__(self) -> str:
        return f"Timestamp({self._ts})"

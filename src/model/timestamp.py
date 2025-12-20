from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Timestamp:
    _ts: float

    def __post_init__(self) -> None:
        if isinstance(self._ts, datetime):
            object.__setattr__(self, "_ts", self._ts.timestamp())
        elif not isinstance(self._ts, float):
            raise ValueError(
                f"Timestamp must be initialized with float or datetime, got {type(self._ts).__name__}"
            )

    def __float__(self) -> float:
        return self._ts

    def __str__(self) -> str:
        return f"Timestamp({self._ts})"

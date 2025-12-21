from dataclasses import dataclass


class PlayerIdError(Exception):
    pass


@dataclass(frozen=True)
class PlayerId:
    _id: int

    def __post_init__(self) -> None:
        if not isinstance(self._id, int):
            raise PlayerIdError(f"PlayerId must be int, not {type(self._id).__name__}")
        if self._id < 1:
            raise PlayerIdError(f"PlayerId must be positive, got {self._id}")

    def __int__(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"PlayerId({self._id})"

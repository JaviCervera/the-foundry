from datetime import datetime

import pytest

from src.model.timestamp import Timestamp
from src.model.timestamp_error import TimestampError


def test_can_create_timestamp_from_float():
    assert float(Timestamp(12345.25)) == 12345.25


def test_can_create_timestamp_from_datetime():
    dt = datetime.now()
    assert float(Timestamp(dt)) == dt.timestamp()


def test_can_add_timestamps():
    assert Timestamp(100.0) + Timestamp(99.0) == Timestamp(199.0)


def test_can_convert_timestamp_to_str():
    assert str(Timestamp(1234.0)) == "Timestamp(1234.0)"


def test_cannot_create_timestamp_from_other_type():
    with pytest.raises(TimestampError) as exc:
        Timestamp(1234)
    assert str(exc.value) == "Timestamp must be initialized with float or datetime, got int"


def test_cannot_add_other_type_to_timestamp():
    with pytest.raises(TimestampError) as exc:
        Timestamp(0.0) + 5.0
    assert str(exc.value) == "Cannot add float to Timestamp"

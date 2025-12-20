from datetime import datetime

import pytest

from src.model.timestamp import Timestamp


def test_can_create_timestamp_from_float():
    ts = 12345.25
    assert float(Timestamp(ts)) == ts


def test_can_create_timestamp_from_datetime():
    dt = datetime.now()
    assert float(Timestamp(dt)) == dt.timestamp()


def test_can_convert_timestamp_to_str():
    assert str(Timestamp(1234.0)) == "Timestamp(1234.0)"


def test_cannot_create_timestamp_from_other_type():
    with pytest.raises(ValueError):
        Timestamp(1234)

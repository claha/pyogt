"""Tests for OGTDeparture class."""
from pyogt.ogtdeparture import OGTDeparture


def test_ogtdeparture_default_arguments():
    """Test default arguments."""
    departure = OGTDeparture()
    assert departure.get_name() == ''
    assert departure.get_date_time() == ''
    assert departure.get_towards() == ''
    assert departure.get_stop_point() == ''


def test_ogtdeparture_name():
    """Test name."""
    name = 'name'
    departure = OGTDeparture(name=name)
    assert departure.get_name() == name


def test_ogtdeparture_date_time():
    """Test date/time."""
    date_time = '2019-01-01T00:00:00'
    departure = OGTDeparture(date_time=date_time)
    assert departure.get_date_time() == date_time


def test_ogtdeparture_towards():
    """Test towards."""
    towards = 'towards'
    departure = OGTDeparture(towards=towards)
    assert departure.get_towards() == towards


def test_ogtdeparture_stop_poinnt():
    """Test stop point."""
    stop_point = 'stop_point'
    departure = OGTDeparture(stop_point=stop_point)
    assert departure.get_stop_point() == stop_point

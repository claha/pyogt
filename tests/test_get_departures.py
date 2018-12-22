"""Tests to get departures."""
import pyogt


def test_get_deparutres():
    """Test get departures."""
    departures = pyogt.get_departures('linkopings-resecentrum')
    for departure in departures:
        assert departure.get_name() is not None
        assert departure.get_date_time() is not None
        assert departure.get_towards() is not None
        assert departure.get_stop_point() is not None

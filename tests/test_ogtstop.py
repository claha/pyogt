"""Tests for OGTStop class."""
import pyogt


def test_ogtstop_default_arguments():
    """Test default arguments."""
    stop = pyogt.OGTStop()
    assert stop.get_name() == ''
    assert stop.get_id() == -1
    assert stop.get_pretty_name() == ''


def test_ogtstop_name():
    """Test name."""
    name = 'name'
    stop = pyogt.OGTStop(name=name)
    assert stop.get_name() == name


def test_ogtstop_id():
    """Test id."""
    id_ = 0
    stop = pyogt.OGTStop(id_=id_)
    assert stop.get_id() == id_


def test_ogtstop_pretty_name():
    """Test pretty name."""
    pretty_name = 'pretty_name'
    stop = pyogt.OGTStop(pretty_name=pretty_name)
    assert stop.get_pretty_name() == pretty_name

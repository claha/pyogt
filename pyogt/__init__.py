"""Init file for pyogt."""
from .ogtrest import OGTRest
from .ogtstop import OGTStop


def find_stop(name):
    """Find a stop by name."""
    stops = OGTRest.stops_find(query=name)

    for stop in stops:
        if stop.get_name() == name:
            return stop

    return OGTStop()

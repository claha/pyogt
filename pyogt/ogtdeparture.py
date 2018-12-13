"""Class to represent a departure from the OGT rest api."""


class OGTDeparture(object):
    """Class to store information about a departure."""

    def __init__(self, name, date_time, towards, stop_point):
        """Initialize an OGTDeparture."""
        self._name = name
        self._date_time = date_time
        self._towards = towards
        self._stop_point = stop_point

    def get_name(self):
        """Return the name of the departure."""
        return self._name

    def get_date_time(self):
        """Return the date/time of the departure."""
        return self._date_time

    def get_towards(self):
        """Return the towards of the departure."""
        return self._towards

    def get_stop_point(self):
        """Return the stop point of the departure."""
        return self._stop_point

    @staticmethod
    def from_json(data):
        """Create an OGTDeparture object from json-data."""
        name = None
        date_time = None
        towards = None
        stop_point = None

        if 'Ogt' in data:
            if 'OgtLineUrlSegment' in data['Ogt']:
                name = data['Ogt']['OgtLineUrlSegment']
            if 'PassingStops' in data['Ogt']:
                towards = data['Ogt']['PassingStops'][-1]
        if 'JourneyDateTime' in data:
            date_time = data['JourneyDateTime']
        if 'StopPointAliasFormatted' in data:
            stop_point = data['StopPointAliasFormatted']

        return OGTDeparture(name, date_time, towards, stop_point)

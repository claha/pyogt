"""OGTRest exposes the OGT rest api."""
import requests
from .ogtstop import OGTStop
from .ogtdeparture import OGTDeparture


class OGTRest(object):
    """Static class that exposes the OGT rest api."""

    URL_REST = 'https://rest.ostgotatrafiken.se/'
    METHOD_STOPS_FIND = 'stops/Find'
    METHOD_STOPS_INFOS = 'stops/Infos'
    METHOD_STOP_DEPARTURES = 'stopdepartures/departures'

    @staticmethod
    def get(method, params):
        """Perform a http get requests to the OGT rest api."""
        url = OGTRest.URL_REST + method
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def stops_find(query):
        """Find stops that matches the query."""
        # Define method and params
        method = OGTRest.METHOD_STOPS_FIND
        params = {
            'q': query,
            'pointType': 'stop',
        }

        # Send request
        stops = OGTRest.get(method, params)

        # Convert to list of OGTStop
        ogt_stops = []
        if stops is not None:
            for stop in stops:
                ogt_stops.append(OGTStop.from_json(stop))

        # Return stops
        return ogt_stops

    @staticmethod
    def stops_infos(ids):
        """Find stops that matches the ids."""
        # Define method and params
        method = OGTRest.METHOD_STOPS_INFOS
        if isinstance(ids, (list,)):
            ids = ','.join(map(str, ids))
        params = {
            'ids': ids,
        }

        # Send request
        stops = OGTRest.get(method, params)

        # Convert to list of OGTStop
        ogt_stops = []
        if stops is not None:
            for stop in stops:
                ogt_stops.append(OGTStop.from_json(stop))

        # Return stops
        return ogt_stops

    @staticmethod
    def stop_departures(stop_id, num_departures=20):
        """Find stop departures that matches the stop_id."""
        # Define method and params
        method = OGTRest.METHOD_STOP_DEPARTURES
        date = ''
        delay = 0
        lines = []
        traffic_types = []
        stop_points = []
        sort_order = 'DepartureTime'  # LineNumber
        params = {
            'stopAreaId': stop_id,
            'date': date,
            'delay': delay,
            'maxNumberOfResultPerColumn': num_departures,
            'columnsPerPageCount': 1,
            'pagesCount': 1,
            'lines': ','.join(lines),
            'trafficTypes': ','.join(traffic_types),
            'stopPoints': ','.join(stop_points),
            'sortOrder': sort_order,
            'useDaySeparator': False,
        }

        # Send request
        departures = OGTRest.get(method, params)['groups'][0]

        # Convert to list of OGTDeparture
        ogt_departures = []
        if departures is not None:
            for departure in departures:
                ogt_departures.append(
                    OGTDeparture.from_json(departure['Line']))

        # Return departures
        return ogt_departures

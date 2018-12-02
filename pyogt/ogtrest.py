"""OGTRest exposes the OGT rest api."""
import requests
from .ogtstop import OGTStop


class OGTRest(object):
    """Static class that exposes the OGT rest api."""

    URL_REST = 'https://rest.ostgotatrafiken.se/'
    METHOD_STOPS_FIND = 'stops/Find'

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

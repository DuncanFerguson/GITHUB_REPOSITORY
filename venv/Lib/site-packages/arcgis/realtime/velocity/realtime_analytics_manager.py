from ._realtime_analytics import RealTimeAnalytics
from ._util import _Util


class RealTimeAnalyticsManager:
    """
    Used to manage Real-Time Analytics
    """

    _gis = None
    _util = None

    def __init__(self, url, gis):
        """
        :param url: Base url of Velocity.
        :param gis: An authenticated arcigs.gis.GIS object.
        """
        self._gis = gis

        self._util = _Util(gis, url)

    # ----------------------------------------------------------------------
    @property
    def items(self):
        """
        Get all Real-Time Analytics items
        :return: returns a collection of all configured Real-Time Analytics items
        """
        all_realtime_analytics_response = self._util._get_request("analytics/realtime")
        realtime_analytics_items = [
            RealTimeAnalytics(self._gis, self._util, realtime_item)
            for realtime_item in all_realtime_analytics_response
        ]
        return realtime_analytics_items

    # ----------------------------------------------------------------------
    def get(self, id):
        """
        Get Real-Time Analytics by id
        :param id: unique id of a big data task
        :return: endpoint response of Real-Time Analytics for the given id
        """
        realtime_analytics_item = self._util._get("analytics/realtime", id)
        return RealTimeAnalytics(self._gis, self._util, realtime_analytics_item)

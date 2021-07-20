from ._bigdata_analytics import BigDataAnalytics
from ._util import _Util


class BigDataAnalyticsManager:
    """
    Used to manage Big Data Analytics
    """

    _gis = None
    _util = None

    def __init__(self, url, gis):
        """
        Initializer
        :param url: Base url of Velocity.
        :param gis: An authenticated arcigs.gis.GIS object.
        """
        self._gis = gis

        self._util = _Util(gis, url)

    # ----------------------------------------------------------------------
    @property
    def items(self):
        """
        Get all Big Data Analytics items
        :return: returns a collection of all configured Big Data Analytics items
        """
        all_bigdata_analytics_response = self._util._get_request("analytics/bigdata")
        bigdata_analytics_items = [
            BigDataAnalytics(self._gis, self._util, bigdata_item)
            for bigdata_item in all_bigdata_analytics_response
        ]
        return bigdata_analytics_items

    # ----------------------------------------------------------------------
    def get(self, id):
        """
        Get Big Data Analytics by id
         :param id:  unique id of a big data task
        :return: endpoint response of Big Data Analytics for the given id
        """
        bigdata_analytics_item = self._util._get("analytics/bigdata", id)
        return BigDataAnalytics(self._gis, self._util, bigdata_analytics_item)

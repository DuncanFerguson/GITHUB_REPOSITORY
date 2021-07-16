from .bigdata_analytics_manager import BigDataAnalyticsManager
from .feeds_manager import FeedsManager
from .realtime_analytics_manager import RealTimeAnalyticsManager


class Velocity:
    _gis = None
    _url = None
    _subinfo = None
    _velocity = None
    # manager instances
    _feeds = None
    _realtime_analytics = None
    _bigdata_analytics = None

    def __init__(self, url, gis):
        self._gis = gis
        self._url = url

    @property
    def feeds(self):
        """
        Provides access to the resource manager for managing configured Feeds with ArcGIS Velocity. See :class:`~arcgis.realtime.FeedsManager`.

        :return: feeds
        """
        if self._feeds is None:
            self._feeds = FeedsManager(url=self._url, gis=self._gis)
        return self._feeds

    @property
    def realtime_analytics(self):
        """
         Provides access to  the resource manager for managing configured Real-time analytics tasks with ArcGIS Velocity. See :class:`~arcgis.realtime.RealTimeAnalyticsManager`.

        :return: realtime_analytics
        """
        if self._realtime_analytics is None:
            self._realtime_analytics = RealTimeAnalyticsManager(
                url=self._url, gis=self._gis
            )
        return self._realtime_analytics

    @property
    def bigdata_analytics(self):
        """
         Provides access to the resource manager for managing configured Big data analytics tasks with ArcGIS Velocity. See :class:`~arcgis.realtime.BigDataAnalyticsManager`.

        :return: bigdata_analytics
        """
        if self._bigdata_analytics is None:
            self._bigdata_analytics = BigDataAnalyticsManager(
                url=self._url, gis=self._gis
            )
        return self._bigdata_analytics

from ._task import Task


class Feed(Task):
    """
    Feed class implements Task and provides public facing methods to access Feeds API endpoints
    """

    _id = ""
    _gis = None
    _util = None
    _item = None

    def __init__(self, gis, util, item=None):
        self._gis = gis
        self._util = util
        self._item = item
        self._id = item["id"]

    # ----------------------------------------------------------------------
    def __repr__(self):
        return "<%s id:%s label:%s>" % (
            type(self).__name__,
            self._id,
            self._item["label"],
        )

    # ----------------------------------------------------------------------
    def start(self):
        """
        Start the Feed for the given id
        :return: response of feed start
        """
        return self._util._start("feed", self._id)

    # ----------------------------------------------------------------------
    def stop(self):
        """
        Stop the Feed for the given id
        Return True if the Feed was successfully stopped.
        :return: boolean
        """
        return self._util._stop("feed", self._id)

    # ----------------------------------------------------------------------
    @property
    def status(self):
        """
        Get the status of the running Feed for the given id
        :return: response of Feed status
        """
        return self._util._status("feed", self._id)

    # ----------------------------------------------------------------------
    @property
    def metrics(self):
        """
        Get the metrics of the running Feed for the given id
        :return: response of Feed metrics
        """
        return self._util._metrics("feed/metrics", self._id)

    # ----------------------------------------------------------------------
    def delete(self):
        """
        Deletes an existing feed instance
        :return: A boolean containing True (for success) or
         False (for failure) a dictionary with details is returned.
        """
        return self._util._delete("feed", self._id)

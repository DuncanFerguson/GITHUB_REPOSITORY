import csv
from datetime import datetime
from arcgis.gis.kubernetes._admin._base import _BaseKube
from typing import Dict, Any, Optional, List

########################################################################
class LogManager(_BaseKube):
    """
    Helper class for the management of logs by administrators.

    Logs are the transaction records written by the various components
    of ArcGIS Server.  You can query the logs, change various log settings,
    and check error messages for helping to determine the nature of an issue.

    """

    _url = None
    _con = None
    _json_dict = None
    _json = None
    # ----------------------------------------------------------------------
    def __init__(self, url, gis, initialize=False):
        """Constructor


        ==================     ====================================================================
        **Argument**           **Description**
        ------------------     --------------------------------------------------------------------
        url                    Required string. The machine URL.
        ------------------     --------------------------------------------------------------------
        gis                    Optional string. The GIS or Server object..
        ==================     ====================================================================

        """
        connection = gis
        super(LogManager, self).__init__(gis=gis, url=url)
        self._url = url
        if hasattr(connection, "_con"):
            self._con = connection._con
        if initialize:
            self._init(connection)

    # ----------------------------------------------------------------------
    def __str__(self):
        return "<%s at %s>" % (type(self).__name__, self._url)

    # ----------------------------------------------------------------------
    def __repr__(self):
        return "<%s at %s>" % (type(self).__name__, self._url)

    # ----------------------------------------------------------------------
    def clean(self, start_time=None, end_time=None, level=None):
        """
        Deletes all the log files on all server machines in the site. This is an irreversible
        operation.

        This operation forces the server to clean the logs, which has the effect of freeing up disk space. However, it is not required that you invoke this operation because the server periodically purges old logs.

        ===============     ====================================================================
        **Argument**        **Description**
        ---------------     --------------------------------------------------------------------
        start_time          Optional String. The date associated with a log, in timestamp format
                            (yyyy-mm-ddThh:mm:ss). If specified, logs created after this time
                            will be deleted. When the endTime parameter is also defined, only
                            logs created between the date range will be deleted. When `log_level`
                            is added to the request with a date range specified, only logs that
                            match the selected level and were created within the defined date
                            range will be deleted.
        ---------------     --------------------------------------------------------------------
        end_time            Optional String. The date associated with a log, in timestamp
                            format (yyyy-mm-ddThh:mm:ss). If specified, logs created before this
                            time will be deleted. When the startTime parameter is also defined,
                            only logs created between the date range will be deleted. When
                            `log_level` is added to the request with a date range specified,
                            only logs that match the selected level and were created within the
                            defined date range will be deleted.
        ---------------     --------------------------------------------------------------------
        level               Optional String. The level of logs that will be deleted. If no
                            option is selected, all log messages will be deleted.

                            Values: SEVERE | WARNING | INFO | FINE | VERBOSE | DEBUG

        ===============     ====================================================================


        :return:
           A boolean indicating success (True) or failure (False).

        """
        params = {
            "f": "json",
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time
        if level:
            params["logLevel"] = level
        url = "{}/clean".format(self._url)
        res = self._con.post(path=url, postdata=params)
        if "status" in res:
            return res["status"] == "success"
        elif "success" in res:
            return res["success"] == "true"
        return res

    # ----------------------------------------------------------------------
    def refresh_index(self) -> bool:
        """
        Recreates the log indexes and can be used to troubleshoot issues
        related to accessing logs, such as if new logs are not being
        generated or if existing logs are unavailable.


        :returns: bool

        """
        params = {"f": "json"}
        url = self._url + "/settings/updateLogIndex"
        return self._con.post(url, params).get("status", "failed") == "success"

    # ----------------------------------------------------------------------
    @property
    def settings(self):
        """Gets the current log settings."""
        params = {"f": "json"}
        url = self._url + "/settings"
        try:
            return self._con.get(url, params)
        except:
            return ""

    # ----------------------------------------------------------------------
    def edit(self, level="WARNING"):
        """
        Provides log editing capabilities for the entire site.

        ==================     ====================================================================
        **Argument**           **Description**
        ------------------     --------------------------------------------------------------------
        level                  Optional string. The log level.  Can be one of (in severity order):
                               OFF, DEBUG, VERBOSE, FINE, INFO, WARNING, SEVERE. The default is WARNING.
        ==================     ====================================================================


        :return:
           Boolean

        """
        url = self._url + "/settings/edit"
        allowed_levels = (
            "OFF",
            "SEVERE",
            "WARNING",
            "INFO",
            "FINE",
            "VERBOSE",
            "DEBUG",
        )
        current_settings = self.settings
        current_settings["f"] = "json"

        if level.upper() in allowed_levels:
            current_settings["logLevel"] = level.upper()

        res = self._con.post(path=url, postdata=current_settings)
        if "success" in res:
            return res["success"] == "true"
        return res

    # ----------------------------------------------------------------------
    def query(
        self,
        start_time=None,
        end_time=None,
        level="WARNING",
        log_code=None,
        users=None,
        request_ids=None,
        service_types=None,
        source=None,
        show_stack_traces=True,
        num=1000,
    ):
        """
        The query operation on the logs resource provides a way to
        aggregate, filter, and page through logs across the entire site.

        ==================     ====================================================================
        **Argument**           **Description**
        ------------------     --------------------------------------------------------------------
        start_time             Optional string. The oldest time to query logs against, formatted as
                               either a timestamp (yyyy-mm-ddThh:mm:ss) or milliseconds from epoch.
                               The default is the beginning of all recorded logs.
        ------------------     --------------------------------------------------------------------
        end_time               Optional string. The most recent time to query against, formatted as
                               either a timestamp (yyyy-mm-ddThh:mm:ss) or milliseconds from epoch.
                               The default is the current date.
        ------------------     --------------------------------------------------------------------
        level                  Optional string. Gets only the records with a log level at or more
                               severe than the level declared here. Can be one of (in severity
                               order): DEBUG, VERBOSE, FINE, INFO, WARNING, SEVERE. The
                               default is WARNING.
        ------------------     --------------------------------------------------------------------
        log_code               Optional String. Specifies the log codes assigned to the logs. When
                               specified, query will return logs associated with those codes.
        ------------------     --------------------------------------------------------------------
        users                  Optional String. The username of a user within the organization that
                               can be used to further filter log results.
        ------------------     --------------------------------------------------------------------
        request_ids            Optional String. An ID assigned to a specific server event.
        ------------------     --------------------------------------------------------------------
        service_types          Optional String. The service type of a service within the
                               organization that can be used to further filter query results.

                               Note: Currently, only MapServer, GPServer, and FeatureServer are the
                                     only supported service types.
        ------------------     --------------------------------------------------------------------
        source                 Optional String. The source of logged events.
        ------------------     --------------------------------------------------------------------
        show_stack_traces      Optional Boolean. If `True` the stack trace is returned.
        ------------------     --------------------------------------------------------------------
        num                    Optional Int.  The maximum number of log records to be returned by
                               this query. The default messages per page is 1000. The limit for
                               this parameter is 10000 records.
        ==================     ====================================================================

        :return:
           A JSON of the log items that match the query. If export option is set to True, the
           output log file path is returned.

        """

        allowed_levels = ("SEVERE", "WARNING", "INFO", "FINE", "VERBOSE", "DEBUG")
        params = {"f": "json", "num": num}
        params["start"] = 1
        url = "{url}/query".format(url=self._url)
        if start_time is not None and isinstance(start_time, datetime):
            params["startTime"] = start_time.strftime("%Y-%m-%dT%H:%M:%S,%f")
        if end_time is not None and isinstance(end_time, datetime):
            params["endTime"] = end_time.strftime("%Y-%m-%dT%H:%M:%S,%f")
        if level.upper() in allowed_levels:
            params["logLevel"] = level
        if log_code is not None:
            params["logCode"] = log_code
        if users:
            params["users"] = users
        if request_ids:
            params["requestIDs"] = request_ids
        if service_types:
            params["serviceTypes"] = service_types
        if source:
            params["source"] = source
        if show_stack_traces is not None:
            params["showStackTraces"] = show_stack_traces
        res = self._con.get(url, params)
        messages = res["messages"]
        # ['messages', 'total', 'start', 'num', 'nextStart', 'query']
        while res["nextStart"] != -1:
            params["start"] = res["nextStart"]
            res = self._con.get(url, params)
            messages.extend(res["messages"])
        return messages

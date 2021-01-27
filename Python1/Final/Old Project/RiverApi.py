from climata.usgs import DailyValueIO


def riverflowapi():
    """This uses the climata api. It may need to be downloaded"""
    station_id = '09163500'  # This is the loma station id
    parameter_id = '00060'  # This gets use the CFS
    # parameter_id2 = '00010'  # This gets use water Temp in Celsius

    data = DailyValueIO(start_date= "2020-10-01",
                         end_date = "2020-11-01",
                         station = station_id,
                         parameter= parameter_id)

    for series in data:
        flow = [r[1] for r in series.data]
        dates = [r[0] for r in series.data]

    flowdates = [flow,dates]
    return flowdates



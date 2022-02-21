import pandas as pd
import pyodbc
from datetime import datetime, timedelta

from prophet import Prophet
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
pio.renderers.default='browser'

# using performance counters instead of CDR's
numdays = 30
startday = datetime.today().replace(hour=0, minute=0, second=0, microsecond = 0) - timedelta(days=numdays)
endday = datetime.today().replace(hour=0, minute=0, second=0, microsecond = 0)
dfdays = pd.DataFrame({'report_date':pd.date_range(startday, periods=numdays * 24, freq = 'H')})  # dataframe to hold all the dates so we can put None's in missing days

server = 'nqsql1' 
database = 'rollup' 
username = 'anomalyTool' 
password = 'DonAnomalyDalton' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#select ZTE LTE
query = '''SELECT report_date, Technology, sum(FDD_Cell_DL_MAC_Data_Volume_MB) as Total_DL_MB, sum(FDD_Cell_UL_MAC_Data_Volume_MB) as Total_UL_MB \
from dbo.fact_z_lte_combined_data_bts_sec_vw \
where is_test_site = 'False' AND report_date > \'%s\' AND report_date < \'%s\' \
    GROUP BY report_date, Technology''' % (startday, endday)

timestart = datetime.now()
print("Started ZTE Query at :", timestart)
df = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)

# change Technology to 'ZTE_FDD'
df.replace('LTE','ZTE_LTE', inplace=True)
dfdays['Technology'] = 'ZTE_LTE'
df = df.merge(dfdays, how='outer')

# select NokiaTDD
query = '''SELECT report_date, Technology, sum(Cell_DL_MAC_Data_Volume_MB) as Total_DL_MB, sum(Cell_UL_MAC_Data_Volume_MB) as Total_UL_MB \
from dbo.fact_nokia_lte_tdd_data_bts_sec_vw \
where Technology = \'LTE_TDD\' AND is_test_site = \'False\' AND report_date > \'%s\' AND report_date < \'%s\' \
    GROUP BY report_date, Technology''' % (startday, endday)

timestart = datetime.now()
print("Started Nokia TDD Query at :", timestart)
df2 = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)

df2.replace('LTE_TDD','Nokia_TDD',inplace=True)
dfdays['Technology'] = 'Nokia_TDD'
df2 = df2.merge(dfdays, how='outer')
df = df.append(df2)  # append NokiaTDD to ZTE

# select NokiaFDD
query = '''SELECT report_date, Technology, sum(Cell_DL_MAC_Data_Volume_MB) as Total_DL_MB, sum(Cell_UL_MAC_Data_Volume_MB) as Total_UL_MB \
from dbo.fact_nokia_lte_fdd_data_bts_sec_vw \
where dim_entity_id=2 AND Technology = \'LTE\' AND is_test_site = \'False\' AND report_date > \'%s\' AND report_date < \'%s\' \
    GROUP BY report_date, Technology''' % (startday, endday)

timestart = datetime.now()
print("Started Nokia FDD Query at :", timestart)
df2 = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)

df2.replace('LTE','Nokia_FDD',inplace=True)
dfdays['Technology'] = 'Nokia_FDD'
df2 = df2.merge(dfdays, how='outer')
df = df.append(df2)  # append NokiaFDD to ZTE and Nokia TDD

# ALU LTE

query = '''SELECT report_date, technology AS Technology, sum(VS_DL_RLC_Payload_MB) as Total_DL_MB, sum(VS_UL_RLC_Payload_MB) as Total_UL_MB \
from dbo.fact_ALU_LTE_data_bts_sec_vw \
where dim_entity_id=2 AND Technology = \'LTE\' AND is_test_site = \'False\' AND report_date > \'%s\' AND report_date < \'%s\' \
    GROUP BY report_date, Technology''' % (startday, endday)

timestart = datetime.now()
print("Started ALU FDD Query at :", timestart)
df2 = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)

df2['report_date'] = pd.to_datetime(df2['report_date'])
df2.replace('LTE','ALU_FDD',inplace=True)
dfdays['Technology'] = 'ALU_FDD'
df2 = df2.merge(dfdays, how='outer')
df = df.append(df2)  # add to dataframe

# ZTE UMTS
query = '''SELECT Report_Date, sum(cell_dl_traffic_volume_ps_fp_KB)/1000 as Total_DL_MB, sum(cell_ul_traffic_volume_ps_fp_KB)/1000 as Total_UL_MB \
from dbo.FACT_Z_UMTS_DATA_BTS_CELL_VW \
where Report_Date > \'%s\' AND Report_Date < \'%s\' \
    GROUP BY Report_Date''' % (startday, endday)

timestart = datetime.now()
print("Started ZTE UMTS Query at :", timestart)
df2 = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)

df2['Technology'] = 'UMTS'
df2['Report_Date'] = pd.to_datetime(df2['Report_Date'])
df2.rename(columns={'Report_Date':'report_date'}, inplace=True)
dfdays['Technology'] = 'UMTS'
df2 = df2.merge(dfdays, how='outer')
df = df.append(df2)  # append UMTS to dataframe

# ZTE CDMA
endday = datetime.today().replace(minute=0, second=0, microsecond = 0)
query = '''SELECT Report_Date, sum(Fwd_RevAB_TCH_Physical_MB) as Total_DL_MB, sum(Rev_RevAB_TCH_Physical_MB) as Total_UL_MB \
from dbo.FACT_Z_EVDO_BTS_SEC_CARR_VW \
where Report_Date > \'%s\' AND Report_Date < \'%s\' \
    GROUP BY Report_Date''' % (startday, endday)

timestart = datetime.now()
print("Started ZTE CDMA Query at :", timestart)
df2 = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)

df2['Technology'] = 'CDMA'
df2['Report_Date'] = pd.to_datetime(df2['Report_Date'])
df2.rename(columns={'Report_Date':'report_date'}, inplace=True)
dfdays['Technology'] = 'CDMA'
df2 = df2.merge(dfdays, how='outer')
df = df.append(df2)  # append UMTS to dataframe

# # write to file
df.to_csv("hourlyMB.csv")

# plot results
df.sort_values(by=['report_date'], ascending = True, inplace = True)

# DL plots
fig = px.line(df,x='report_date',y='Total_DL_MB',color='Technology', title='DL data for last 30 days').update_traces(connectgaps=False)
fig.show()

fig = px.line(df,x='report_date',y='Total_DL_MB',color='Technology', log_y=True, title='DL data for last 30 days, log scale').update_traces(connectgaps=False)
fig.show()
#UL plots
fig = px.line(df,x='report_date',y='Total_UL_MB',color='Technology', title='UL data for last 30 days').update_traces(connectgaps=False)
fig.show()

fig = px.line(df,x='report_date',y='Total_UL_MB',color='Technology', log_y=True, title='UL data for last 30 days, log scale').update_traces(connectgaps=False)
fig.show()

# Prophet part
def anom_func(row):
    if row['y'] > row['yhat_upper'] or row['y'] < row['yhat_lower']:
        return 'anomaly'
    return ''

for tech in df['Technology'].unique():
    df2 = df[df['Technology'] == tech]
    df2 = df2[['report_date','Total_DL_MB']]
    df2.columns = ['ds', 'y']
    m = Prophet(changepoint_prior_scale=0.01,interval_width = 0.95).fit(df2[0:-24])
    future = m.make_future_dataframe(periods=24, freq='H')
    fcst = m.predict(future)
    df2['ds'] = pd.to_datetime(df2['ds'])
    df2 = df2.join(fcst.set_index('ds'), on='ds')

    df2['anomaly'] = df2.apply(anom_func,axis=1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df2['ds'], y=df2['yhat_upper'],line_color='lightskyblue', name='Upper CI')) # fill to yhat_lower
    fig.add_trace(go.Scatter(x=df2['ds'], y=df2['yhat_lower'], fill='tonexty',line_color='lightskyblue', name='Lower CI')) 
    fig.add_trace(go.Scatter(x=df2['ds'], y=df2['y'], line_color='black', name= tech + ' hourly'))
    fig.add_trace(go.Scatter(x=df2[df2['anomaly'] == 'anomaly']['ds'], y=df2[df2['anomaly'] == 'anomaly']['y'],mode='markers', name='Anomaly', marker_color='red'))
    fig.update_layout(
    title= tech + " Data",
    xaxis_title="Date",
    yaxis_title="Hourly MB")
    fig.show()
    count = df2[-24:][df2[-24:]['anomaly'] == 'anomaly']['anomaly'].count()
    if count > 4:
        print("Anomaly with" + tech + " MB's.  Count: ", count)
#%%
#################################################################
# voice

# ZTE UMTS
query = '''SELECT Report_Date, sum(MOU) as MOU \
from dbo.FACT_Z_UMTS_VOICE_BTS_CELL_VW \
where Report_Date > \'%s\' AND Report_Date < \'%s\' \
    GROUP BY Report_Date''' % (startday, endday)

timestart = datetime.now()
print("Started ZTE UMTS Query at :", timestart)
df = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)

df['Technology'] = 'UMTS'
df['Report_Date'] = pd.to_datetime(df['Report_Date'])
df.rename(columns={'Report_Date':'report_date'}, inplace=True)
dfdays['Technology'] = 'UMTS'

# ZTE CDMA
    
query = '''SELECT Report_Date, sum(MOU) as MOU \
from dbo.FACT_Z_CDMA_VOICE_BTS_SEC_CAR_VW \
where Report_Date > \'%s\' AND Report_Date < \'%s\' \
    GROUP BY Report_Date''' % (startday, endday)

timestart = datetime.now()
print("Started ZTE CDMA voice Query at :", timestart)
df2 = pd.read_sql(query,con=conn)
print("Ended Query after: ",datetime.now() - timestart)
conn.close()

df2['Technology'] = 'CDMA'
df2['Report_Date'] = pd.to_datetime(df2['Report_Date'])
df2.rename(columns={'Report_Date':'report_date'}, inplace=True)
dfdays['Technology'] = 'CDMA'
df2 = df2.merge(dfdays, how='outer')
df = df.append(df2)  # append CDMA voice to dataframe

# plot results
df.sort_values(by=['report_date'], ascending = True, inplace = True)
import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'
# DL plots
fig = px.line(df,x='report_date',y='MOU',color='Technology', title='Voice MOU for last 30 days').update_traces(connectgaps=False)
fig.show()

fig = px.line(df,x='report_date',y='MOU',color='Technology', log_y=True, title='Voice MOU for last 30 days, log scale').update_traces(connectgaps=False)
fig.show()

# Prophet detection and plots
for tech in df['Technology'].unique():
    df2 = df[df['Technology'] == tech]
    df2 = df2[['report_date','MOU']]
    df2.columns = ['ds', 'y']
    m = Prophet(changepoint_prior_scale=0.01,interval_width = 0.95).fit(df2[0:-24])
    future = m.make_future_dataframe(periods=24, freq='H')
    fcst = m.predict(future)
    df2['ds'] = pd.to_datetime(df2['ds'])
    df2 = df2.join(fcst.set_index('ds'), on='ds')

    df2['anomaly'] = df2.apply(anom_func,axis=1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df2['ds'], y=df2['yhat_upper'],line_color='lightskyblue', name='Upper CI')) # fill to yhat_lower
    fig.add_trace(go.Scatter(x=df2['ds'], y=df2['yhat_lower'], fill='tonexty',line_color='lightskyblue', name='Lower CI')) 
    fig.add_trace(go.Scatter(x=df2['ds'], y=df2['y'], line_color='black', name= tech + ' hourly'))
    fig.add_trace(go.Scatter(x=df2[df2['anomaly'] == 'anomaly']['ds'], y=df2[df2['anomaly'] == 'anomaly']['y'],mode='markers', name='Anomaly', marker_color='red'))
    fig.update_layout(
    title= tech + " MOU",
    xaxis_title="Date",
    yaxis_title="Hourly MOU")
    fig.show()
    
    count = df2[-24:][df2[-24:]['anomaly'] == 'anomaly']['anomaly'].count()
    if count > 4:
        print("Anomaly with" + tech + " MOUs.  Count: ", count)
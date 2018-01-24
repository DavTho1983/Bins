import pandas as pd

bins = pd.read_csv('binfeed.ical', sep=':', header=None, index_col=None, skiprows=6)
bins.columns = ['cols', 'vals']
bins['index_col'] = bins.index
bins = pd.pivot(index=bins.groupby('cols').cumcount(),
              columns=bins['cols'],
              values=bins['vals'])
bins.columns = ['Begin', 'Datestamp', 'Date', 'End', 'Summary', 'UID']
bins['Date_as_Datetime']=pd.to_datetime(bins['Date'])
same_day_collections = bins.groupby('Date_as_Datetime').count()
bins = bins.sort_values(by=['Date_as_Datetime'])
print(bins.head())
print(bins.tail())
print(same_day_collections)

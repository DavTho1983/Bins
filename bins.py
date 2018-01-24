import pandas as pd
import unittest

def binsFunc(filename) :
    bins = pd.read_csv(filename, sep=':', header=None, index_col=None, skiprows=6)
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
    return same_day_collections.iloc[0][1] == 1

class SomeTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(binsFunc('binfeed.ical'))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

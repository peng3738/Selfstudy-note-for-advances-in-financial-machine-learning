import numpy as np
import pandas as pd

def getRolledSeries(pathIn,key):
    #series=pd.read_hdf(pathIn,key='bars/ES_10k')
    pathIn='E:python_study/advances_in_financial_machine_learning/financial-data-structures-master/saved_data/dollar_bars.csv'
    series=pd.read_csv(pathIn)
    #series['Time']=pd.to_datetime(series['Time'],format='%Y%m%d%H%M%S%f')
    series['Time']=pd.to_datetime(series['date'],format='%m/%d/%Y %H:%M:%S.%f')
    series=series.set_index('Time')
    gaps=rollGaps(series)
    for fld in ['Close','VWAP']:series[fld]-=gaps
    return series
#-------------------------
def rollGaps(series, dictio={'Instrument':'FUT_CUR_GEN_TICKER','Open':'PX_OPEN',\
    'Close':'PX_LAST'},matchEnd=True):
    #Compute gaps at each roll, between previous close and next open
    #dictio={'Instrument':'date','Open':'open','Close':'close'}
    rollDates=series[dictio['Instrument']].drop_duplicates(keep='first').index
    gaps=series[dictio['Close']]*0
    iloc=list(series.index)
    iloc=[iloc.index(i)-1 for i in rollDates]# index of days prior to roll 
    gaps.loc[rollDates[1:]]=series[dictio['Open']].loc[rollDates[1:]]-\
	series[dictio['Close']].iloc[iloc[1:]].values
    gaps=gaps.cumsum();
    if matchEnd:gaps-=gaps.iloc[-1]#roll backward
    return gaps

def mpSampleTW(t1,numCoEvents,molecule):
    # Derive average uniqueness over the event's lifespan
    wght=pd.Series(index=molecule)
    for tIn,tOut in t1.loc[wght.index].iteritems():
        wght.loc[tIn]=(1./numCoEvents.loc[tIn:tOut]).mean()
    return wght
#--------------------------------------
numCoEvents=mpPandasObj(mpNumCoEvents,('molecule',events.index),numThreads,\
                        closeIdx=close.index,t1=events['t1'])
numCoEvents=numCoEvents.loc[~numCoEvents.index.duplicated(keep='last')]
numCoEvents=numCoEvents.reindex(close.index).fillna(0)
out['tW']=mpPdandasObj(mpSampleTW,('molecule',events.index),numThreads,\
                       t1=events['t1'],numCoEvents=numCoEvents)

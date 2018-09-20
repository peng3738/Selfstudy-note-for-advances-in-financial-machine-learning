def getEvents(close,tEvents,ptS1,trgt,minRet,numThreads,t1=False):
    #1)get target
    trgt=trgt.loc[tEvents]
    trgt=trgt[trgt>minRet]#minRet
    #2)get t1 (max holding period)
    if t1 is False:t1=pd.Series(pd.NaT,index=tEvents)
    #3) form events object,apply stop loss on t1
    side_=pd.Series(1.,index=trgt.index)
    events=pd.concat({'t1':t1,'trgt':trgt,'side':side_}),axis=1).dropna(subset=['trgt'])
    df0=mpPandasObj(func=applyPtS1OnT1,pdObj=('molecule',events.index),\
                    numThreads=numThreads,close=close,events=events,ptS1=[ptS1,ptS1])
    events['t1']=df0.dropna(how='all').min(axis=1)#pd.min ignores nan
    events=events.drop('side',axis=1)
    return events

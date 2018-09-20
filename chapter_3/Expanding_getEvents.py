def getEvents(close,tEvents,ptS1,trgt,minRet,numThreads,t1=False,side=None):
    #1)get target
    trgt=trgt.loc[tEvents]
    trgt=trgt[trgt>minRet]#minRet
    #2)get t1 (max holding period)
    if t1 is False:t1=pd.Series(pd.NaT,index=tEvents)
    #3)form events pbject,apply stop loss on t1
    if side is None:side_,ptS1_=pd.Series(1.,index=trgt.index),[ptS1[0],ptS1[0]]
    else:side_.ptS1_=side.loc[trgt.index],ptS1[:2]
    events=pd.concat({'t1':t1,'trgt':trgt,'side':side_},axis=1).dropna(subset=['trgt'])
    df0=mpPandasObj(func=applyPtS1OnT1,pdObj=('molecule',events.index),\
                    numThreads=numThreads,close=inst['Close'],events=events,ptS1=ptS1_)
    events['t1']=df0.dropna(how='all').min(axis=1)#pd.min ignores nan
    if side is None:events=events.drop('side',axis=1)
    return events



    

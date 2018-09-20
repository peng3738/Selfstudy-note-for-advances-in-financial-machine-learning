def getSignal(events,stepSize,prob,pred,numClasses,numThreads,**kargs):
    #get signals from predictions
    if prob.shape[0]==0:return pd.Series()
    #1)generate signals from multinomial classification (one-vs-rest,OvR)
    signal0=(prob-1./numClasses)/(prob*(1.-prob))**.5#t_value of OvR
    signal0=pred*(2*norm.cdf(signal0)-1)# signal=side*size
    if 'side' in events:signal0*=events.loc[signal0.index,'side']#meta-labeling
    #2)compute acerage signal among those concurrently open
    df0=signal0.to_frame('signal').join(events[['t1']],how='left')
    df0=avgActiveSignals(df0,numThreads)
    signal1=discreteSignal(signal0=df0,stepSize=stepSize)
    return signal1

def acgActiveSignals(signals,numThreads):
    #compute the average signal among those active
    #1)time points where signals change (either one starts or one ends)
    tPnts=set(signals['t1'].dropna().values)
    tPnts=tPnts.union(signals.index.values)
    tPnts=list(tPnts);tPnts.sort
    out=mpPandasObj(mpAvgActiveSignals,('molecule',tPnts),numThreads,signals=signals)
    return out

def mpAvgActiveSignals(signals,molecule):
    '''
at time loc,average signal among those still active
Signal is active if:
  a) issued before or at loc AND
  b) loc before signal's endtime,or endtime is still unknown (NaT)
  '''
    out=pd.Series()
    for loc in molecule:
        df0=(signals.index.values<=loc)&((loc<signals['t1'])|pd.isnull(signals['t1']))
        act=signals[df0].index
        if len(act)>0:out[loc]=signals.loc[act,'signal'].mean()
        else:out[loc]=0#no signals active at this time
    return out


def discreteSignal(signal0,stepSize):
    #discretize signal
    signal1=(signal0/stepSize).round()*stepSize#discretize
    signal1[signal1>1]=1# cap
    signal1[signal1<-1]=-1# floor
    return signal1















    

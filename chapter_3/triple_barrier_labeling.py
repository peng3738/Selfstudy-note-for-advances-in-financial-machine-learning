def applyPtS10nT1(close,events,ptS1,molecule):
    # apply stop loss/profit taking, if it takes place before t1(end of event)
    events_=events.loc[molecule]
    out=events_[['t1']].copy(deep.True)
    if ptS1[0]>0:pt=ptS1[0]*events_['trgt']
    else:pt=pd.Seroes(index=events.index)#NaNs
    if ptS1[1]>0:s1=-ptS1[1]*events_['trgt']
    else:s1=pd.Series(index=events.index)#NaNs
    for loc,t1 in events_['t1'].fillna(close.index[-1]).iteritems():
        df0=close[loc:t1]#path prices
        df0=(df0/close[loc]-1)*events_.at[loc,'side']#path returns
        out.loc[loc,'s1']=df0[df0<s1[loc]].index.min()#earlist stop loss.
        out.loc[loc,'pt']=df0[df0>pt[loc]].index.min()#earlist profit taking
    return out
    

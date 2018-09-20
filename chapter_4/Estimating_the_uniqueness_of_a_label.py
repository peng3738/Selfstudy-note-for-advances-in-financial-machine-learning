def mpNumCoEvents(closeIdx,t1,molecule):
    '''
    compute the number of concurrent events per bar.
    +molecule[0] is the date of the first event on which the weight will be computed
    +molecule[-1] is the date of the last event on which the weight will be computed
    Any events that starts before t1[molecule].max() impacts the count.
    '''
    #1) find events that span the period [molecule[0],molecule[-1]]
    t1=t1.fillna(closeIdx[-1])# unclosed events still must impact other weights
    t1=t1[t1>=molecule[0]]#events that end at or after molecule[0]
    t1=t1.loc[:t1[molecule].max()]#events that start at or before t1[molecule].max()

##2)count events spanning a bar
    iloc=closeIdx.searchsorted(np.array([t1.index[0],t1.max()]))
    count=pd.Series(0,index=closeIdx[iloc[0]:iloc[1]+1])
    for tIn,tOut in t1.iteritems():count.loc[tIn:tOut]+=1.
    return count.loc[molecule[0]:t1[molecule].max()]

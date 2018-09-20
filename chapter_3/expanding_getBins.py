def getBins(events,close):
    '''
    compute event's outcome(including side information, if provided).
    events is a DataFrame where:
    -events.index is event's starttime
    -events['t1'] is the event's endtime
    -events['trgt'] is the event's target
    -events['side'] (optional) implies the algo's position side
    Case 1: ('side' not in events):bin in (-1,1)<-label by price action
    Case 2: ('side' in events): binin (0,1)<-label by pn1(meta_labeling)
    '''
    #1) prices aligned with events
    events_=events.dropna(subset=['t1'])
    px=events_.index.union(events_['t1'].value).drop_duplicates()
    px=close.reindex(px,method='bfill')
    #2) create out object
    out=pd.DataFrame(index=events_.index)
    out['ret']=px.loc[events_['t1'].values].values/px.loc[events_.index]-1
    if 'side' in events_:out['ret']*=events_['side']# meta-labeling
    out['bin']=np.sign(out['ret'])
    if 'side' in events_:out.loc[out['ret']<=0,'bin']=0#meta-labeling
    return out

    

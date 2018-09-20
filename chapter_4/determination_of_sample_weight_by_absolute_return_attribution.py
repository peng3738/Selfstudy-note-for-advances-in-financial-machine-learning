def mpSampleW(t1,numCoEvents,close,molecule):
    # Derive sample wiehgt by return attribution
    ret=np.log(close).diff()#log-returns, so that they are additive
    wght=pd.Series(index=molecule)
    for tIn,tOut in t1.loc[wght.index].iteritems():
        wght.loc[tIn]=(ret.loc[tIn:tOut]/numCoEvents.loc[tIn:tOut]).sum()
        return wght.abs()
#-------------------------------------
    out['w']=mpPandasObj(mpSampleW,('molecule',events.index),numThreads,\
                         t1=events['t1'],numCoEvents=numCoEvents,close=close)
    out['w']*=out.shape[0]/out['w'].sum()
    

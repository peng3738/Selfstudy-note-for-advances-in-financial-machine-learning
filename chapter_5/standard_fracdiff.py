def fracDiff(series,d,thres=0.1):
    '''
Increasing width window, with treatment of NaNS
Note 1:For thres=1,nothing is skipped.
Note 2: d can be any positive fractional, not necessarily bounded [0,1].
'''
    #1) Compute weights for the londest series
    w=getWeights(d,series.shape[0])
    #2) Determine initial calcs to be skipped based on weight-loss threshold
    w_=np.cumsum(abs(w))
    w_/=w_[-1]
    skip=w_[w_>thres].shape[0]
    #3)Apply weights to values
    df={}
    for name in series.columns:
        seriesF,df_=series[[name]].fillna(method='fill').dropna(),pd.Series()
        for iloc in range(skip,seriesF.shape[0]):
            loc=seriesF.index[iloc]
            if not np.isfinite(series.loc[loc,name]):continue   #exclude NAs
            df_[loc]=np.dot(w[-(iloc+1):,:].T,seriesF.loc[:loc])[0,0]
            df[name]=df_.copy(deep=True)
    df=pd.concat(df,axis=1)
    return df
        

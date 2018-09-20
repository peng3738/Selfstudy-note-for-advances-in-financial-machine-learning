'''
def convert2(row):
    return datetime.strptime(str(row), "%Y-%m-%d")


def getWeights_FFD(d, thres, lim):
    w, k = [1.], 1
    ctr = 0
    while True:
        w_ = -w[-1]/k*(d-k+1)
        if abs(w_)<thres:
            break
        w.append(w_)
        k+=1
        ctr += 1
        if ctr == lim:
            break
    w = np.array(w[::-1]).reshape(-1,1)
    return w
'''

def fracDiff_FFD(series,d,thres=1e-5):
    '''
Constant width window(new solution)
Note 1: thres determines the cut-off weight for the window
Note 2: d can be any positive fractional, not necessarily bounded [0,1].
'''
    #1) Compute weights for the longest series
    w=getWeights_FFD(d,thres)
    width=len(w)-1
    #2) Apply weights to values
    df={}
    for name in series.columns:
        seriesF,df_=series[[name]].fillna(method='ffill').dropna(),pd.Series()
        for iloc1 in range(width,seriesF.shape[0]):
            loc0,loc1=seriesF.index[iloc1-width],seriesF.index[iloc1]
            if not np.isfinite(series.loc[loc1,name]):continue #exclude NAs
            df_[loc1]=np.dot(w.T,seriesF.loc[loc0:loc1])[0,0]
        df[name]=df_.copy(deep=True)
    df=pd.concat(df,axis=1)
    return df

    

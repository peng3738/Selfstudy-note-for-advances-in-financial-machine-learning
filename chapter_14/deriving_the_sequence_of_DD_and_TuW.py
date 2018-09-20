def computeDD_TuW(series,dollars=False):
    #compute series of drawdowns and the time under water associated with them
    df0=series.to_frame('pnl')
    df0['hwm']=series.expanding().max()
    df1=df0.groupby('hwm').min().rest_index()
    df1.columns=['hwm','min']
    df1.index=df0['hwm'].drop_duplicates(keep='first').index # time of hwm
    df1=df1[df1['hwm']>df1['min']]#hwm followed by a drawdown
    if dollars:dd=df1['hwm']-df1['min']
    else:d=1-df1['min']/df1['hwm']
    tuw=((df1.index[1:]-df1.index[:-1])/np.timedelta64(1,'Y')).values#in years
    tuw=pd.Series(tuw,index=df1.index[:-1])
    return dd,tuw

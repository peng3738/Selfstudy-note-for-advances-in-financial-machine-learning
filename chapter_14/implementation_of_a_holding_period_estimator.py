def getHoldingPeriod(tPos):
    #Derive avg holding period (in days) using avg entry time pairing algo
    hp,eEntry=pd.DataFrame(columns=['dT','w']),0.
    pDiff,tDiff=tPos.diff(),(tPos.index-tPos.index[0])/np.timedelta64(1,'D')
    for i in range(1,tPos.shape[0]):
        if pDiff.iloc[i]*tPos.iloc[i-1]>=0:# increased or unchanged
            if tPos.iloc[i]!=0:
                tEntry=(tEntry*tPos.iloc[i-1]+tDiff[i]*pDiff.iloc[i])/tPos.iloc[i]
            else:# decreased
                if tPos.iloc[i]*tPos.iloc[i-1]<0:#flip
                    hp.loc[tPos.index[i],['dT','w']]=(tDiff[i]-eEntry,abs(pDiff.iloc[i-1]))
                    tEntry=tDiff[i] #reset entry time
                else:
                    hp.loc[tPos.index[i],['dT','w']]=(tDiff[i]-eEntry,abs(pDiff.iloc[i]))
    if hp['w'].sum()>0:hp=(hp['dT']*hp['w']).sum()/hp['w'].sum()
    else:hp=np.nan
    return hp

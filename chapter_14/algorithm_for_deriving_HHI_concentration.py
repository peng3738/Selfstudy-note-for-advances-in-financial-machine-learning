rHHIPos=getHHI(ret[ret>=0])#concentration of positive returns per bet
rHHINeg=getHHI(ret[ret<0])#concentration of negative returns per bet
tHHI=getHHI(ret.groupby(pd.TimeGrouper(freq='M')).count())#concentr.bets/month
#------------------------------------------
def getHHI(betRet):
    if betRet.shape[0]<=2:return np.nan
    wght=betRet/betRet.sum()
    hhi=(wght**2).sum()
    hhi=(hhi-betRet.shape[0]**-1)/(1.-betRet.shape[0]**-1)
    return hhi

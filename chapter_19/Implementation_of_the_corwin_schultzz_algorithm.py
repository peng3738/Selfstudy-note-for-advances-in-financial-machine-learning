def getBeta(series,sl):
    h1=series[['High','Low']].values
    h1=np.log(h1[:,0]/h1[:,1])**2
    h1=pd.Series(h1,index=series.index)
    beta=pd.stats.moments.rolling_sum(h1,window=2)
    beta=pd.stats.moments.rolling_mean(beta,window=sl)
    return beta.dropna()
#----------------------------------

def getGamma(series):
    h2=pd.stats.moments.rolling_max(series['High'],window=2)
    l2=pd.stats.moments.rolling_min(series['Low'],window=2)
    gamma=np.log(h2.values/l2.values)**2
    gamma=pd.series(gamma,index=h2.index)
    return gamma.dropna()

#------------------------------------
def getAlpha(beta,gamma):
    den=3-2*2**.5
    alpha=(2**.5-1)*(beta*.5)/den
    alpha-=(gamma/den)**.5
    alpha[alpha<0]=0 # set netative alphas to 0
    return alpha.dropna()

#--------------------------------
def corwinSchultz(series,sl=1):
    #Note:S<0 iff alpha<0
    beta=getBeta(series,sl)
    gamma=getGamma(series)
    alpha=getAlpha(beta,gamma)
    spread=2*(np.exp(alpha)-1)/(1+np.exp(alpha))
    startTime=pd.Series(series.index[0:spread.shape[0]],index=spread.index)
    spread=pd.concat([spread,startTime],axis=1)
    spread.columns=['Spread','Start_time']# 1st loc used to compute beta
    return spread

#------------------------------
def getSigma(beta,gamma):
    k2=(8/np.pi)**.5
    den=3-2*2**.5
    sigma=(2**-.5-1)*beta**.5/(k2*den)
    sigma+=(gamma/(k2**2*den))**.5
    sigma[sigma<0]=0
    return sigma

#--------------------------------

















    

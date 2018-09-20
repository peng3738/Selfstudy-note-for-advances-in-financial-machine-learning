import scipy.cluster.hierarchy as sch, random
import numpy as np
import pandas as pd
import CLA
from HRP import correlDist,getIVP,getQuasiDiag,getRecBipart
#-------------------------
def generateData(nObs,sLength,size0,size1,mu0,sigma0,sigma1F):
    #Time series of correlated variables
    #1)generate random uncorrelated data
    x=np.random.normal(mu0,sigma0,size=(nObs,size0))
    #2)create correlation between the variables
    cols=[random.randint(0,size0-1) for i in range(size1)]
    y=x[:,cols]+np.random.normal(0,sigma0*sigma1F,size=(nObs,len(cols)))
    x=np.append(x,y,axis=1)
    #3)add common random shock
    point=np.random.randint(sLength,nObs-1,size=2)
    x[np.ix_(point,[cols[0],size0])]=np.array([[-.5,-.5],[2,2]])
    #4)add specific random shock
    point=np.random.randint(sLength,nObs-1,size=2)
    x[point,cols[-1]]=np.array([-.5,2])
    return x,cols
#--------------------------------------
def getHRP(cov,corr):
    # construct a hierarchical portfolio
    corr,cov=pd.DataFrame(corr),pd.DataFrame(cov)
    dist=correlDist(corr)
    link=sch.linkage(dist,'single')
    sortIx=getQuasiDiag(link)
    sortIx=corr.index[sortIx].tolist()# recover labels
    hrp=getRecBipart(cov,sortIx)
    return hrp.sort_index()
#-------------------------------------
def getCLA(cov,**kargs):
    #compute CLA's minimum variance portfolio
    mean=np.arange(cov.shape[0]).reshape(-1,1)# not used by c portf
    lB=np.zeros(mean.shape)
    uB=np.ones(mean.shape)
    cla=CLA.CLA(mean,cov,lB,uB)
    cla.solve()
    return cla.w[-1].flatten()
#-----------------------------------
def hrpMC(numIters=1e4,nObs=520,size0=5,size1=5,mu0=0,sigma0=1e-2,sigma1F=.25,\
          sLength=260,rebal=22):
    #Monte Carlo experiment on HRP
    methods=[getIVP,getHRP,getCLA]
    stats,numIter={i.__name__:pd.Series() for i in methods},0
    pointers=range(sLength,nObs,rebal)
    while numIter<numIters:
        print(numIter)
        #1) prepare data for one experiment
        x,cols=generateData(nObs,sLength,size0,size1,mu0,sigma0,sigma1F)
        r={i.__name__:pd.Series() for i in methods}
        #2) compute portfolios in sample
        for pointer in pointers:
            x_=x[pointer-sLength:pointer]
            cov_,corr_=np.cov(x_,rowvar=0),np.corrcoef(x_,rowvar=0)
            #3) compute performance out of sample
            x_=x[pointer:pointer+rebal]
            for func in methods:
                w_=func(cov=cov_,corr=corr_)#callback
                r_=pd.Series(np.dot(x_,w_))
                r[func.__name__]=r[func.__name__].append(r_)
            #4) Evaluate and store results
            for func in methods:
                r_=r[func.__name__].reset_index(drop=True)
                p_=(1+r_).cumprod()
                stats[func.__name__].loc[numIter]=p_.iloc[-1]-1
            numIter+=1
        #5) Report results
        stats=pd.DataFrame.from_dict(stats,orient='columns')
        stats.to_csv('stats.csv')
        df0,df1=stats.std(),stats.var()
        print(pd.concat([df0,df1,df1/df1['getHRP']-1],axis=1))
        return
#-------------------------------------
if __name__=='__main__':hrpMC()

                                     

            





















    

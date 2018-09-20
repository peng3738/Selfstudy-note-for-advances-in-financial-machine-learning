import pandas as pd
import numpy as np
from pandas import DataFrame
from numpy import *
from math import *
#------------------------------------
def getIndMatrix(barIx,t1):
    #Get indicator matrix
    indM = pd.DataFrame(0,index=barIx,columns=range(t1.shape[0]))
    for i,(t0,t1) in enumerate(t1.iteritems()):indM.loc[t0:t1,i]=1
    return indM


def getAvgUniqueness(indM):
    #Average uniqueness from indicator matirx
    c=indM.sum(axis=1)#concurrency
    u=indM.div(c,axis=0)#uniqueness
    avgU=u[u>0].mean()#average uniqueness
    return avgU


def seqBootstrap(indM,sLength=None):
    #Generate a sample via sequential bootstrap
    if sLength is None: sLength=indM.shape[1]
    phi=[]
    while len(phi)<sLength:
        avgU=pd.Series()
        for i in indM:
            indM_=indM[phi+[i]]#reduce indM
            avgU.loc[i]=getAvgUniqueness(indM_).iloc[-1]
        prob=avgU/avgU.sum()#draw prob
        phi+=[np.random.choice(indM.columns,p=prob)]
    return phi



def main():
    t1=pd.Series([2,3,5],index=[0,2,4])#t0,t1 for each feature obs
    barIx=range(t1.max()+1)#index of bars
    indM=getIndMatrix(barIx,t1)
    phi=np.random.choice(indM.columns,size=indM.shape[1])
    print(phi)
    print('Standard uniqueness:',getAvgUniqueness(indM[phi]).mean())
    phi=seqBootstrap(indM)
    print(phi)
    print('Sequential uniqueness:',getAvgUniqueness(indM[phi]).mean())
    return 



print('Standard uniqueness:'),getAvgUniqueness(indM[phi]).mean()
print('Sequential uniqueness:'),getAvgUniqueness(indM[phi]).mean()

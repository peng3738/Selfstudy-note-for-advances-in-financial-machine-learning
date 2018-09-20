import pandas as pd,numpy as np
#------------------------------------
def getIndMatirx(barIx,t1):
    #Get indicator matrix
    indM=pd.DataFrame(0,index=barIx,columns=range(t1.shape[0]))
    for i,(t0,t1) in enumerate(t1.iteritems()):indM.loc[t0:t1,i]=1.
    return indM

    

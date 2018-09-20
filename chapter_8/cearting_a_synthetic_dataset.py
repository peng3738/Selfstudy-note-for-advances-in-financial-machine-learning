def getTestData(n_features=40,n_informative=10,n_redundant=10,n_samples=10000):
    #generate a random dataset for a classficatio problem
    from sklearn.datasets import make_classification
    import pandas as pd
   # from pandas import DataFrame 
    trnsX,cont=make_classification(n_samples=n_samples,n_features=n_features,
                                   n_informative=n_informative,n_redundant=n_redundant,
                                   random_state=0,shuffle=False)
    df0=pd.DatetimeIndex(periods=n_samples,freq=pd.tseries.offsets.BDay(),\
                         end=pd.datetime.today())
    trnsX,cont=pd.DataFrame(trnsX,index=df0),pd.Series(cont,index=df0).to_frame('bin')
    df0=['I_'+str(i) for i in range(n_informative)]+\
         ['R_'+str(i) for i in range(n_redundant)]
    df0+=['N_'+str(i) for i in range(n_features-len(df0))]
    trnsX.columns=df0
    cont['w']=1./cont.shape[0]
    cont['t1']=pd.Series(cont.index,index=cont.index)
    return trnsX,cont


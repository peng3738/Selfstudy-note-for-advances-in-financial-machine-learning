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
        phi+=[np.random,choice(indM.columns,p=prob)]
    return phi

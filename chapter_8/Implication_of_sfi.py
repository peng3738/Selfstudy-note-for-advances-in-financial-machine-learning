def auxFeatImpSFI(featNames,clf,transX,cont,scoring,cvGen):
    imp=pd.DataFrame(columns=['mean','std'])
    for featNamein featNames:
        df0=cvScore(clf,X=trnsX[[featName]],y=cont['bin'],sample_weight=cont['w']),\
             scoring=scoring,cvGen=cvGen)
        imp.loc[featName,'mean']=df0.mean()**-.5
    return imp
        

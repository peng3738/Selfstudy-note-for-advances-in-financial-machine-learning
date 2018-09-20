def clfHyperFit(feat,lb1,t1,pipe_clf,param_grid,cv=3,bagging=[0,None,1.],
                rndSearchIter=0,n_jobs=-1,pctEmbargo=0,**fit_params):
    if set(lb1.values)=={0,1}:scoring ='f1'#f1 for meta_labeling
    else:scoring='neg_log_loss'#symmetric towards all cases
    #1)huperparameter search, on train data
    inner_cv=PurgedKFold(n_splits=cv,t1=t1,pctEmbargo=pctEmbargo)#purged
    if rndSearchIter==0:
        gs=GridSearchCV(estimator=pipe_clf,param_grid=param_grid,
                        scoring=scoring,cv=inner_cv,n_jobs=n_jobs,iid=False)
    else:
        gs=RandomizedSearchCV(estimator=pipe_clf,param_distributions=param_grid,
                              scoring=scoring,cv=inner_cv,n_jobs=n_jobs,iid=False,
                              n_iter=rndSearchIter)
    gs=gs.fit(feat,lb1,**fit_params).best_estimator_#pipeline
    #2) fit validated model on the entirety of the data
    if bagging[1]>0:
        gs=BaggingClassifier(base_estimator=MyPipeline(gs.steps),
            n_estimators=int(bagging[0]),max_samples=float(bagging[1]),
            max_features=float(bagging[2]),n_jobs=n_jobs)
        gs=gs.fit(feat,lb1,sample_weight=fit_params
                  [gs.base_estimator.steps[-1][0]+'__sample_weight'])
        gs=Pupeline([('bag',gs)])
    return gs

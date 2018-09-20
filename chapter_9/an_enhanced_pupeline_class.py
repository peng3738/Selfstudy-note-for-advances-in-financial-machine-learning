class MyPipeline(pipeline):
    def fit(self,X,y,sample_weight=None,**fit_params):
        if sample_weight is not None:
            fit_params[self.steps[-1][0],'_sample_weight']=sample_weight
        return super(MyPipeline,self).fit(X,y,**fit_params)
        

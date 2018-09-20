def getTrainTimes(t1,testTimes):
    '''
Given testTimes,find the times of the training observations.
t1.index: Time when the observation started.
t1.value: Time when the observation ended.
testTimes: Times of testing observations.
'''
    trn=t1.copy(deep=True)
    for i,j in testTimes.iteritems():
        df0=trn[(i<=trn.index)&(trn.index<=j)].index # train starts within test
        df1=trn[(i<=trn)&(trn.index<=j)].index#train ends within test
        df2=trn[(trn.index<=i)&(j<=trn)].index #train envelops test
        trn=trn.drop(df0.union(df1).union(df2))
    return trn

def getAvgUniqueness(indM):
    #Average uniqueness from indicator matirx
    c=indM.sum(axis=1)#concurrency
    u=indM.div(c,axis=0)#uniqueness
    avgU=u[u>0].mean()#average uniqueness
    return avgU

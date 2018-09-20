import pandas as pd,numpy as np
from mpEngine import processJobs,processJobs_
#----------------------------------------
def mainMC(numObs=10,numBars=100,maxH=5,numIters=1E6,numThreads=24):
    #Monte Carlo experiments
    jobs=[]
    for i in xrange(int(numIters)):
        job={'func':auxMC,'numObs':numObs,'numBars':numBars,'maxH':maxH}
        jobs.append(job)
    if numThreads==1:out=processsJobs_(jobs)
    else:out=processJobs(jobs,numThreads=numThreads)
    print(pd.DataFrame(out).describe())
    return

    

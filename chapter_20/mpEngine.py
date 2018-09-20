def mpPandasObj(func,pdObj,numThreads=24,mpBatches=1,linMols=True,**kargs):
    '''
Parallelize jobs, return a DataFrame or Series
+func: function to be parallelized. returns a DataFrame
+pdObj[0]: Name of argument used to pass the molecule
+pdObj[1]:list of atoms that will be grouped into molecules
+kargs:any other argument needed by func
Example:df1=myPandasObj(func,('molecule'.df0.index),24,**kargs)
'''
#-----------------------------------------------------
    import pandas as pd
    if linMols:parts=linParts(len(argList[1]),numThreads*mpBatches)
    else:parts=nestedParts(len(argList[1]),numThreads*mpBatches)
    jobs=[]
    for i in xrange(1,len(parts)):
        job={pdObj[0]:pdObj[1][parts[i-1]:parts[i]],'func':func}
        job.update(kargs)
        jobs.append(job)
    if numThreads==1:out=processJobs_(jobs)
    else:out=processJobs(jobs,numThreads=numThreads)
    if isinstance(out[0],pd.DataFrame):df0=pd.DataFrame()
    elif isinstance(out[0],pd.Series):df0=pd.Series()
    else:return out
    for i in out:df0=df0.append(i)
    df0=df0.sort_index()
    return df0
#---------------------------------

def processJobs_(jobs):
    #Run jobs sequentially, for debugging
    out=[]
    for job in jobs:
        out_=expandCall(job)
        out.append(out_)
        return out


import multiprocessing as mp
#-------------------------------
def reportProgress(jobNum,numJobs,time0,task):
    #Report progress as asynch jobs are completed
    msg=[float(jobNum)/numJobs,(time.time()-time0)/60.]
    msg.append(msg[1]*(1/msg[0]-1))
    timeStamp=str(dt.datetime.fromtimestamp(time.time()))
    msg=timeStamp+''+str(round(msg[0]*100,2))+'% '+task+' done after '+\
         str(round(msg[1],2))+' minutes.remaining '+str(round(msg[2],2))+' minutes.'
    if jobNum<numJobs:sys.stderr.write(msg+'\r')
    else:sys.stderr.write(msg+'\n')
    return

#-------------------------------------
def processJobs(jobs,task=None,numThreads=24):
    #Run in parallel
    #jobs must contain a 'func' callback, for expandcall
    if task is None:task=jobs[0]['func']._name_
    pool=mp.Pool(processes=numThreads)
    outputs,out,time0=pool.imap_unordered(expandCall,jobs),[],time.time()
    #Process asynchronous output. report progress
    for i,out_ in enumerate(outputs,1):
        out.append(out_)
        reportProgress(i,len(jobs),time0,task)
    pool.close();pool.join()#this is needed to prevent memory leaks
    return out

#----------------------------------
def expandCall(kargs):
    #Expand the arguments of a callback function,kargs['func']
    func=kargs['func']
    del kargs['func']
    out=func(**kargs)
    return out























    
    

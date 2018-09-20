def processJobsRedux(jobs,task=None,numThreads=24,redux=None,reduxArgs={},reduxInPlace=False):
    '''
run in parallel
jobs must contain a 'func'  callback for expandCall
redux prevents wasting memory by reducin output on the fly
'''
    if task is None:task=jobs[0]['func'].__name__
    pool=mp.Pool(processes=numThreads)
    imap,out,time0=pool.imap_unordered(expandCall,jobs),None,time.time()
    #Process asynchronous output,report progress
    for i,out_ in enimerate(imap,1):
        if out is None:
            if redux is None:out,redux,reduxInPlace=[out_],list.append,True
            else:out=copy.deepcopy(out_)
        else:
            if reduxInPlace:redux(out,out_,**reduxArgs)
            else:out=redux(out,out_,**reduxArgs)
        reportProgress(i,len(jobs),time0,task)
    pool.close();pool.join()# this is needed to prevent memory leaks
    if isinstance(out,(pd.Series,pd.DataFrame)):out=out.sort_index()
    return out


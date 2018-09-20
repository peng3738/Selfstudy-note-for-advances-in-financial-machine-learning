import numpy as np
import multiprocessing as mp
#--------------------------------
def main1():
    # path dependency: multi threaded implementation
    r, numThreads=np.random.normal(0,.01,size=(1000,10000)),24
    parts=np.linspace(0,r.shape[0],min(numThreads,r.shape[0])+1)
    parts,jobs=np.ceil(parts).astype(int),[]
    for i in range(1,len(parts)):
        jobs.append(r[:,parts[i-1]:parts[i]])# parallel jobs
    pool,out=mp.Pool(processes=numThreads),[]
    outputs=pool.imap_unordered(barrierTouch,jobs)
    for out_ in outputs: out.append(out_)# asynchronous respnse
    pool.close();pool.join()
    return

#-----------------
def barrierTouch(r,width=.5):
    #find the index of the earliest barrier touch
    t,p={},np.log((1+r).cumprod(axis=0))
    for j in range(r.shape[1]):# go through columns
        for i in range(r.shape[0]):# go through rows
            if p[i,j]>=width or p[i,j]<=-width:
                t[j]=i
                continue
    return t

#---------------------
if __name__=='__main__':
    import timeit
    print(min(timeit.Timer('main1()',setup='from __main__ import main1').repeat(5,10)))

    
        

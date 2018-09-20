pcs=mpJobList(getPCs,('molecules',fileNames),numThreads=24,mpBatches=1,
              path=path,eVec=eVec,redux=pd.DataFrame.add)
#---------------------
def getPCs(path,molecules,eVec):
    # get principal omponents by loading one file at a time
    pcs=None
    for i in molecules:
        df0=pd.read_csv(path+i,index_col=0,parse_dates=True)
        if pcs is None:pcs=np.dot(df0.values,eVec.loc[df0.columns].values)
        else:pcs+=np.dot(df0.values,eVec.loc[df0.columns].values)
    pcs=pd.DataGrame(pcs,index=df0.index,columns=eVec.columns)
    return pcs

    

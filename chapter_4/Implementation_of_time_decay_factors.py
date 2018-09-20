def getTimeDecay(tW,clfLastW=1.):
    #apply piecewise-linear decay to observed uniqueness (tW)
    #newest observation gets weight=1,oldest observation gets weight=clfLastW
    clfW=tW.sort_index().cumsum()
    if clfLastW>=0:slope=(1.-clfLastW)/clfW.iloc[-1]
    else:slope=1./((clfLastW+1)*clfW.iloc[-1])
    const=1.-slope*clfW.iloc[-1]
    clfW=const+slope*clfW
    clfW[ckfW<0]=0
    print const,slope
    return clfW

def plotFeatImportance(pathOut,imp,oob,oos,method,tag=0,simNum=0,**kargs):
    #plot mean imp bars with std
    import matplotlib as mpl
    mpl.figure(figsize=(10,imp.shape[0]/5.))
    imp=imp.sort_values('mean',ascending=True)
    ax=imp['mean'].plot(kind='barh',color='b',alpha=.25,xerr=imp['std'],
                        error_kw={'ecolor':'r'})
    if method=='MDI':
        mpl.xlim([0,imp.sum(axis=1).max()])
        mpl.axvline(1./imp.shape[0],linewidth=1,color='r',linestyle='dotted')
    ax.get_yaxis().set_visible(False)
    for i,j in zip(ax.patches,imp.index):ax.text(i.get_width()/2,i.get_y()+
                   i.get_height()/2,j,ha='center',va='center',color='black')
    mpl.title=('tag='+tag+'|simNum='+str(simNum)+'|oob='+str(round(oob,4))+
               '|oos='+str(round(oos,4)))
    mpl.savefig(pathOut+'featImportance_'+str(simNum)+'.png',dpi=100)
    mpl.clf();mpl.close()
    return

def getQuasiDiag(link):
    #sort clustered items by distance
    link=link.astype(int)
    sortIx=pd.Series([link[-1,0],link[-1,1]])
    numItems=link[-1,3]#number of original items
    while sortIx.max()>=numItems:
        sortIx.index=range(0,sortIx.shape[0]*2,2)#make space
        df0=sortIx(sortIx>=numItems)#find clusters
        i=df0.index;j=df0.values-numItems
        sortIx[i]=link[j,0]#item 1
        df0=pd.Series(link[j,1],index=i+1)
        sortIx=sortIx.append(df0)#item s
        sortIx=sortIx.sort_index()# re-sort
        sortIx.index=range(sortIx.shape[0])#re-index
        return sortIx.tolist()
    

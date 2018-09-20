def betSize(w,x):
    return x*(w+x**2)**-.5

#---------------------------------
def getTPos(w,f,mP,maxPos):
    return int(betSize(w,f-mP)*maxPos)

#------------------------------
def invPrice(f,w,m):
    return f-m*(w/(1-m**2))**.5
#----------------------------
def limitPrice(tPos,pos,f,w,maxPos):
    sgn=(1 if tPos>=pos else -1)
    lP=0
    for j=in range(abs(pos+sgn),abs(tPos+1)):
        lP+=invPrice(f,w,j/float(maxPos))
    lP/=tPos-pos
    return lP
#----------------------
deg getW(x,m):
    #0<alpha<1
    return x**2*(m**-2-1)

#------------------------
def main():
    pos,maxPos,mP,f,wParams=0,100,100,115,{'divergence':10,'m':.95}
    w=getW(wParams['divergence'],wParams['m'])# calibrate w
    tPos=getTPos(w,f,mP,maxPos)# get tPos
    lP=limitPrice(tPos,pos,f,w,maxPos) # limit price for order
    return

#--------------------
if __name__=='__main__':main()



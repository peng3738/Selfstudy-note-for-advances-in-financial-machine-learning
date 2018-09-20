def matchLength(msg,i,n):
    #Maximum matched length +1, with overlap
    # i>=n & len(msg)>=i+n
    subS=''
    for l in xrange(n):
        msg1=msg[i:i+l+1]
        for j in xrange(i-n,i):
            msg0=msg[j:j+l+1]
            if msg1==msg0:
                subS=msg1
                break # search for higher 1
    return len(subS)+1,subS # matched length+1


#---------------------------------------

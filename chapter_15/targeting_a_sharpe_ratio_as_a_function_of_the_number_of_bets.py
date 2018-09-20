import numpy as np
out,p=[],.55
for i in range(1000000):
    rnd=np.random.binomial(n=1,p=p)
    x=(1 if rnd==1 else -1)
    out.append(x)
print(np.mean(out),np.std(out),np.mean(out)/np.std(out))

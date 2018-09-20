from scipy.special import comb
N,p,k=100,1./3,3.
p_=0
for i in range(0,int(N/k)+1):
    p_+=comb(N,i)*p**i*(1-p)**(N-i)
print(p,1-p_)



  def main():
        import numpy as np
        import CLA
        #1) Path
        path='H:/PROJECTS/Data/CLA_Data.csv'
        #2) Load data, set seed
        headers=open(path,'r').readline().split(',')[:-1]
        data=np.genfromtxt(path,delimiter=',',skip_header=1) # load as numpy array
        mean=np.array(data[:1]).T
        lB=np.array(data[1:2]).T
        uB=np.array(data[2:3]).T
        covar=np.array(data[3:])
        #3) Invoke object
        cla=CLA.CLA(mean,covar,lB,uB)
        cla.solve()
        print(cla.w) # print all turning points
        #4) Plot frontier
        mu,sigma,weights=cla.efFrontier(100)
        plot2D(sigma, mu, 'Risk', 'Expected Excess Return', 'CLA-derived Efficient Frontier')
        #5) Get Maximum Sharpe ratio portfolio
        sr,w_sr = cla.getMaxSR()
        print(np.dot(np.dot(w_sr.T, cla.covar), w_sr)[0, 0]**.5, sr)
        print(w_sr)
        #6) Get Minimum Variance portfolio
        mv, w_mv = cla.getMinVar()
        print(mv)
        print (w_mv)
        return
        #---------------------------------------------------------------
    # Boilerplate
    if __name__ == '__main__':main()
    #----------------------------------------------------
    #____________________________________________________-
    def plot2D(x, y, xLabel = '', yLabel = '', title = '', pathChart = None):
        import matplotlib.pyplot as mpl
        fig = mpl.figure()
        ax = fig.add_subplot(1, 1, 1) # one row, one column, first plot
        ax.plot(x, y, color = 'blue')
        ax.set_xlabel(xLabel)
        ax.set_ylabel(yLabel, rotation = 90)
        mpl.xticks(rotation = 'vertical')
        mpl.title(title)
        if pathChart == None:
            mpl.show()
        else:
            mpl.savefig(pathChart)
        mpl.clf() # reset pylab
        return

'''
     #5) compute solution vector
    wF, g = self.computeW(covarF_inv, covarFB, meanF, wB)
    for i in range(len(f)):w[f[i]] = wF[i]
    self.w.append(np.copy(w)) # store solution
    self.g.append(g)
    self.f.append(f[:])
    if self.l[-1]==0:break

   '''
    #----------------------
    '''
    
        #4) decide lambda
        if l_in > l_out:
            self.l.append(l_in)
            f.remove(i_in)
            w[i_in] = bi_in # set value at the correct boundary
        else:
            self.l.append(l_out)
            f.append(i_out)
        covarF, covarFB, meanF, wB = self.getMatrices(f)
        covarF_inv = np.linalg.inv(covarF)

         #1) case a): Bound one free weight
        l_in = None
        if len(f) > 1:
            covarF, covarFB, meanF, wB = self.getMatrices(f)
            covarF_inv = np.linalg.inv(covarF)
            j = 0
            for i in f:
                l, bi = self.computeLambda(covarF_inv, covarFB, meanF, wB, j, [self.lB[i], self.uB[i]])
                if l > l_in:l_in, i_in, bi_in = l, i, bi
                j += 1
    

'''
#---------------------------------------
  '''  if (l_in == None or l_in < 0) and (l_out == None or l_out < 0):
        #3) compute minimum variance solution
        self.l.append(0)
        covarF, covarFB, meanF, wB = self.getMatrices(f)
        covarF_inv = np.linalg.inv(covarF)
        meanF = np.zeros(meanF.shape)
'''

import numpy as np
from scipy.stats import weightedtau
featImp=np.array([.55,.33,.07,.05])#feature importance
pcRank=np.array([1,2,4,3])#PCA rank
weightedtau(featImp,pcRank**-1.)[0]

import scipy.cluster.hierarchy as sch
import numpy as np
import pandas as pd
cov,corr=x.cov(),x.corr()
dist=((1-corr)/2.)**.5 #distance matrix
link=sch.linkage(dist,'single')#linkage matrix

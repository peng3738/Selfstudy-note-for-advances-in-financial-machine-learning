#cartesian poduct of dictionary of lists
dict0={'a':['1','2'],'b':['+','*'],'c':['!','@']}
for a in dict0['a']:
    for b in dict0['b']:
        for c in dict0['c']:
            print({'a':a,'b':b,'c':c})


#----------------------------
# cartesian product of dictionary of lists
from itertools import product
dict0={'a':['1','2'],'b':['+','*'],'c':['!','@']}
jobs=(dict(zip(dict0,i)) for i in product(*dict0.values()))
for i in jobs:print(i)
    

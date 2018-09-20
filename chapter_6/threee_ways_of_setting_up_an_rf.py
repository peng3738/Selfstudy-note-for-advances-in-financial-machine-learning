from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

max_samples=out['tW'].mean().


clf0=RandomForestClassifier(n_estimators=1000,class_weight='balanced_subsample',\
                            criterion='entropy')
clf1=DecisionTreeClassifier(criterion='entropy',max_features='auto',class_weight='balanced')
clf1=BaggingClassifier(base_estimator=clf1,n_estimators=1000,max_samples=avgU)
clf2=RandomForestClassifier(n_estimators=1,criterion='entropy',bootstrap=False,\
                            class_weight='balanced_subsample')
clf2=BaggingClassifier(base_estimator=clf2,n_estimators=1000,max_samples=avgU,\
                       max_features=1.)

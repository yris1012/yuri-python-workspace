import numpy as np
import pickle

dic = {'apple':0, 'banana':1, 'orange':2}
f = open('/Users/yuri/sophia/YuriPythonWorkspace/YuriPythonProject7/dic.pickle', 'wb')
pickle.dump(dic, f)
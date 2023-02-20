import numpy as np
import BadParameterError

class PyMultiMap:
    
    def __init__(self):
        self.classdict = {}
        self.sizeOfMulitMap = 0

    def __str__(self):
        return self.classdict

    def put(self,key,values):
        if isinstance(values,list) == False and isinstance(values,np.ndarray) == False:
            raise Exception("List or Array") #BadParameterError #("Second parameter has to be a list or a numpy-array !")
        if isinstance(values,np.ndarray):
            self.classdict[key] = values 
        else:
            self.classdict[key] = np.array(values)  
        self.sizeOfMulitMap = self.sizeOfMulitMap + 1

    def get(self,key):
        return self.classdict[key]

    def getAsAList(self,key):
        return self.classdict[key].tolist()

    def remove(self, key):
        self.classdict.pop(key)
        if len(self.classdict) >= 1:
            self.sizeOfMulitMap = self.sizeOfMulitMap - 1

    def size(self):
        return self.sizeOfMulitMap
    
    def clear(self):
        self.classdict.clear()
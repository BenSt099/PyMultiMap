import numpy as np

class PyMultiMap:
    
    def __init__(self):
        self.classdict = {}
        self.sizeOfMulitMap = 0

    def __str__(self):
        return  f"{self.classdict}" 

    def put(self,key,values):
        if isinstance(values,list) == False and isinstance(values,np.ndarray) == False:
           raise ValueError("Values have to be in a List Or an NumPy-Array!")  
        if isinstance(values,np.ndarray):
            self.classdict[key] = values 
        else:
            self.classdict[key] = np.array(values)  
        self.sizeOfMulitMap = self.sizeOfMulitMap + 1

    def get(self,key):
        try:
            return self.classdict[key]
        except KeyError:
            return None

    def getAsAList(self,key):
        try:
            return self.classdict[key].tolist()
        except KeyError:
            return None

    def update(self,key,values):
        if isinstance(values,list) == False and isinstance(values,np.ndarray) == False:
           raise Exception("Values have to be in a List Or an NumPy-Array!")  
        if isinstance(values,np.ndarray):
            self.classdict.update({key : values})
        else:
            self.classdict.update({key : np.array(values)})

    def copy(self):
        return self.classdict.copy()

    def keys(self):
        if self.size() == 0:
            return None
        return self.classdict.keys()

    def values(self):
        if self.size() == 0:
            return None
        return self.classdict.values()

    def remove(self, key):
        self.classdict.pop(key)
        if len(self.classdict) >= 1:
            self.sizeOfMulitMap = self.sizeOfMulitMap - 1

    def size(self):
        return self.sizeOfMulitMap
    
    def clear(self):
        self.sizeOfMulitMap = 0
        self.classdict.clear()
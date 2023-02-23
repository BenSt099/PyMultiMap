import sys
import numpy as np
 
sys.path.append('../src/')

from main.PyMultiMap import * 

def test_0201():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    assert pmmobj.__str__() != False

def test_0202():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    pmmCopy = pmmobj.copy()
    assert pmmobj.__str__() == pmmCopy.__str__()

def test_0203():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    pmmobj.put("key2",[4,5,6])
    assert len(pmmobj.values()) == 2

def test_0204():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    pmmobj.put("key2",[4,5,6])
    pmmobj.remove("key2")
    assert pmmobj.size() == 1

def test_0205():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    pmmobj.put("key2",[4,5,6])
    pmmobj.update("key2",np.array([5,6,7]))
    assert list(pmmobj.get("key2")) == list(np.array([5,6,7]))

def test_0206():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    assert pmmobj.get("key2") == None
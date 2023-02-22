import sys
import pytest
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
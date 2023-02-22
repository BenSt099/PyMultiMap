import sys
import pytest
 
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
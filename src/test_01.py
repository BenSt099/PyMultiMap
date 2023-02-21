from main.PyMultiMap import * 
import pytest

def test_0101():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    assert pmmobj.getAsAList("key1") == [1,2,3]

def test_0102():
    pmmobj = PyMultiMap()
    with pytest.raises(ValueError):
        pmmobj.put("key1",1)

def test_0103():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    pmmobj.clear()
    assert pmmobj.size() == 0

def test_0104():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    pmmobj.clear()
    assert pmmobj.getAsAList("key1") == None

def test_0105():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    assert pmmobj.size() == 1

def test_0106():
    pmmobj = PyMultiMap()
    assert pmmobj.keys() == None
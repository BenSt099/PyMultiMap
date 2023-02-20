from PyMultiMap import * 

def testMM():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    assert pmmobj.getAsAList("key1") == [1,2,3]

testMM()
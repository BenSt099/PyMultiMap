from PyMultiMap import * 

def testMM():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    assert pmmobj.getAsAList("key1") == [1,2,3]

def testMM2():
    pmmobj = PyMultiMap()
    try:
        pmmobj.put("key1",1)
    except Exception:
        print("Bad Param Error raised")

def testMM3():
    pmmobj = PyMultiMap()
    pmmobj.put("key1",[1,2,3])
    pmmobj.put("key2",[1,4,3])
    pmmobj.put("key3",[1,8,3])
    print(pmmobj)


testMM()
testMM2()
testMM3()
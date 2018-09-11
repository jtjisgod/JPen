import JThread      # Simple Thread Module
import time

"""
    [ Usage ]
    JTest.testAttack(print, [1,2,3,4])
"""

# Time Test
def testAttack(func, params, count=10) :
    startTime = time.time()
    jThread = JThread.JThread(func, params, count=count)
    jThread.run()
    threadTime = time.time() - startTime
    startTime = time.time()
    for param in params :
        func(param)
    print(func)
    print("Thread Time\t : ", threadTime)
    print("Loop Time\t : ", time.time() - startTime)


def testFunc(param) :
    return (int(param) * 10)/2.3
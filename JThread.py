import os
import json
import copy
from threading import Thread

"""

    [ What ]
    This is JTJ's Thread Module.

    [ Usage ]
    JThread(func, params, count=10).run().getResponse()

"""

class JThread :

    def __init__(self, func, params, count=10) :
        self.params = copy.deepcopy(params)
        self.func = func
        self.response = {}
        self.count = count
    
    def run(self) :
        threads = []
        for i in range(0, self.count) :
            threads.append(Thread(target=self.threadFunc))
        for thread in threads :
            thread.start()
        for thread in threads :
            thread.join()
        return self
            
    def threadFunc(self) :
        while True :
            if len(self.params) == 0 :
                break
            try : param = self.params.pop()
            except : break
            self.response[str(param)] = self.func(param)
    
    def getResponse(self) :
        return self.response
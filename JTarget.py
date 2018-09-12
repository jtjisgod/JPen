import os
import JEnum
import pickle
import time

class JTarget :

    def __init__(self, domain, initType=0) :
        if initType == 0 :
            self.binFile = JEnum.targets + domain + ".bin"
        else :
            self.binFile = domain
        if not os.path.exists(self.binFile) :
            f = open(self.binFile, "wb")
            pickle.dump({
                "domain" : domain,
                "createTime" : time.time()
            }, f)
            f.close()
        f = open(self.binFile, "rb")
        self.target = pickle.load(f)
        f.close()
    
    def commit(self) :
        print(self.binFile)
        f = open(self.binFile, "wb")
        pickle.dump(self.target, f)
        f.close()

    def element(self, name, contents=None) :
        if contents == None :
            return self.getter(name)
        else :
            self.setter(name, contents)
        
    def getter(self, name) :
        return self.target[name]
    
    def setter(self, name, contents) :
        self.target[name] = contents
        self.commit()
    
    def remove(self) :
        return os.remove(self.binFile)
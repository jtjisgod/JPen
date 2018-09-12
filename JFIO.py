import os
import pickle

def readFile(filename) :
    f = open(filename, "r")
    ret = f.read()
    f.close()
    return ret

def readFile2Line(filename) :
    return readFile(filename).split("\n")

def getFileList(directory, nameFilter=lambda x: True) :
    lists = []
    for d in os.scandir(directory) :
        if nameFilter(d.name) :
            lists.append(directory + "/" + d.name)
    return lists

def readPickle(filename) :
    f = open(filename, "rb")
    p = pickle.load(f)
    f.close()
    return p



def readFile(filename) :
    f = open(filename, "r")
    ret = f.read()
    f.close()
    return ret

def readFile2Line(filename) :
    return readFile(filename).split("\n")
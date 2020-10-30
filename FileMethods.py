def openFile(fname,mode):
   file = open(fname,mode)
   return file
    
def readFile(fobj,c=0):
    if c==0:
            data = fobj.read()
    else:
            data = fobj.read(c)
    return data


def readLines(fobj):
    data = fobj.readlines()
    return data
        
def writeFile(fobj, data):
    for line in data:
        fobj.write(line)
    fobj.close()
    

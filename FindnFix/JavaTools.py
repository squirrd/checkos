import zipfile
from StringIO import StringIO



def readFile(jarFile, file):
    aJar = zipfile.ZipFile(jarFile, 'r')
    sio = StringIO()
    sio.write(aJar.read(file))
    return (sio.getvalue())
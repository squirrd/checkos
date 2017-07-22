import os

def dirs(searchRoots, searchDirs, excludeDirs=[]):
    searchResults = []
    for searchRootName, searchRoot in searchRoots:
        for walkRoot, walkDirs, walkFiles in os.walk(searchRoot):
            if any(exDir in walkRoot for exDir in excludeDirs):
                continue
            for searchDir in searchDirs:
                # print('{0} - {1} : {2} - {3}'.format(searchRoot,searchDir, walkRoot, searchDir))
                if searchDir in walkDirs:
                    searchResults.append((searchRoot, searchDir, walkRoot))
    return searchResults

def files(searchRoots, searchFiles, excludeDirs=[]):
    searchResults = []
    for searchRootName, searchRoot in searchRoots:
        for walkRoot, walkDirs, walkFiles in os.walk(searchRoot):
            if any(exDir in walkRoot for exDir in excludeDirs):
                continue
            for walkFile in walkFiles:
                if walkFile in searchFiles:
                    searchResults.append((searchRoot, walkFile, walkRoot))
    return searchResults
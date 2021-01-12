import pickle
from os.path import isfile
from typing import Sequence


def str_2_XYZ(line: str) -> Sequence[float]:
    terms = line.split()
    coords = []
    # print(terms[-3:])
    for text in terms[-3:]:
        coords.append(float(text))
    # print(coords)
    return tuple(coords)


class stl_reader_2():
    FACEBEGIN = 'outer loop'
    FACEEND = 'endloop'
    VXPREFIX = 'vertex'
    ENDSOLID = 'endsolid'

    def __init__(self, filename: str):
        if isfile(filename):
            self.filename = filename
            print(f'file {filename} is found')
        else:
            raise FileExistsError

    def __iter__(self):
        self.stlFile = open(self.filename, 'r', encoding='UTF-8')
        solidName = self.stlFile.readline()
        self.bodyName = solidName[6:]
        self.nFaces = 0
        return self

    def __next__(self):
        faceVXlist = []
        while True:
            line = self.stlFile.readline()
            line = line.strip()
            if not line:
                self.stlFile.close()
                raise StopIteration
            if line.count(self.VXPREFIX):
                # print(line)
                faceVXlist.append(str_2_XYZ(line))
                continue
            if line.count(self.FACEBEGIN):
                faceVXlist = []
                continue
            if line.count(self.FACEEND):
                self.nFaces += 1
                # print(self.nFaces)
                return faceVXlist


class stl_reader_1():
    FACEBEGIN = 'outer loop'
    FACEEND = 'endloop'
    VXPREFIX = 'vertex'
    ENDSOLID = 'endsolid'

    def __init__(self, filename: str):
        if isfile(filename):
            self.filename = filename
            print(f'file {filename} is found')
        else:
            raise FileExistsError

    def __iter__(self):
        # self.stlFile = open(self.filename, 'r', encoding='UTF-8')
        with open(self.filename, 'r', encoding='UTF-8') as stlFile:
            self.filetext = stlFile.readlines()
        # solidName = self.filetext
        # self.bodyName = solidName[6:]
        self.nFaces = 0
        return self

    def __next__(self):
        faceVXlist = []
        for line in self.filetext:
            line = line.strip()
            if not line:
                raise StopIteration
            if line.count(self.VXPREFIX):
                # print(line)
                faceVXlist.append(str_2_XYZ(line))
                continue
            if line.count(self.FACEBEGIN):
                faceVXlist = []
                continue
            if line.count(self.FACEEND):
                self.nFaces += 1
                # print(self.nFaces)
                return faceVXlist


def test_read(name: str):
    stl = open(name, encoding='utf-8')
    for line in stl.readlines():
        print(line)


def pickleWrite(fileName: str, a: object):
    if isfile(fileName):
        print(f"File \"{fileName}\" already exists. \nIt will be overwritten")
    with open(file=fileName, mode='wb') as f:
        pickle.dump(a, f)

def pickleRead(fileName: str) -> object:
    if not isfile(fileName):
        print(f"File {fileName} not found")
        raise FileExistsError
    with open(file=fileName, mode='rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    # line1 = 'vertex 0.000000e+000 4.600000e+001 0.000000e+000'
    # line2 = 'facet normal -7.071068e-001 7.071068e-001 0.000000e+000'
    # vx1 = ['vertex 4.000000e+000 5.000000e+001 0.000000e+000',
    #        'vertex 0.000000e+000 4.600000e+001 0.000000e+000',
    #        'vertex 4.000000e+000 5.000000e+001 4.000000e+000']
    # print(str_2_XYZ(line2))
    # for line in vx1:
    #     print(str_2_XYZ(line))

    stlFile = 'LK1-002.01c.STL'

    reader = stl_reader_2(filename=stlFile)
    it = iter(reader)
    # print(reader)
    for vxcoords in it:
        print(vxcoords)
    # test_read(stlFile)

#!/usr/bin/python
'this module contains different functions of matrix'


class Matrix(object):
    """the class of matrix"""
    def __init__(self, m=2, n=2, v=0):
        if isinstance(m, (int, float)) and isinstance(n, (int, float)):
            self.rowNum = m
            self.colNum = n
            self.mat = createMat(self.rowNum, self.colNum, v)
        if isinstance(m, list):
            self.rowNum = len(m)
            for item in range(self.rowNum):
                if not isinstance(m[item], list):
                    print 'the argument must be a 2D list'
                    self.mat=[[]]
                    return None
            self.colNum = len(m[0])
            for item in range(self.rowNum):
                if len(m[item]) is not self.colNum:
                    print 'the length of the list must be the same'
                    self.mat=[[]]
                    return None
            self.mat = m

    def __str__(self):
        s = ''
        for i in range(self.rowNum):
            for j in range(self.colNum):
                s=s + str(self[i][j]) + '\t'
            s += '\n'
        s = s[:-1]
        return s
    __repr__ = __str__

    def __add__(self, obj):
        retmat = Matrix(self.rowNum, self.colNum)
        if isinstance(obj, (int, float)):
            return self + Matrix(self.rowNum, self.colNum, obj)
        if isinstance(obj, Matrix) and (obj.rowNum == self.rowNum) and (obj.rowNum == self.rowNum):
            for i in range(self.rowNum):
                for j in range(self.colNum):
                    retmat[i][j] = self[i][j] + obj[i][j]
            return retmat
        else:
            print 'error: the type of adder is wrong.'
            return None

    def __mul__(self, obj):
        retmat = Matrix(self.rowNum, obj.colNum)
        if isinstance(obj, Matrix) and self.colNum == obj.rowNum:
            for i in range(self.rowNum):
                for j in range(obj.colNum):
                    for k in range(self.colNum):
                        retmat[i][j] += self[i][k] * obj[k][j]
            return retmat
        else:
            print 'error:the type of matrix is wrong.'
            return None

    def __call__(self, x, y):
        return self[x][y]

    def __getitem__(self, ind):
        return self.mat[ind]

    def transpose(self):
        'calculate the transposed matrix of self'
        return Matrix([list(x) for x in zip(*self.mat)])


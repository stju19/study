#! /usr/bin/python
"different kinds of functions in exercises from the book Python Core Programming"

from math import sqrt

def isLeapYear(year):
    "judge whether the year is leap year or not,exercise 5-4"
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False

def createRandomList():
    "create a list that have N random numbers,exercise 5-17"
    import random
    N=random.randint(0,100)
    randomList = []
    item = 0
    while item < N:
        randomList.append(random.randint(0,2**31-1))
        item+=1
    return randomList

def calGCD(a, b):
    'calculate the greatest common divisor of a and b,exercise 5-15'
    while b:
        t = a % b
        a = b
        b = t
    return a

def calLCM(a,b):
    'calculate the lowest common multiple of a and b,exercise 5-15'
    return a * b / calGCD(a, b)

def rot13(s):
    'the rot13 encryption, exercise 7-10'
    sl = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sh = 'nopqrstuvWxyzabcedfghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    rotdict=dict(zip(sl,sh))
    retstr = ''
    for i in range(len(s)):
        if s[i] in rotdict.keys():
            retstr += rotdict[s[i]]
        else:
            retstr += s[i]
    return retstr

def convertNumberToEnglish(num):
    "Given a number, return an English string that can explain the number, exercise 6-8"
    engNum = ('zero','one','two','three','four','five','six','seven','eight','nine')
    engStr = ''
    numstr = str(num)
    for item in numstr:
        engStr += engNum[int(item)] + '-'
    engStr = engStr[:-1]
    return engStr

def convertAlpha(str):
    "Given a string of alphas, return its convertion between upper and lower alphas, exercise 6-10"
    for item in str:
        if str[item].islower():
            str[item] = str[item].upper()
        else:
            str[item] = str[item].lower()
    return str

def convertString(str):
    "Given a string, return its convertion between upper and lower alphas, exercise 6-10"
    for item in str:
        if str[item].isalpha():
           convertAlpha(str[item])

def safe_input(str = ''):
    'addaption from raw_input(), has exceptions for KeyboardInterrupt and EOFError, exercise 10-8'
    try:
        retstr = raw_input(str)
    except (EOFError, KeyboardInterrupt), mesg:
        retstr = none
        print '\nError: ' , mesg.__doc__
    return retstr

def factorial(n):
    'calculate the factorial of number n,exercise 11-13'
    try:
        if not isinstance(n, int):
            raise TypeError, "TypeError:the argument must be a interger"
    except TypeError, mesg:
        print mesg
        return None
    if n in [0, 1]:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n+1))

def calcFibonacci(n):
    'calulate the value of fibonacci sequence by recurion, exercise 11-14'
    if n in [0, 1]:
        return 1
    else:
        return calcFibonacci(n-1)+calcFibonacci(n-2)

def fibonacci(n = 10):
    'show the fibonacci sequence, exercise 11-14'
    retstr = ''
    for i in range(n):
        retstr += str(calcFibonacci(i)) + ', '
    retstr = retstr[:-2]
    return retstr

class Point(object):
    'this class describe a point at the plane rectangular coordinates,exercise 13-5'
    def __init__(self, x = 0, y = 0):
        if isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        elif isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        elif isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
    def __str__(self):
        return str((self.x, self.y))
    __repr__ = __str__

class LineSegment(object):
    'the class of line segment, exercise 13-6'
    def __init__(self, a, b):
        self.pa = Point(a)
        self.pb = Point(b)
    def __str__(self):
        return str(self.pa) + ', ' + str(self.pb)
    __repr__ = __str__
    def length(self):
        return sqrt((float(self.pa.x - self.pb.x))**2+(float(self.pa.y - self.pb.y))**2)
    def sloap(self):
        deltax = float(self.pa.x - self.pb.x)
        deltay = float(self.pa.y - self.pb.y)
        if deltax == 0:
            print 'the line segment sloap is infinite.'
            return None
        else:
            return deltay / deltax
    __abs__ = length

class Time60(object):
    "exercise 13-20"
    def __init__(self, obj = 0, min = 0):
        ""
        if isinstance(obj, int):
            self.hr = obj
            self.min = min
        elif isinstance(obj, tuple):
            self.hr = obj[0]
            self.min = obj[1]
        elif isinstance(obj, dict):
            self.hr = obj['hr']
            self.min = obj['min']
        elif isinstance(obj, str):
            colonIndex=obj.find(':')
            self.hr = int(obj[:colonIndex])
            self.min = int(obj[colonIndex+1:])
    def update(self):
        self.hr += self.min / 60
        self.min %= 60
    def __str__(self):
        ""
        self.update()
        return "%02d:%02d" % (self.hr, self.min)
    __repr__ = __str__
    def __add__(self, other):
        "addition for Time60"
        return self.__class__(self.hr + other.hr, self.min + other.min)
    def __iadd__(self, other):
        "in-situ addtion for Time60"
        self.hr += other.hr
        self.min += other.min
        return self
    def __call__(self):
        ""
        print "i'm callable"

def main():
    'the main function.'
    print 'hello!'
    pass

if __name__ == "__main__":
    main()


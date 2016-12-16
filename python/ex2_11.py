#!/usr/bin/python
#still have bug,can't input character

def getNum():
    "get a number from the user"
    while True:
        num = int(raw_input("Please enter a number from 1 to 100:"))
        if 0 < num < 101:
            return num
        else:
            print "The number must be between 0 and 100!\n"

def get5Num():
    "continuously get 5 numbers from the user"
    totalNum=[0,0,0,0,0]
    for item in range(5):
        totalNum[item]=getNum()
    return totalNum

def calNumSum(totalNum):
    "calculate the sum of numbers from the argument"
    sum=0
    for item in range(len(totalNum)):
        sum += totalNum[item]
    return sum

def calNumAverage(totalNum):
    "calculate the average of numbers from the argument"
    sum = calNumSum(totalNum)
    average = sum / len(totalNum)
    return average

def isSame(sur,dest):
    "judge that whether the two value is the same or not"
    if sur == dest:
        return True
    else:
        return False

def getUserChioce():
    "show the chioces that the user can operate to the standard output"
    print "(1) get sum of 5 numbers\n" , "(2) get average of 5 numbers\n" , "(x) Exit"
    return raw_input()

def main():
    while True:
        chioce=getUserChioce()
        if isSame(int(chioce) , 1):
            totalNum = get5Num()
            print "the sum is : " , calNumSum(totalNum)
        elif isSame(int(chioce) , 2):
            totalNum = get5Num()
            print "the average is : " , calNumAverage(totalNum)
        elif isSame(chioce , 'x') or isSame(chioce , 'X'):
            print "Exit."
            break

if __name__ == '__main__':
    main()


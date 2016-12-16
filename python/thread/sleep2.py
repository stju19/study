#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4,2]
def loop2():
    print 'start loop2', 'at:', ctime()
    sleep(2)
    print 'loop2', 'done at:', ctime()

def loop4():
    print 'start loop4', 'at:', ctime()
    sleep(4)
    print 'loop4', 'done at:', ctime()

def main(): 
    print 'starting at:', ctime()
    thread2=threading.Thread(target=loop2,args=())
    thread4=threading.Thread(target=loop4,args=())
    
    # thread4.setDaemon(True)
    
    thread2.start()
    thread4.start()
    
    thread2.join()
    thread4.join()
    
    print 'all DONE at:', ctime() 

if __name__ == '__main__':
    main()
        
    


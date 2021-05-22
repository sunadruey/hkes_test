import logging
import time
import logging
import _thread

import threading
logging.basicConfig(level=logging.INFO)

loops=[2,4]

def loop(nloop,nsec):

    print("loop  start all at "+"loop" +str(nloop) + " " + time.ctime())
    time.sleep(nsec)
    print("loop end  all at "+"loop" + str(nloop)  + " "+ time.ctime())



def main():
    logging.info('start all at' + time.ctime())
    threads=[]
    nloops=range(len(loops))

    for i in nloops:

       t = threading.Thread(target=loop,args=(i,loops[i]))
       threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    logging.info('end  all at' + time.ctime())



if __name__ == '__main__':
    main()
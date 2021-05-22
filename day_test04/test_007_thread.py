import logging
import time
import logging
import _thread

logging.basicConfig(level=logging.INFO)

loops=[2,4]
def loop(nloop,nsec,lock):

    print("loop  start all at "+"loop" +str(nloop) + " " + time.ctime())
    time.sleep(nsec)
    print("loop end  all at "+"loop" + str(nloop)  + " "+ time.ctime())
    lock.release()


def main():
    logging.info('start all at' + time.ctime())
    locks =[]
    nloops=range(len(loops))

    for i in nloops:
        lock= _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))

    for i in nloops:
        while locks[i].locked():pass

    time.sleep(6)
    logging.info('end  all at' + time.ctime())



if __name__ == '__main__':
    main()
import logging
import time
import logging
import _thread

import threading
logging.basicConfig(level=logging.INFO)

loops=[2,4]


class MyTread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func =func
        self.args = args
        self.name=name


    def run(self):
        self.func(*self.args)
def loop(nloop,nsec):

    print("loop  start all at "+"loop" +str(nloop) + " " + time.ctime())
    time.sleep(nsec)
    print("loop end  all at "+"loop" + str(nloop)  + " "+ time.ctime())



def main():
    logging.info('start all at' + time.ctime())
    threads=[]
    nloops=range(len(loops))

    for i in nloops:

       t = MyTread(loop,(i,loops[i]),loop.__name__)
       threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    logging.info('end  all at' + time.ctime())



if __name__ == '__main__':
    main()
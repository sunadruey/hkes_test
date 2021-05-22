import logging
import time
import logging
import _thread

logging.basicConfig(level=logging.INFO)

def loop0():
    print("loop0  start all at " + time.ctime())
    time.sleep(5)
    print("loop0 end  all at " + time.ctime())

def loop1():
    print("loop1 start all at " + time.ctime())
    time.sleep(5)
    print("loop1 end  all at " + time.ctime())


def main():
    logging.info('start all at' + time.ctime())
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1, ())
    time.sleep(6)
    logging.info('end  all at' + time.ctime())



if __name__ == '__main__':
    main()
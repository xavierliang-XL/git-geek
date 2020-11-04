import threading
import time

res=0
lock=threading.Lock()#创建锁
def task1():
    lock.acquire()  # 上锁
    global res
    for i in range(1000000):
        res=res+1
    print("t1_total:",res)
    lock.release()#开锁

def task2():
    lock.acquire()  # 上锁
    global res
    for i in range(1000000):
        res=res+1

    print("t2_total:",res)
    lock.release()  # 开锁


#t1_total: 1000000
#t2_total: 2000000
#互斥锁是让多个进程互相去抢锁，抢到的线程先运行。
if __name__ == '__main__':
    t1_thread=threading.Thread(target=task1, name="task1_thread")
    t2_thread = threading.Thread(target=task2, name="task2_thread")

    t1_thread.start()
    t2_thread.start()
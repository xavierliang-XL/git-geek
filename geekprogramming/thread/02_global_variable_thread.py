import threading
import time

res=0

def task1():
    global res
    for i in range(1000000):
        res=res+1

    print("t1_total:",res)

def task2():
    global res
    for i in range(1000000):
        res=res+1

    print("t2_total:",res)


#t1_total: 1194196
#t2_total: 1241194
#线程的运行是无序的，每一次多线程运行的结果都会不同，数字越大运行差错就会越大
if __name__ == '__main__':
    t1_thread=threading.Thread(target=task1, name="task1_thread")
    t2_thread = threading.Thread(target=task2, name="task2_thread")

    t1_thread.start()
    t1_thread.join()#强制让第一个线程先运行
    t2_thread.start()
#1.准备任务
import threading
import time


def coding():
    print("coding_thread:",threading.current_thread())
    for i in range(10):
        print("coding...")
        time.sleep(0.3)

def debugging():
    print("debugging_thread:",threading.current_thread())
    for i in range(10):
        print("debugging...")
        time.sleep(0.3)
if __name__=='__main__':
    #2.创建进程
    coding_thread=threading.Thread(target=coding)
    debugging_thread=threading.Thread(target=debugging)
    #Process([group [,target[,name]])
    #3.启动进程
    coding_thread.start()
    debugging_thread.start()

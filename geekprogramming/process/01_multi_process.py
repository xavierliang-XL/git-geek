#1.准备任务
import multiprocessing
import time


def coding():
    for i in range(10):
        print("coding...")
        time.sleep(0.3)

def debugging():
    for i in range(10):
        print("debugging...")
        time.sleep(0.3)
if __name__=='__main__':
    #2.创建进程
    coding_process=multiprocessing.Process(target=coding)
    debugging_process=multiprocessing.Process(target=debugging)
    #Process([group [,target[,name]])
    #3.启动进程
    coding_process.start()
    debugging_process.start()
import multiprocessing
import time

#让子进程一直为true,测试主进程
def task():
    while True:
        print("task executing...")
        time.sleep(0.3)

if __name__ == '__main__':
    sub_process=multiprocessing.Process(target=task,name="sub_process")
    sub_process.daemon=True
#让主进程退出子进程销毁，不让主进程再去等待

    sub_process.start()
    time.sleep(1)
    print("main over")
#主进程会等待所有子进程执行结束之后再结束（销毁）
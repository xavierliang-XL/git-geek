import threading
lock=threading.Lock()
def get_val(index):
    lock.acquire()
    print(threading.current_thread())
    list=[10,11,12]
    if index>=len(list):#通过过滤正确的避免死锁(再有可能会出现问题的地方添加过滤，保证程序的正确性)
        print("index out of range:",index)
        return
    print(list[index],threading.current_thread())
    lock.release()#出现死锁，程序无法继续向下打印，因为list只有三项。

if __name__ == '__main__':
    for i in range(10):
        t1_thread=threading.Thread(target=get_val, name="task1_thread",args=(i,))
        t1_thread.start()
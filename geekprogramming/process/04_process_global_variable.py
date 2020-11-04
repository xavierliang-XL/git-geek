import multiprocessing
import time

g_list=[]
#1.1添加数据任务
def add_data():
    for i in range(1,10):
        g_list.append(i)
        print("added:",i)
        time.sleep(0.3)

    print("after added:",g_list)
#1.2读取数据任务
def read_data():
    print("read",g_list)

#2.创建子进程（当前此类为主进程）
if __name__ == '__main__':
    add_data_process=multiprocessing.Process(target=add_data,name="add_data_process")
    read_data_process=multiprocessing.Process(target=read_data,name="read_data_process")

#3启动进程
    add_data_process.start()
    read_data_process.start()

#结果：read并没有调用g_list,进程之间不共享全局变量

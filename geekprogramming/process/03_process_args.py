import multiprocessing


def show_info(name,age):
    print(name,age)

if __name__ == '__main__':
    #sub_process=multiprocessing.Process(target=show_info, args=("david",14))
    #sub_process = multiprocessing.Process(target=show_info, kwargs={"name":"david","age":14})
    sub_process = multiprocessing.Process(target=show_info, args=("david",),kwargs={"age": 14})
    sub_process.start()

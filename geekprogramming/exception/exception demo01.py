import time
try:
    f = open('test.txt','r')#no such file found error
    try:
        while True:
            content=f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    except:
        print('意外终止')
    finally:
        f.close()
        print('关闭')
except:
    print('没有这个文件')
import socket

if __name__ == '__main__':
    #1.创建tcp服务器套接字
    tcp_server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.设置端口号，为了让程序退出时，端口号立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    #3.绑定端口号
    tcp_server_socket.bind(("",8000))
    #4.设置监听
    tcp_server_socket.listen(128)
    #5.循环等待客户端连接请求
    while True:
        new_socket,ip_port=tcp_server_socket.accept()
        #6.接收到客户端发来的请求信息
        recv_data=new_socket.recv(4096)
        print(recv_data)
        recv_content=recv_data.decode("utf-8")
        request_list=recv_content.split(" ",maxsplit=2)
        request_path=request_list[1]
        print(request_path)
        #7.打开文件读取文件中的数据
        with open("static/index.html","rb")as file:#rb:以二进制的形式读取bytes
            file_data=file.read()

        #8.准备响应行
        response_line="HTTP/1.1 200 OK\r\n"
        #9.响应头
        response_header="Server:PWS/1.0\r\n"
        #10.响应体
        response_body=file_data

        #11.封装response并进行编辑
        response=(response_line+response_header+"\r\n").encode("utf-8")+response_body
        #13.发送给客户端
        new_socket.send(response)
        #14.关闭套接字
        new_socket.close()

        #代码链接:https://github.com/isisisisisitch/geekPython
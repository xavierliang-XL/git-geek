import socket
import threading


def handle_client_request(ip_port, new_client):
    print("client port num:", ip_port)
    # 接收数据
    recv_data = new_client.recv(1024)
    if recv_data:#只要客户端不断开，就一直接收客户端的信息
        recv_content = recv_data.decode("utf-8")
        print("client said: ", recv_content, ip_port)

        # 发送数据
        send_content = "hello client"  # input()
        send_data = send_content.encode("utf-8")
        new_client.send(send_data)
    else:
        #客户端关闭
        print("client is offline: ",ip_port)
        tcp_server_socket.close()

        # 关闭套接字
    new_client.close()




if __name__ == '__main__':

    # 创建服务端端套接字对象
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #设置端口号的复用：服务器程序退出端口号立即释放
    #SOL_SOCKET:表示当前套接字
    #SO_REUSEADDR：表示复用端口号的选项
    #True：表示确定复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("127.0.0.1", 9090))
    # 设置监听
    #设置最大等待建立连接的个数
    tcp_server_socket.listen(128)
    new_client, ip_port = tcp_server_socket.accept()
    # 等待接受客户端的连接请求
    while True:

        #能来到这里，说明客户端和服务器端建立连接成功
        #创建子线程，让子线程专门负责接收客户端的信息
        sub_thread = threading.Thread(target=handle_client_request,args=(ip_port, new_client))
        sub_thread.setDaemon(True)
        sub_thread.start()
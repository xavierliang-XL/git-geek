import socket
import threading


def text():
    # 发送数据
    while True:
        send_content = input("say something:")  # input()
        send_data = send_content.encode("utf-8")
        tcp_client_socket.send(send_data)
        # 接收数据
        recv_data = tcp_client_socket.recv(1024)
        recv_content = recv_data.decode("utf-8")
        print("party:",recv_content)
        if send_content=="close":
            tcp_client_socket.close()
            break


# 关闭客户端套接字

if __name__ == '__main__':
    # 1.创建客户端套接字对象
    #AF_INET:ipv4
    #SOCK_STREAM: tcp
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和服务端套接字建立连接
    tcp_client_socket.connect(('127.0.0.1', 9090))


    cli_thread = threading.Thread(target=text)
    cli_thread.start()
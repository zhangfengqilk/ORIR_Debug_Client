from PySide2 import QtCore
import socket
import threading
from src.base import stopThreading
import time

class TCP_Server:
    runinfo_signal = QtCore.Signal(str, bytes)
    recv_data_signal = QtCore.Signal(bytes)

    def __init__(self):
        super(TCP_Server, self).__init__()

        self.tcp_socket = None
        self.server_thread = None
        self.clien_socket_list = list()

        self.link = False  # 用于标记是否开启了连接

    def tcp_server_start(self, ip_addr, port):
        """
        功能函数，TCP服务端开启的方法
        :return: None
        """
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 取消主动断开连接四次握手后的TIME_WAIT状态
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 设定套接字为非阻塞式
        self.tcp_socket.setblocking(False)
        try:
            self.tcp_socket.bind((ip_addr, port))
        except Exception as ret:
            msg = '请检查端口号\n'
            self.runinfo_signal.emit(msg, None)
        else:
            self.tcp_socket.listen()
            self.server_thread = threading.Thread(target=self.tcp_server_concurrency)
            self.server_thread.start()
            msg = 'TCP服务端正在监听端口:%s\n' % str(port)
            self.runinfo_signal.emit(msg, None)

    def tcp_server_concurrency(self):
        """
        功能函数，供创建线程的方法；
        使用子线程用于监听并创建连接，使主线程可以继续运行，以免无响应
        使用非阻塞式并发用于接收客户端消息，减少系统资源浪费，使软件轻量化
        :return:None
        """
        while True:
            try:
                client_socket, client_address = self.tcp_socket.accept()
            except Exception as ret:
                time.sleep(0.001)
            else:
                client_socket.setblocking(False)
                # 将创建的客户端套接字存入列表,client_address为ip和端口的元组
                self.client_socket_list.append((client_socket, client_address))
                msg = 'TCP服务端已连接IP:%s端口:%s\n' % client_address
                self.runinfo_signal.emit(msg, None)
            # 轮询客户端套接字列表，接收数据
            for client, address in self.client_socket_list:
                try:
                    recv_msg = client.recv(1024)
                except Exception as ret:
                    pass
                else:
                    if recv_msg:
                        # try:
                        #     msg = recv_msg.decode('utf-8')
                        # except Exception as e:
                        #     msg = recv_msg.hex()
                        # msg = recv_msg
                        # print('recv_msg: ', recv_msg.hex())
                        # print(type(msg))
                        msg = '来自IP:{}端口:{}:\n'.format(address[0], address[1])
                        self.runinfo_signal.emit(msg, recv_msg)
                        self.recv_data_signal.emit(recv_msg)
                    else:
                        client.close()
                        self.client_socket_list.remove((client, address))

    def tcp_server_send(self, data):
        """
        功能函数，用于TCP服务端和发送消息
        :return: None
        """
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.runinfo_signal.emit(msg, None)
            return False
        else:
            try:
                # 向所有连接的客户端发送消息
                for client, address in self.client_socket_list:
                    client.send(data)
                # self.runinfo_signal.emit('TCP服务端已发送: \n' + str(data))
            except Exception as ret:
                self.runinfo_signal.emit('发送失败\n', None)
                return False

    def tcp_server_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        if self.net_type_cbb.currentIndex() == 0:
            try:
                for client, address in self.client_socket_list:
                    client.close()
                self.tcp_socket.close()
                if self.link is True:
                    msg = '已断开网络\n'
                    self.runinfo_signal.emit(msg, None)
            except Exception as ret:
                pass
        try:
            stopThreading.stop_thread(self.sever_thread)
        except Exception:
            pass
        self.link = False

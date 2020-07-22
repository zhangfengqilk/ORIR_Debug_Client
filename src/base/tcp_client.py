from PySide2 import QtCore
import socket
import threading
from src.base import stopThreading

class TCP_Client:
    runinfo_signal = QtCore.Signal(str, bytes)
    recv_data_signal = QtCore.Signal(bytes)

    def __init__(self):
        super(TCP_Client, self).__init__()
        self.tcp_socket = None
        self.client_thread = None

        self.link = False  # 用于标记是否开启了连接

    def tcp_client_start(self, ip_addr, port):
        """
        功能函数，TCP客户端连接其他服务端的方法
        :return:
        """
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            address = (ip_addr, port)
        except Exception as ret:
            self.runinfo_signal.emit('请检查目标IP，目标端口\n',None)
        else:
            try:
                self.runinfo_signal.emit('正在连接目标服务器\n',None)
                self.tcp_socket.connect(address)

            except Exception as ret:
                self.runinfo_signal.emit('无法连接目标服务器\n',None)
            else:
                self.client_thread = threading.Thread(target=self.tcp_client_concurrency, args=(address,))
                self.client_thread.start()
                msg = 'TCP客户端已连接IP:%s端口:%s\n' % address
                self.runinfo_signal.emit(msg, None)

    def tcp_client_concurrency(self, address):
        """
        功能函数，用于TCP客户端创建子线程的方法，阻塞式接收
        :return:
        """
        while True:
            recv_msg = self.tcp_socket.recv(1024)
            if recv_msg:
            #     try:
            #         msg = recv_msg.decode('utf-8')
            #     except:
            #         try:
            #             msg = recv_msg.hex()
            #         except:
            #             pass
                msg = '来自IP:{}端口:{}:\n'.format(address[0], address[1])
                self.runinfo_signal.emit(msg, recv_msg)
                self.recv_data_signal.emit(recv_msg)
            else:
                self.tcp_socket.close()
                self.runinfo_signal.emit('从服务器断开连接\n', None)
                break

    def tcp_client_send(self, data):
        """
                功能函数，用于TCP服务端和TCP客户端发送消息
                :return: None
                """
        if self.link is False:
            msg = '请选择服务，并点击连接网络\n'
            self.runinfo_signal.emit(msg, None)
            return False
        else:
            try:
                self.tcp_socket.send(data)
                # self.runinfo_signal.emit('TCP客户端已发送\n' + str(data))
                return True
            except Exception as ret:
                self.runinfo_signal.emit('发送失败\n', None)
                return False

    def tcp_client_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        try:
            self.tcp_socket.close()
            if self.link is True:
                msg = '已断开网络\n'
                self.runinfo_signal.emit(msg, None)
        except Exception as ret:
            pass

        try:
            stopThreading.stop_thread(self.client_thread)
        except Exception:
            pass
        self.link = False


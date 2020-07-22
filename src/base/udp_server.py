from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QObject

from src.base import stopThreading
import socket
import threading
import sys



class UDP_Server:
    runinfo_signal = QtCore.Signal(str, bytes)
    recv_data_signal = QtCore.Signal(bytes)
    def __init__(self):
        super(UDP_Server, self).__init__()
        self.udp_server_socket = None
        self.address = None
        self.sever_th = None
        self.link = False
        self.client_socket_list = list()

    def udp_server_start(self, ip_addr, port):
        """
        开启UDP服务端方法
        :return:
        """
        self.udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.udp_server_socket.bind((ip_addr, port))
        except Exception as ret:
            self.runinfo_signal.emit('请检查端口号\n', None)
        else:
            self.sever_th = threading.Thread(target=self.udp_server_concurrency)
            self.sever_th.start()
            msg = 'UDP服务端正在监听端口:{}\n'.format(port)
            self.runinfo_signal.emit(msg, None)

    def udp_server_concurrency(self):
        """
        用于创建一个线程持续监听UDP通信
        :return:
        """
        while True:
            recv_msg, recv_addr = self.udp_server_socket.recvfrom(1024)
            msg = recv_msg.decode('utf-8')
            msg = '来自IP:{}端口:{}:\n{}\n'.format(recv_addr[0], recv_addr[1], msg)
            self.runinfo_signal.emit(msg, None)
            if recv_addr not in self.client_socket_list:
                self.client_socket_list.append((recv_addr))


    def udp_server_send(self, data):
        """
        功能函数，用于UDP客户端发送消息
        :return: None
        """
        if self.link is False:
            self.runinfo_signal.emit('请选择服务，并点击连接网络\n', None)
        else:
            try:
                for client_addr in self.client_socket_list:
                    self.udp_server_socket.sendto(data, client_addr)
                    self.runinfo_signal.emit('UDP服务端已发送\n', None)
            except Exception as ret:
                self.runinfo_signal.emit('发送失败\n', None)

    def udp_server_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        try:
            self.udp_socket.close()
            if self.link is True:
                self.runinfo_signal.emit('已断开网络\n', None)
        except Exception as ret:
            pass
        try:
            stopThreading.stop_thread(self.sever_th)
        except Exception:
            pass

from PySide2 import QtCore

import socket
import threading

class UDP_Client:
    runinfo_signal = QtCore.Signal(str, bytes)
    recv_data_signal = QtCore.Signal(bytes)

    def __init__(self):
        super(UDP_Client, self).__init__()
        self.udp_client_socket = None
        self.address = None
        self.client_thread = None
        self.link = False

    def udp_client_start(self, remote_ip_addr, remote_port):
        """
        确认UDP客户端的ip及地址
        :return:
        """
        self.udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.address = (remote_ip_addr, remote_port)
        except Exception as ret:
            self.runinfo_signal.emit('请检查目标IP，目标端口\n', None)
        else:
            self.client_thread = threading.Thread(target=self.udp_client_concurrency)
            self.client_thread.start()
            self.runinfo_signal.emit('UDP客户端已启动\n', None)

    def udp_client_concurrency(self):
        """
        用于创建一个线程持续监听UDP通信
        :return:
        """
        while True:
            recv_msg, recv_addr = self.udp_client_socket.recvfrom(1024)
            msg = recv_msg.decode('utf-8')
            msg = '来自IP:{}端口:{}:\n{}\n'.format(recv_addr[0], recv_addr[1], msg)
            self.runinfo_signal.emit(msg, None)

    def udp_client_send(self, data):
        """
        功能函数，用于UDP客户端发送消息
        :return: None
        """
        if self.link is False:
            self.runinfo_signal.emit('请选择服务，并点击连接网络\n', None)
        else:
            try:
                self.udp_client_socket.sendto(data, self.address)
                self.runinfo_signal.emit('UDP客户端已发送\n', None)
            except Exception as ret:
                self.runinfo_signal.emit('发送失败\n', None)

    def grpc_client_close(self):

        pass

    def udp_client_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        try:
            self.udp_client_socket.close()
            if self.link is True:
                self.runinfo_signal.emit('已断开网络\n', None)
        except Exception as ret:
            pass


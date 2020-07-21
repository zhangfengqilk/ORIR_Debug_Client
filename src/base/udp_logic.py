from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QObject

from src.base import stopThreading
import socket
import threading
import sys

class AbstractNet(QObject):
    runinfo_signal = QtCore.Signal(str)
    recv_data_signal = QtCore.Signal(str)

    def __init__(self, local_ip, local_port, remote_ip, remote_port):
        self.local_ip = local_ip
        self.local_port = local_port
        self.remote_ip = remote_ip
        self.remote_port = remote_port

        self.socket_handle = None # 套接字句柄


    def start(self):
        pass

    def send(self, data):
        pass

    def close(self):
        pass

class UDPServer(AbstractNet):
    def __init__(self, local_ip, local_port, remote_ip, remote_port):
        super(UDPServer, self).__init__(local_ip, local_port, remote_ip, remote_port)



class UdpLogic():
    runinfo_signal = QtCore.Signal(str, bytes)
    recv_data_signal = QtCore.Signal(bytes)
    def __init__(self):
        super(UdpLogic, self).__init__()
        self.udp_socket = None
        self.address = None
        self.sever_th = None
        self.link = False
        self.client_socket_list = list()

    def init(self, local_ip, local_port, remote_ip, remote_port):
        self.local_ip = local_ip
        self.local_port = local_port
        self.remote_ip = remote_ip
        self.remote_port = remote_port

    def udp_server_start(self, ip_addr, port):
        """
        开启UDP服务端方法
        :return:
        """
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.udp_socket.bind((ip_addr, port))
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
            recv_msg, recv_addr = self.udp_socket.recvfrom(1024)
            msg = recv_msg.decode('utf-8')
            msg = '来自IP:{}端口:{}:\n{}\n'.format(recv_addr[0], recv_addr[1], msg)
            self.runinfo_signal.emit(msg, None)
            if recv_addr not in self.client_socket_list:
                self.client_socket_list.append((recv_addr))


    def udp_client_start(self, ip_addr, port):
        """
        确认UDP客户端的ip及地址
        :return:
        """
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.address = (ip_addr, port)
        except Exception as ret:
            self.runinfo_signal.emit('请检查目标IP，目标端口\n', None)
        else:
            self.runinfo_signal.emit('UDP客户端已启动\n', None)

    def udp_send(self, data):
        """
        功能函数，用于UDP客户端发送消息
        :return: None
        """
        if self.link is False:
            self.runinfo_signal.emit('请选择服务，并点击连接网络\n', None)
        else:
            try:
                if self.net_type_cbb.currentIndex() == 2:
                    for client_addr in self.client_socket_list:
                        self.udp_socket.sendto(data, client_addr)
                        self.runinfo_signal.emit('UDP服务端已发送\n', None)

                elif self.net_type_cbb.currentIndex() == 3:
                    self.udp_socket.sendto(data, self.address)
                    self.runinfo_signal.emit('UDP客户端已发送\n', None)

            except Exception as ret:
                self.runinfo_signal.emit('发送失败\n', None)

    def udp_close(self):
        """
        功能函数，关闭网络连接的方法
        :return:
        """
        if self.net_type_cbb.currentIndex() == 2:
            try:
                self.udp_socket.close()
                if self.link is True:
                    self.runinfo_signal.emit('已断开网络\n', None)
            except Exception as ret:
                pass
        if self.net_type_cbb.currentIndex() == 3:
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
        try:
            stopThreading.stop_thread(self.client_th)
        except Exception:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = UdpLogic(1)
    ui.show()
    sys.exit(app.exec_())

from src.uibasewindow.Ui_ORIR_Debug_LogAnalysis_Page import Ui_ORIR_LogAnalysis_Page
from PySide2.QtWidgets import QWidget,QFileDialog

from src.uibasewindow.Ui_ORIR_Debug_Page import Ui_ORIR_Debug_Page
from PySide2.QtWidgets import QWidget,QFileDialog
from PySide2.QtWidgets import QApplication, QWidget, QListView, QMessageBox
from PySide2.QtGui import QTextCursor
import sys
import socket
from src.base.tcp_logic import TcpLogic
from src.base.udp_logic import UdpLogic
import time
import datetime
import threading

class ORIR_LogAnalysis(QWidget, Ui_ORIR_LogAnalysis_Page, TcpLogic, UdpLogic):
    def __init__(self):
        super(ORIR_LogAnalysis, self).__init__()
        Ui_ORIR_LogAnalysis_Page.__init__(self)
        TcpLogic.__init__(self)
        UdpLogic.__init__(self)

        self.setupUi(self)
        self.signal_connect()

    def signal_connect(self):
        self.get_local_ip_btn.clicked.connect(self.get_host_ip)
        self.udp_connect_btn.clicked.connect(self.udp_connect_net)
        self.tcp_connect_btn.clicked.connect(self.tcp_connect_net)

        self.runinfo_signal.connect(self.show_runinfo)
        self.recv_data_signal.connect(self.show_runinfo)

    def get_host_ip(self):
        """
        获取本机IP
        :return:
        """
        self.ip_addr_le.clear()
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.ip_addr_le.setText(str(self.local_ip))
        print(self.local_ip)

    def udp_connect_net(self):
        if self.udp_connect_btn.text() == 'UDP连接':
            self.udp_server_start(str(self.ip_addr_le.text()), int(self.udp_port_le.text()))
            self.link = True
            self.udp_connect_btn.setText('UDP断开')
            self.runinfo_signal.emit('UDP连接成功\n', None)
        elif self.udp_connect_btn.text() == 'UDP断开':
            self.udp_close()
            self.link = False
            self.udp_connect_btn.setText('UDP连接')
            self.runinfo_signal.emit('UDP 断开', None)

    def tcp_connect_net(self):
        if self.tcp_connect_btn.text() == 'TCP连接':
            self.tcp_client_start(str(self.ip_addr_le.text()), int(self.tcp_port_le.text()))
            self.link = True
            self.tcp_connect_btn.setText('TCP断开')
            self.runinfo_signal.emit('TCP连接成功\n', None)
        elif self.tcp_connect_btn.text() == 'TCP断开':
            self.tcp_close()
            self.link = False
            self.net_connect_btn.setText('TCP连接')
            self.runinfo_signal.emit('TCP 断开', None)

    def show_runinfo(self, info, data=None):
        msg = '[' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  + '] '+ info
        self.runinfo_te.insertPlainText(msg)
        if data:
            if self.is_show_as_hex_cb.isChecked():
                self.runinfo_te.insertPlainText(self.byte2hex_str(data))
            else:
                try:
                    self.runinfo_te.insertPlainText(data.decode('utf-8'))
                except:
                    self.runinfo_te.insertPlainText('无法正确显示，请尝试使用十六进制显示')
        self.runinfo_te.insertPlainText('\n\n')
        self.runinfo_te.moveCursor(QTextCursor.End)
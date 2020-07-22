from src.uibasewindow.Ui_ORIR_Debug_LogAnalysis_Page import Ui_ORIR_LogAnalysis_Page
from PySide2.QtWidgets import QWidget,QFileDialog

from src.uibasewindow.Ui_ORIR_Debug_Page import Ui_ORIR_Debug_Page
from PySide2.QtWidgets import QWidget,QFileDialog
from PySide2.QtWidgets import QApplication, QWidget, QListView, QMessageBox
from PySide2.QtGui import QTextCursor

import socket
from src.base.tcp_client import TCP_Client
from src.base.udp_server import UDP_Server
import time
import datetime
import threading
from src.base.utils import *


class ORIR_LogAnalysis(QWidget, Ui_ORIR_LogAnalysis_Page, TCP_Client, UDP_Server):
    def __init__(self):
        super(ORIR_LogAnalysis, self).__init__()
        Ui_ORIR_LogAnalysis_Page.__init__(self)
        TCP_Client.__init__(self)
        UDP_Server.__init__(self)

        self.setupUi(self)
        self.signal_connect()

        self.level_cbb.setView(QListView())
        self.tag_cbb.setView(QListView())

    def signal_connect(self):
        self.get_local_ip_btn.clicked.connect(self.get_host_ip)
        self.udp_connect_btn.clicked.connect(self.udp_connect_net)
        self.tcp_connect_btn.clicked.connect(self.tcp_connect_net)

        self.runinfo_signal.connect(self.show_runinfo)
        # self.recv_data_signal.connect(self.show_runinfo)
        self.send_debug_msg_btn.clicked.connect(self.send_debug_msg)
        self.level_cbb.currentTextChanged.connect(self.set_log_level)
        self.tag_cbb.currentTextChanged.connect(self.set_log_tag)
        self.keyword_le.editingFinished.connect(self.set_log_keyword)

        self.clear_runinfo_btn.clicked.connect(self.clear_runinfo)

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
            self.udp_server_close()
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
            self.tcp_client_close()
            self.link = False
            self.tcp_connect_btn.setText('TCP连接')
            self.runinfo_signal.emit('TCP 断开', None)

    def show_runinfo(self, info, data=None):
        msg = '[{}] {}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), info)
        # msg = '[' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + '] ' + info
        self.runinfo_te.insertPlainText(msg)
        if data:
            if self.is_show_as_hex_cb.isChecked():
                self.runinfo_te.insertPlainText(byte2hex_str(data))
            else:
                try:
                    self.runinfo_te.insertPlainText(data.decode('utf-8', errors='ignore'))
                except:
                    self.runinfo_te.insertPlainText('无法正确显示，请尝试使用十六进制显示')

        self.runinfo_te.insertPlainText('\n\n')
        self.runinfo_te.moveCursor(QTextCursor.End)

    def send_debug_msg(self):
        msg = str(self.send_debug_msg_te.toPlainText())
        self.runinfo_signal.emit('发送：' + msg + '\n', None)
        # print('msg1: ', msg, type(msg))

        # 判断是否为16进制发送，如果是则转为16进制，否则编码为utf-8
        if self.send_hex_data_cb.isChecked():
            msg = msg.replace(' ', '')
            if len(msg) % 2:
                msg = msg[0: -1] + '0' + msg[-1]
            try:
                msg = bytes.fromhex(msg)
            except:
                msg = bytes(msg, encoding='utf-8')
                # self.runinfo_signal.emit('无法将发送数据已十六进制发送', None)
        else:
            msg = msg.encode('utf-8')

        # 判断是否为循环发送，如果时间框里有时间，则为循环发送
        if self.send_debug_msg_btn.text() == '发送':
            self.send_period = int(self.cycle_send_period_ms_le.text())
            if self.send_period == 0:
                self.tcp_client_send(msg)
            else:   # 开启循环发送线程
                self.is_cycle_send = True
                self.send_debug_msg_btn.setText('停止')
                thd = threading.Thread(target=self.cycle_send)
                thd.start()

        elif self.send_debug_msg_btn.text() == '停止':
            self.send_debug_msg_btn.setText('发送')
            self.is_cycle_send = False

    def cycle_send(self):
        while self.is_cycle_send:
            msg = str(self.send_debug_msg_te.toPlainText())
            self.runinfo_signal.emit('发送：' + msg + '\n', None)
            # print('msg1: ', msg, type(msg))
            if self.send_hex_data_cb.isChecked():
                msg = msg.replace(' ', '')
                if len(msg) % 2:
                    msg = msg[0: -1] + '0' + msg[-1]
                try:
                    msg = bytes.fromhex(msg)
                except:
                    msg = bytes(msg, encoding='utf-8')
            else:
                msg = msg.encode('utf-8')

            self.tcp_client_send(msg)
            time.sleep(self.send_period / 1000)

    def set_log_level(self, level):
        if not self.link:
            self.runinfo_signal.emit('请先连接网络！', None)
            return

        self.tcp_client_send('ulog level {}'.format(level).encode('utf-8'))

        if level == 'allon':
            self.runinfo_signal.emit('打开所有等级', None)
        elif level == 'alloff':
            self.runinfo_signal.emit('关闭所有等级', None)
        else:
            self.runinfo_signal.emit('设置日志级别为：{}'.format(level), None)

    def set_log_tag(self, tag):
        if not self.link:
            self.runinfo_signal.emit('请先连接网络！', None)
            return

        if tag == '清除标签':
            tag = ''
        self.tcp_client_send('ulog tag {}'.format(tag).encode('utf-8'))
        if tag:
            self.runinfo_signal.emit('设置日志标签为：{}'.format(tag), None)
        else:
            self.runinfo_signal.emit('清除日志标签', None)

    def set_log_keyword(self):
        if not self.link:
            self.runinfo_signal.emit('请先连接网络！', None)
            return

        keyword = self.keyword_le.text()
        self.tcp_client_send('ulog keyword {}'.format(keyword).encode('utf-8'))

        if not keyword:
            self.runinfo_signal.emit('清除日志关键字', None)
        else:
            self.runinfo_signal.emit('设置日志关键字为：{}'.format(keyword), None)
    def clear_runinfo(self):
        self.runinfo_te.clear()
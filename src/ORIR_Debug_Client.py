from PySide2.QtWidgets import QApplication, QWidget, QListView, QMessageBox
from PySide2.QtGui import QTextCursor
from PySide2 import QtCore
from src.uibasewindow.Ui_ORIR_Debug_Client import Ui_ORIR_Debug_Client
import sys
import socket
from src.tcp_logic import TcpLogic
from src.udp_logic import UdpLogic
import time
import datetime
import threading


class ORIR_Debug_Client(QWidget, TcpLogic, UdpLogic):
    def __init__(self):
        super(ORIR_Debug_Client, self).__init__()
        self.setupUi(self)
        self.link = False
        self.signal_connect()
        self.client_socket_list = []
        self.send_period = 0
        self.is_cycle_send = False
        self.net_type_cbb.setView(QListView())

        # 标志位
        self.is_ptz_bearing_inplace = False
        self.is_ptz_pitching_inplace = False
        self.is_lift_inplace = False
        self.is_walkmotor_inplace = False

    def signal_connect(self):
        """
        信号槽设置
        :return:
        """
        self.net_connect_btn.clicked.connect(self.connect_net)
        self.get_local_ip_btn.clicked.connect(self.get_host_ip)
        self.runinfo_signal.connect(self.show_runinfo)
        self.recv_data_signal.connect(self.parse_recv_data)
        self.send_debug_msg_btn.clicked.connect(self.send_debug_msg)

        self.ptz_signal_connect()
        self.debug_signal_connect()
        self.walkmotor_signal_connect()
        self.lifter_signal_connect()

        self.partialdischarge_detect_btn.clicked.connect(self.partialdischarge_detect)
        self.barcode_query_position_btn.clicked.connect(self.barcode_query_position)
        self.hall_query_position_btn.clicked.connect(self.hall_query_position)
        self.ranging_query_position_btn.clicked.connect(self.ranging_query_position)
        self.statuslight_signal_connect()



    def ptz_signal_connect(self):
        self.ptz_poweron_btn.clicked.connect(self.ptz_poweron)
        self.ptz_poweroff_btn.clicked.connect(self.ptz_poweroff)
        self.ptz_down_btn.clicked.connect(self.ptz_down)
        self.ptz_up_btn.clicked.connect(self.ptz_up)
        self.ptz_left_btn.clicked.connect(self.ptz_left)
        self.ptz_right_btn.clicked.connect(self.ptz_right)
        self.ptz_leftup_btn.clicked.connect(self.ptz_leftup)
        self.ptz_leftdown_btn.clicked.connect(self.ptz_leftdown)
        self.ptz_rightup_btn.clicked.connect(self.ptz_rightup)
        self.ptz_rightdown_btn.clicked.connect(self.ptz_rightdown)
        self.ptz_stop_btn.clicked.connect(self.ptz_stop)

        self.ptz_set_bearing_btn.clicked.connect(self.ptz_set_bearing)
        self.ptz_set_pitching_btn.clicked.connect(self.ptz_set_pitching)
        self.ptz_query_bearing_btn.clicked.connect(self.ptz_query_bearing)
        self.ptz_query_pitching_btn.clicked.connect(self.ptz_query_pitching)
        self.ptz_set_bearing_pitching_btn.clicked.connect(self.ptz_set_bearing_pitching)
        self.ptz_query_bearing_pitching_btn.clicked.connect(self.ptz_query_bearing_pitching)

        self.ptz_set_velocity_btn.clicked.connect(self.ptz_set_velocity)
        self.ptz_query_velocity_btn.clicked.connect(self.ptz_query_velocity)
        self.ptz_set_zero_position_btn.clicked.connect(self.ptz_set_zero_position)

    def debug_signal_connect(self):
        self.clear_runinfo_btn.clicked.connect(self.clear_runinfo)

    def walkmotor_signal_connect(self):
        self.walkmotor_poweron_btn.clicked.connect(self.walkmotor_poweron)
        self.walkmotor_backward_btn.clicked.connect(self.walkmotor_backward)
        self.walkmotor_forward_btn.clicked.connect(self.walkmotor_forward)
        self.walkmotor_poweroff_btn.clicked.connect(self.walkmotor_poweroff)
        self.walkmotor_stop_btn.clicked.connect(self.walkmotor_stop)
        self.walkmotor_query_pos_btn.clicked.connect(self.walkmotor_query_pos)
        self.walkmotor_query_velocity_btn.clicked.connect(self.walkmotor_query_velocity)
        self.walkmotor_set_pos_btn.clicked.connect(self.walkmotor_set_pos)
        self.walkmotor_set_velocity_btn.clicked.connect(self.walkmotor_set_velocity)

    def lifter_signal_connect(self):
        self.lifter_up_btn.clicked.connect(self.lifter_up)
        self.lifter_down_btn.clicked.connect(self.lifter_down)
        self.lifter_stop_btn.clicked.connect(self.lifter_stop)
        self.lifter_query_pos_btn.clicked.connect(self.lifter_query_pos)

    def statuslight_signal_connect(self):
        self.statuslight_red_on_btn.clicked.connect(self.statuslight_red_on)
        self.statuslight_green_on_btn.clicked.connect(self.statuslight_green_on)
        self.statuslight_yellow_on_btn.clicked.connect(self.statuslight_yellow_on)
        self.statuslight_all_off_btn.clicked.connect(self.statuslight_all_off)



    def clear_runinfo(self):
        self.runinfo_te.clear()

    def byte2hex_str(self, byte_data):
        """
        将十六进制数据转为hex字符串，每个字节中间加入空格
        :param byte_data:
        :return:
        """
        hex_str = str(byte_data.hex())
        hex_str = hex_str.upper()
        hex_str_list = []
        for i in range(0, len(hex_str) - 1, 2):
            hex_str_list.append(hex_str[i:i+2])
            hex_str_list.append(' ')

        return ''.join(hex_str_list)

    def int2hex_str(self, byte_len, data):
        """
        将某个整数转换为指定字节长度的十六进制字符串
        如：整数12，转为 2个字节长度的十六进制字符串，为000c

        :param byte_len:
        :param data:
        :return:
        """
        hex_str = hex(data)
        hex_str = hex_str[2:]

        if len(hex_str) % 2:
            hex_str = '0' + hex_str

        if len(hex_str) < byte_len * 2:
            hex_str = '00' * int(byte_len - len(hex_str)/2) + hex_str
        return hex_str


    def construct_cmd(self, device_type, data_len, opcode, data=''):
        cmd = bytearray()
        cmd += bytearray.fromhex('5aa5') # 帧头
        cmd += bytearray.fromhex(self.int2hex_str(2, 13)) # 总长度
        cmd += bytearray.fromhex('01')  # 地址
        cmd += bytearray.fromhex(self.int2hex_str(1, device_type)) # 设备类型

        # cmd += bytearray.fromhex(self.int2hex_str(2, data_len)) # 数据域长度
        cmd += bytearray.fromhex(self.int2hex_str(1, opcode)) # 操作码
        if data:
            cmd += bytearray.fromhex(self.int2hex_str(4, data))
        else:
            cmd += bytearray.fromhex(self.int2hex_str(4, 0))
        cmd += bytearray.fromhex('00')
        cmd += bytearray.fromhex('ff')
        return cmd

    def send_single_cmd(self, device_type, len, opcode, data, description):
        """
        针对单指令型的发送，如云台向下，云台向右，电机运行，查询云台方位等
        :param device_type:
        :param len:
        :param data:
        :param description:
        :return:
        """
        cmd = self.construct_cmd(device_type, len, opcode, data)
        if self.send_data(cmd):
            if str(data):
                run_msg = description  + '：' + str(data) + '：\n' + self.byte2hex_str(cmd) + '\n'
            else:
                run_msg = '发送' + description + '指令：\n' + self.byte2hex_str(cmd) + '\n'
            self.runinfo_signal.emit(run_msg, None)


##-------------------------云台指令-------------------------------
    def ptz_poweron(self):
        self.send_single_cmd(0x01, 0x01, 0x01, '', '云台上电')

    def ptz_poweroff(self):
        self.send_single_cmd(0x01, 0x01, 0x02, '', '云台下电')

    def ptz_down(self):
        self.send_single_cmd(0x01, 0x01, 0x05, '', '云台向下')

    def ptz_up(self):
        self.send_single_cmd(0x01, 0x01, 0x04, '', '云台向上')

    def ptz_left(self):
        self.send_single_cmd(0x01, 0x01, 0x06, '', '云台向左')

    def ptz_right(self):
        self.send_single_cmd(0x01, 0x01, 0x07, '', '云台向左')

    def ptz_leftup(self):
        self.ptz_left()
        self.ptz_up()

    def ptz_leftdown(self):
        self.ptz_left()
        self.ptz_down()

    def ptz_rightup(self):
        self.ptz_right()
        self.ptz_up()

    def ptz_rightdown(self):
        self.ptz_right()
        self.ptz_down()

    def ptz_stop(self):
        self.send_single_cmd(0x01, 0x01, 0x08, '', '云台停止')

    def ptz_set_bearing(self):
        bearing = int(float(self.ptz_bearing_le.text()) * 100)
        self.send_single_cmd(0x01, 0x03, 0x09, bearing, '设置云台方位')
        self.is_ptz_bearing_inplace = True
        self.ptz_inplace_le.setText('')

    def ptz_set_pitching(self):
        pitching = int(float(self.ptz_pitching_le.text()) * 100)
        self.send_single_cmd(0x01, 0x03, 0x0a, pitching, '设置云台俯仰')
        self.is_ptz_pitching_inplace = True
        self.ptz_inplace_le.setText('')

    def ptz_query_bearing(self):
        self.send_single_cmd(0x01, 0x01, 0x0d, '', '查询方位')

    def ptz_query_pitching(self):
        self.send_single_cmd(0x01, 0x01, 0x0e, '', '查询俯仰')

    def ptz_set_bearing_pitching(self):
        self.ptz_set_bearing()
        self.ptz_set_pitching()

    def ptz_query_bearing_pitching(self):
        self.ptz_query_bearing()
        self.ptz_query_pitching()

    def ptz_set_velocity(self):
        velocity = int(float(self.ptz_velocity_le.text()) * 100)
        self.send_single_cmd(0x01, 0x03, 0x0b, velocity, '设置云台速度')

    def ptz_query_velocity(self):
        self.send_single_cmd(0x01, 0x01, 0x0c, '', '查询云台速度')

    def ptz_set_zero_position(self):
        self.send_single_cmd(0x01, 0x01, 0x03, '', '校正云台')

##--------------------------行走电机指令--------------------------

    def walkmotor_poweron(self):
        self.send_single_cmd(0x03, 0x01, 0x01, '', '行走电机上电')

    def walkmotor_backward(self):
        self.send_single_cmd(0x03, 0x01, 0x04, '', '行走电机后退')

    def walkmotor_forward(self):
        self.send_single_cmd(0x03, 0x01, 0x03, '', '行走电机前进')

    def walkmotor_poweroff(self):
        self.send_single_cmd(0x03, 0x01, 0x02, '', '行走电机下电')

    def walkmotor_stop(self):
        self.send_single_cmd(0x03, 0x01, 0x05, '', '行走电机停止')

    def walkmotor_query_pos(self):
        self.send_single_cmd(0x03, 0x01, 0x07, '', '查询行走电机位置')
        self.is_walkmotor_inplace = True
        self.walkmotor_inplace_le.setText('')

    def walkmotor_query_velocity(self):
        self.send_single_cmd(0x03, 0x01, 0x0a, '', '查询行走电机速度')

    def walkmotor_set_pos(self):
        pos = int(float(self.walkmotor_pos_le.text()) * 100)
        self.send_single_cmd(0x03, 0x03, 0x06, pos, '设置行走电机位置')

    def walkmotor_set_velocity(self):
        velocity = int(float(self.walkmotor_velocity_le.text()) * 100)
        self.send_single_cmd(0x03, 0x03, 0x09, velocity, '设置行走电机速度')

##----------------------升降杆指令-----------------------------------
    def lifter_up(self):
        self.send_single_cmd(0x05, 0x01, 0x01, '', '升降杆上升')
        self.lifter_inplace_le.setText('')
        self.is_lift_inplace = True

    def lifter_down(self):
        self.send_single_cmd(0x05, 0x01, 0x02, '', '升降杆下降')
        self.lifter_inplace_le.setText('')
        self.is_lift_inplace = True

    def lifter_stop(self):
        self.send_single_cmd(0x05, 0x01, 0x03, '', '升降杆停止')

    def lifter_query_pos(self):
        self.send_single_cmd(0x05, 0x01, 0x05, '', '查询升降杆位置')

#--------------------局放、条形码、霍尔、测距指令------------------------
    def partialdischarge_detect(self):
        self.send_single_cmd(0x02, 0x01, 0x01, '', '局放探测')

    def barcode_query_position(self):
        self.send_single_cmd(0x04, 0x01, 0x01, '', '查询条形码位置')

    def hall_query_position(self):
        self.send_single_cmd(0x07, 0x01, 0x01, '', '查询霍尔位置')

    def ranging_query_position(self):
        self.send_single_cmd(0x08, 0x01, 0x01, '', '查询测距位置')

# -------------------------状态灯指令---------------------------------
    def statuslight_red_on(self):
        self.send_single_cmd(0x09, 0x01, 0x01, '', '红灯亮')

    def statuslight_green_on(self):
        self.send_single_cmd(0x09, 0x01, 0x03, '', '绿灯亮')

    def statuslight_yellow_on(self):
        self.send_single_cmd(0x09, 0x01, 0x02, '', '黄灯亮')

    def statuslight_all_off(self):
        self.send_single_cmd(0x09, 0x01, 0x04, '', '关灯亮')

    def connect_net(self):
        """
        连接网络
        :return:
        """
        if self.net_connect_btn.text() == '连接':
            if self.net_type_cbb.currentIndex() == 0:
                self.tcp_server_start('', int(self.port_le.text()))
            elif self.net_type_cbb.currentIndex() == 1:
                self.tcp_client_start(str(self.ip_addr_le.text()), int(self.port_le.text()))
            elif self.net_type_cbb.currentIndex() == 2:
                self.udp_server_start('', int(self.port_le.text()))
            elif self.net_type_cbb.currentIndex() == 3:
                self.udp_client_start(str(self.ip_addr_le.text()), int(self.port_le.text()))
            self.link = True
            self.net_connect_btn.setText('断开')
            self.runinfo_signal.emit('连接成功\n', None)
        elif self.net_connect_btn.text() == '断开':
            self.close_all()
            self.link = False
            self.net_connect_btn.setText('连接')

    def close_all(self):
        if self.net_type_cbb.currentIndex() in [0, 1]:
            self.tcp_close()
            self.client_socket_list.clear()
        elif self.net_type_cbb.currentIndex() in [2, 3]:
            self.udp_close()


    def closeEvent(self, event):
        # message为窗口标题
        # Are you sure to quit?窗口显示内容
        # QtGui.QMessageBox.Yes | QtGui.QMessageBox.No窗口按钮部件
        # QtGui.QMessageBox.No默认焦点停留在NO上
        reply = QMessageBox.question(self, 'Message', "确定退出？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 判断返回结果处理相应事项
        if reply == QMessageBox.Yes:
            self.close_all()
            event.accept()
        else:
            event.ignore()

    def get_host_ip(self):
        """
        获取本机IP
        :return:
        """
        self.ip_addr_le.clear()
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.ip_addr_le.setText(str(self.local_ip))
        print(self.local_ip)

    def send_data(self, data):
        """
        发送数据的统一接口
        :param data:
        :return:
        """
        if self.net_type_cbb.currentIndex() in [0, 1]:
            if self.tcp_send(data):
                return True
        elif self.net_type_cbb.currentIndex() in [2, 3]:
            if self.udp_send(data):
                return True

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

    def parse_recv_data(self, frame):
        """
        从底层ARM板 接收到的消息，在此解析
        :param data:
        :return:
        """
        recvd_msg = list(frame)
        if recvd_msg[0] == 0x5A and recvd_msg[1] == 0xA5: # 接收到帧头
            tot_len = recvd_msg[2] * 256 + recvd_msg[3]  # 取出长度
            if recvd_msg[tot_len - 1] == 0xFF:  # 帧尾
                device_type = recvd_msg[5] # 设备类型
                op_code = recvd_msg[6]  # 操作码
                data = recvd_msg[7] * 256 * 256 * 256 + recvd_msg[8] * 256 * 256 + recvd_msg[9] * 256 + recvd_msg[10]

                # 解析云台
                if device_type == 0x01:
                    if op_code == 0x0F:
                        self.runinfo_signal.emit('方位到位', None)
                        if self.is_ptz_pitching_inplace:
                            self.ptz_inplace_le.setText('方位俯仰到位')
                        else:
                            self.ptz_inplace_le.setText('方位到位')
                        self.is_ptz_bearing_inplace = True
                    if op_code == 0x10:
                        self.runinfo_signal.emit('俯仰到位', None)
                        if self.is_ptz_bearing_inplace:
                            self.ptz_inplace_le.setText('方位俯仰到位')
                        else:
                            self.ptz_inplace_le.setText('俯仰到位')
                        self.is_ptz_pitching_inplace = True

                    if op_code == 0x11:
                        bearing = data
                        self.runinfo_signal.emit('收到方位： ' + str(float(bearing / 100)), None)
                        self.ptz_bearing_le.setText(str(float(bearing / 100)))
                    if op_code == 0x12:
                        pitching = data
                        self.runinfo_signal.emit('收到俯仰： ' + str(float(pitching / 100)), None)
                        self.ptz_pitching_le.setText(str(float(pitching / 100)))

                    if op_code == 0x13:
                        velocity = data
                        self.runinfo_signal.emit('收到云台速度： ' + str(float(velocity / 100)), None)
                        self.ptz_velocity_le.setText(str(float(velocity / 100)))
                # 局放
                if device_type == 0x02:
                    if op_code == 0x02:
                        self.runinfo_signal.emit('局放结果值： ' + str(float(data / 100)), None)
                        self.partialdischarge_result_le.setText(str(float(data / 100)))
                # 行走电机
                if device_type == 0x03:
                    if op_code == 0x08:
                        self.runinfo_signal.emit('行走电机位置： ' + str(float(data / 100)), None)
                        self.walkmotor_pos_le.setText(str(float(data / 100)))
                    if op_code == 0x0B:
                        self.runinfo_signal.emit('行走电机速度： ' + str(float(data / 100)), None)
                        self.walkmotor_velocity_le.setText(str(float(data / 100)))
                    if op_code == 0x0c:
                        self.is_walkmotor_inplace = True
                        self.walkmotor_inplace_le.setText('到位')

                if device_type == 0x04:
                    if op_code == 0x02:
                        self.runinfo_signal.emit('条形码位置： ' + str(float(data / 100)), None)
                        self.barcode_position_le.setText(str(float(data / 100)))


                if device_type == 0x05:
                    if op_code == 0x04:
                        self.runinfo_signal.emit('升降杆到位', None)
                        self.is_lift_inplace = True
                        self.lifter_inplace_le.setText('到位')
                    if op_code == 0x06:
                        self.runinfo_signal.emit('升降杆位置： ' + str(float(data / 100)), None)
                        self.lifter_pos_le.setText(str(float(data / 100)))

                if device_type == 0x06:
                    if op_code == 0x01:
                        if data & 0x01:
                            self.runinfo_signal.emit('光电开关1 开启', None)
                        if data & 0x02:
                            self.runinfo_signal.emit('光电开关2 开启', None)
                        if data & 0x04:
                            self.runinfo_signal.emit('光电开关3 开启', None)
                        if data & 0x08:
                            self.runinfo_signal.emit('光电开关4 开启', None)
                        if data & 0x10:
                            self.runinfo_signal.emit('光电开关5 开启', None)
                        if data & 0x20:
                            self.runinfo_signal.emit('光电开关6 开启', None)
                        if data == 0x00:
                            self.runinfo_signal.emit('光电开关关闭', None)

                if device_type == 0x07:
                    if op_code == 0x02:
                        self.runinfo_signal.emit('霍尔结果值： ' + str(float(data / 100)), None)
                if device_type == 0x08:
                    if op_code == 0x02:
                        self.runinfo_signal.emit('测距结果值： ' + str(float(data / 100)), None)


    def send_debug_msg(self):
        msg = str(self.send_debug_msg_te.toPlainText())
        self.runinfo_signal.emit('发送：' + msg + '\n')
        # print('msg1: ', msg, type(msg))
        if self.send_hex_data_cb.isChecked():
            msg = msg.replace(' ', '')
            if len(msg) % 2:
                msg = msg[0: -1] + '0' + msg[-1]
            msg = bytearray.fromhex(msg)
        else:
            msg = msg.encode('utf-8')

        if self.send_debug_msg_btn.text() == '发送':
            self.send_period = int(self.cycle_send_period_ms_le.text())
            if self.send_period == 0:
                self.send_data(msg)
            else:
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
            self.runinfo_signal.emit('发送：' + msg + '\n')
            # print('msg1: ', msg, type(msg))
            if self.send_hex_data_cb.isChecked():
                msg = msg.replace(' ', '')
                if len(msg) % 2:
                    msg = msg[0: -1] + '0' + msg[-1]
                msg = bytearray.fromhex(msg)
            else:
                msg = msg.encode('utf-8')

            self.send_data(msg)
            time.sleep(self.send_period / 1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ORIR_Debug_Client()
    with open('../resources/Qss/wineRed.qss', encoding='utf-8') as stylesheet:
        window.setStyleSheet(stylesheet.read())

    window.setWindowTitle('挂轨机器人通信调试上位机 V0.3.0 2020-05-21 by Yi')
    window.show()
    sys.exit(app.exec_())

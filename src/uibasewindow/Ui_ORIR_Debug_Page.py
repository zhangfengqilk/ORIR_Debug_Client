# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ORIR_Debug_Page.ui',
# licensing of 'ORIR_Debug_Page.ui' applies.
#
# Created: Thu Jul  9 17:46:03 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ORIR_Debug_Page(object):
    def setupUi(self, ORIR_Debug_Page):
        ORIR_Debug_Page.setObjectName("ORIR_Debug_Page")
        ORIR_Debug_Page.resize(992, 725)
        self.gridLayout_23 = QtWidgets.QGridLayout(ORIR_Debug_Page)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.groupBox = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.net_type_cbb = QtWidgets.QComboBox(self.groupBox)
        self.net_type_cbb.setObjectName("net_type_cbb")
        self.net_type_cbb.addItem("")
        self.net_type_cbb.addItem("")
        self.net_type_cbb.addItem("")
        self.net_type_cbb.addItem("")
        self.gridLayout.addWidget(self.net_type_cbb, 0, 1, 1, 2)
        self.port_le = QtWidgets.QLineEdit(self.groupBox)
        self.port_le.setObjectName("port_le")
        self.gridLayout.addWidget(self.port_le, 2, 1, 1, 2)
        self.ip_addr_le = QtWidgets.QLineEdit(self.groupBox)
        self.ip_addr_le.setObjectName("ip_addr_le")
        self.gridLayout.addWidget(self.ip_addr_le, 1, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.net_connect_btn = QtWidgets.QPushButton(self.groupBox)
        self.net_connect_btn.setObjectName("net_connect_btn")
        self.gridLayout.addWidget(self.net_connect_btn, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.get_local_ip_btn = QtWidgets.QPushButton(self.groupBox)
        self.get_local_ip_btn.setObjectName("get_local_ip_btn")
        self.gridLayout.addWidget(self.get_local_ip_btn, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.com_interface_cbb = QtWidgets.QComboBox(self.groupBox)
        self.com_interface_cbb.setObjectName("com_interface_cbb")
        self.com_interface_cbb.addItem("")
        self.com_interface_cbb.addItem("")
        self.gridLayout_2.addWidget(self.com_interface_cbb, 0, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ptz_stop_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_stop_btn.setObjectName("ptz_stop_btn")
        self.gridLayout_3.addWidget(self.ptz_stop_btn, 1, 2, 1, 1)
        self.ptz_rightup_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_rightup_btn.setObjectName("ptz_rightup_btn")
        self.gridLayout_3.addWidget(self.ptz_rightup_btn, 0, 3, 1, 1)
        self.ptz_rightdown_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_rightdown_btn.setObjectName("ptz_rightdown_btn")
        self.gridLayout_3.addWidget(self.ptz_rightdown_btn, 2, 3, 1, 1)
        self.ptz_right_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_right_btn.setObjectName("ptz_right_btn")
        self.gridLayout_3.addWidget(self.ptz_right_btn, 1, 3, 1, 1)
        self.ptz_leftdown_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_leftdown_btn.setObjectName("ptz_leftdown_btn")
        self.gridLayout_3.addWidget(self.ptz_leftdown_btn, 2, 1, 1, 1)
        self.ptz_up_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_up_btn.setObjectName("ptz_up_btn")
        self.gridLayout_3.addWidget(self.ptz_up_btn, 0, 2, 1, 1)
        self.ptz_leftup_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_leftup_btn.setObjectName("ptz_leftup_btn")
        self.gridLayout_3.addWidget(self.ptz_leftup_btn, 0, 1, 1, 1)
        self.ptz_down_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_down_btn.setObjectName("ptz_down_btn")
        self.gridLayout_3.addWidget(self.ptz_down_btn, 2, 2, 1, 1)
        self.ptz_left_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_left_btn.setObjectName("ptz_left_btn")
        self.gridLayout_3.addWidget(self.ptz_left_btn, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ptz_velocity_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.ptz_velocity_le.setObjectName("ptz_velocity_le")
        self.gridLayout_4.addWidget(self.ptz_velocity_le, 1, 1, 1, 1)
        self.ptz_set_velocity_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_set_velocity_btn.setObjectName("ptz_set_velocity_btn")
        self.gridLayout_4.addWidget(self.ptz_set_velocity_btn, 1, 0, 1, 1)
        self.ptz_query_velocity_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_query_velocity_btn.setObjectName("ptz_query_velocity_btn")
        self.gridLayout_4.addWidget(self.ptz_query_velocity_btn, 1, 2, 1, 1)
        self.ptz_set_zero_position_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_set_zero_position_btn.setObjectName("ptz_set_zero_position_btn")
        self.gridLayout_4.addWidget(self.ptz_set_zero_position_btn, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.ptz_poweron_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_poweron_btn.setObjectName("ptz_poweron_btn")
        self.gridLayout_4.addWidget(self.ptz_poweron_btn, 2, 1, 1, 1)
        self.ptz_poweroff_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_poweroff_btn.setObjectName("ptz_poweroff_btn")
        self.gridLayout_4.addWidget(self.ptz_poweroff_btn, 2, 2, 1, 1)
        self.ptz_inplace_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.ptz_inplace_le.setObjectName("ptz_inplace_le")
        self.gridLayout_4.addWidget(self.ptz_inplace_le, 0, 1, 1, 2)
        self.gridLayout_6.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ptz_pitching_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.ptz_pitching_le.setObjectName("ptz_pitching_le")
        self.gridLayout_5.addWidget(self.ptz_pitching_le, 1, 1, 1, 2)
        self.ptz_set_pitching_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_set_pitching_btn.setObjectName("ptz_set_pitching_btn")
        self.gridLayout_5.addWidget(self.ptz_set_pitching_btn, 1, 0, 1, 1)
        self.ptz_set_bearing_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_set_bearing_btn.setObjectName("ptz_set_bearing_btn")
        self.gridLayout_5.addWidget(self.ptz_set_bearing_btn, 0, 0, 1, 1)
        self.ptz_bearing_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.ptz_bearing_le.setObjectName("ptz_bearing_le")
        self.gridLayout_5.addWidget(self.ptz_bearing_le, 0, 1, 1, 2)
        self.ptz_query_bearing_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_query_bearing_btn.setObjectName("ptz_query_bearing_btn")
        self.gridLayout_5.addWidget(self.ptz_query_bearing_btn, 0, 3, 1, 1)
        self.ptz_query_pitching_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_query_pitching_btn.setObjectName("ptz_query_pitching_btn")
        self.gridLayout_5.addWidget(self.ptz_query_pitching_btn, 1, 3, 1, 1)
        self.ptz_set_bearing_pitching_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_set_bearing_pitching_btn.setObjectName("ptz_set_bearing_pitching_btn")
        self.gridLayout_5.addWidget(self.ptz_set_bearing_pitching_btn, 2, 0, 1, 1)
        self.ptz_query_bearing_pitching_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.ptz_query_bearing_pitching_btn.setObjectName("ptz_query_bearing_pitching_btn")
        self.gridLayout_5.addWidget(self.ptz_query_bearing_pitching_btn, 2, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_2, 0, 1, 2, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_21.setContentsMargins(9, 20, -1, -1)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.runinfo_te = QtWidgets.QTextEdit(self.groupBox_11)
        self.runinfo_te.setObjectName("runinfo_te")
        self.gridLayout_21.addWidget(self.runinfo_te, 1, 0, 1, 4)
        self.cycle_send_period_ms_le = QtWidgets.QLineEdit(self.groupBox_11)
        self.cycle_send_period_ms_le.setObjectName("cycle_send_period_ms_le")
        self.gridLayout_21.addWidget(self.cycle_send_period_ms_le, 4, 0, 1, 1)
        self.clear_runinfo_btn = QtWidgets.QPushButton(self.groupBox_11)
        self.clear_runinfo_btn.setObjectName("clear_runinfo_btn")
        self.gridLayout_21.addWidget(self.clear_runinfo_btn, 2, 3, 1, 1)
        self.send_debug_msg_btn = QtWidgets.QPushButton(self.groupBox_11)
        self.send_debug_msg_btn.setObjectName("send_debug_msg_btn")
        self.gridLayout_21.addWidget(self.send_debug_msg_btn, 4, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_11)
        self.label_14.setObjectName("label_14")
        self.gridLayout_21.addWidget(self.label_14, 0, 0, 1, 1)
        self.send_debug_msg_te = QtWidgets.QTextEdit(self.groupBox_11)
        self.send_debug_msg_te.setObjectName("send_debug_msg_te")
        self.gridLayout_21.addWidget(self.send_debug_msg_te, 3, 0, 1, 4)
        self.label_13 = QtWidgets.QLabel(self.groupBox_11)
        self.label_13.setObjectName("label_13")
        self.gridLayout_21.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_11)
        self.label_15.setObjectName("label_15")
        self.gridLayout_21.addWidget(self.label_15, 4, 1, 1, 1)
        self.send_hex_data_cb = QtWidgets.QCheckBox(self.groupBox_11)
        self.send_hex_data_cb.setChecked(True)
        self.send_hex_data_cb.setObjectName("send_hex_data_cb")
        self.gridLayout_21.addWidget(self.send_hex_data_cb, 4, 2, 1, 1)
        self.is_show_as_hex_cb = QtWidgets.QCheckBox(self.groupBox_11)
        self.is_show_as_hex_cb.setChecked(True)
        self.is_show_as_hex_cb.setObjectName("is_show_as_hex_cb")
        self.gridLayout_21.addWidget(self.is_show_as_hex_cb, 2, 2, 1, 1)
        self.gridLayout_21.setRowStretch(1, 5)
        self.gridLayout_21.setRowStretch(3, 2)
        self.gridLayout_22.addWidget(self.groupBox_11, 0, 2, 6, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.walkmotor_forward_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_forward_btn.setObjectName("walkmotor_forward_btn")
        self.gridLayout_7.addWidget(self.walkmotor_forward_btn, 2, 1, 1, 1)
        self.walkmotor_poweron_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_poweron_btn.setObjectName("walkmotor_poweron_btn")
        self.gridLayout_7.addWidget(self.walkmotor_poweron_btn, 0, 1, 1, 1)
        self.walkmotor_backward_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_backward_btn.setObjectName("walkmotor_backward_btn")
        self.gridLayout_7.addWidget(self.walkmotor_backward_btn, 2, 2, 1, 1)
        self.walkmotor_stop_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_stop_btn.setObjectName("walkmotor_stop_btn")
        self.gridLayout_7.addWidget(self.walkmotor_stop_btn, 3, 1, 1, 1)
        self.walkmotor_poweroff_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_poweroff_btn.setObjectName("walkmotor_poweroff_btn")
        self.gridLayout_7.addWidget(self.walkmotor_poweroff_btn, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 2, 3, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.walkmotor_set_pos_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_set_pos_btn.setObjectName("walkmotor_set_pos_btn")
        self.gridLayout_8.addWidget(self.walkmotor_set_pos_btn, 0, 0, 1, 1)
        self.walkmotor_pos_le = QtWidgets.QLineEdit(self.groupBox_3)
        self.walkmotor_pos_le.setObjectName("walkmotor_pos_le")
        self.gridLayout_8.addWidget(self.walkmotor_pos_le, 0, 1, 1, 1)
        self.walkmotor_query_pos_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_query_pos_btn.setObjectName("walkmotor_query_pos_btn")
        self.gridLayout_8.addWidget(self.walkmotor_query_pos_btn, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1)
        self.walkmotor_inplace_le = QtWidgets.QLineEdit(self.groupBox_3)
        self.walkmotor_inplace_le.setObjectName("walkmotor_inplace_le")
        self.gridLayout_8.addWidget(self.walkmotor_inplace_le, 1, 1, 1, 1)
        self.walkmotor_velocity_le = QtWidgets.QLineEdit(self.groupBox_3)
        self.walkmotor_velocity_le.setObjectName("walkmotor_velocity_le")
        self.gridLayout_8.addWidget(self.walkmotor_velocity_le, 2, 1, 1, 1)
        self.walkmotor_set_velocity_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_set_velocity_btn.setObjectName("walkmotor_set_velocity_btn")
        self.gridLayout_8.addWidget(self.walkmotor_set_velocity_btn, 2, 0, 1, 1)
        self.walkmotor_query_velocity_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.walkmotor_query_velocity_btn.setObjectName("walkmotor_query_velocity_btn")
        self.gridLayout_8.addWidget(self.walkmotor_query_velocity_btn, 2, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_3, 1, 0, 2, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.groupBox_7 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_16.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.partialdischarge_detect_btn = QtWidgets.QPushButton(self.groupBox_7)
        self.partialdischarge_detect_btn.setObjectName("partialdischarge_detect_btn")
        self.horizontalLayout_2.addWidget(self.partialdischarge_detect_btn)
        self.partialdischarge_result_le = QtWidgets.QLineEdit(self.groupBox_7)
        self.partialdischarge_result_le.setObjectName("partialdischarge_result_le")
        self.horizontalLayout_2.addWidget(self.partialdischarge_result_le)
        self.gridLayout_16.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_17.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.barcode_query_position_btn = QtWidgets.QPushButton(self.groupBox_8)
        self.barcode_query_position_btn.setObjectName("barcode_query_position_btn")
        self.horizontalLayout_3.addWidget(self.barcode_query_position_btn)
        self.barcode_position_le = QtWidgets.QLineEdit(self.groupBox_8)
        self.barcode_position_le.setObjectName("barcode_position_le")
        self.horizontalLayout_3.addWidget(self.barcode_position_le)
        self.gridLayout_17.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_8, 1, 0, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_18.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hall_query_position_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.hall_query_position_btn.setObjectName("hall_query_position_btn")
        self.horizontalLayout_4.addWidget(self.hall_query_position_btn)
        self.hall_position_le = QtWidgets.QLineEdit(self.groupBox_9)
        self.hall_position_le.setObjectName("hall_position_le")
        self.horizontalLayout_4.addWidget(self.hall_position_le)
        self.gridLayout_18.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_9, 2, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_19.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ranging_query_position_btn = QtWidgets.QPushButton(self.groupBox_10)
        self.ranging_query_position_btn.setObjectName("ranging_query_position_btn")
        self.horizontalLayout_5.addWidget(self.ranging_query_position_btn)
        self.ranging_position_le = QtWidgets.QLineEdit(self.groupBox_10)
        self.ranging_position_le.setObjectName("ranging_position_le")
        self.horizontalLayout_5.addWidget(self.ranging_position_le)
        self.gridLayout_19.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_10, 3, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_20, 2, 1, 3, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lifter_up_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.lifter_up_btn.setObjectName("lifter_up_btn")
        self.horizontalLayout.addWidget(self.lifter_up_btn)
        self.lifter_down_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.lifter_down_btn.setObjectName("lifter_down_btn")
        self.horizontalLayout.addWidget(self.lifter_down_btn)
        self.lifter_stop_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.lifter_stop_btn.setObjectName("lifter_stop_btn")
        self.horizontalLayout.addWidget(self.lifter_stop_btn)
        self.gridLayout_11.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lifter_inplace_le = QtWidgets.QLineEdit(self.groupBox_4)
        self.lifter_inplace_le.setObjectName("lifter_inplace_le")
        self.gridLayout_10.addWidget(self.lifter_inplace_le, 1, 1, 1, 1)
        self.lifter_pos_le = QtWidgets.QLineEdit(self.groupBox_4)
        self.lifter_pos_le.setObjectName("lifter_pos_le")
        self.gridLayout_10.addWidget(self.lifter_pos_le, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_10.addWidget(self.label_3, 1, 0, 1, 1)
        self.lifter_query_pos_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.lifter_query_pos_btn.setObjectName("lifter_query_pos_btn")
        self.gridLayout_10.addWidget(self.lifter_query_pos_btn, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 1, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_15.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.photoelectricswitch_5_le = QtWidgets.QLineEdit(self.groupBox_6)
        self.photoelectricswitch_5_le.setObjectName("photoelectricswitch_5_le")
        self.gridLayout_14.addWidget(self.photoelectricswitch_5_le, 3, 1, 1, 1)
        self.photoelectricswitch_2_le = QtWidgets.QLineEdit(self.groupBox_6)
        self.photoelectricswitch_2_le.setObjectName("photoelectricswitch_2_le")
        self.gridLayout_14.addWidget(self.photoelectricswitch_2_le, 0, 3, 1, 1)
        self.photoelectricswitch_1_le = QtWidgets.QLineEdit(self.groupBox_6)
        self.photoelectricswitch_1_le.setObjectName("photoelectricswitch_1_le")
        self.gridLayout_14.addWidget(self.photoelectricswitch_1_le, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_14.addWidget(self.label_7, 2, 0, 1, 1)
        self.photoelectricswitch_6_le = QtWidgets.QLineEdit(self.groupBox_6)
        self.photoelectricswitch_6_le.setObjectName("photoelectricswitch_6_le")
        self.gridLayout_14.addWidget(self.photoelectricswitch_6_le, 3, 3, 1, 1)
        self.photoelectricswitch_3_le = QtWidgets.QLineEdit(self.groupBox_6)
        self.photoelectricswitch_3_le.setObjectName("photoelectricswitch_3_le")
        self.gridLayout_14.addWidget(self.photoelectricswitch_3_le, 2, 1, 1, 1)
        self.photoelectricswitch_4_le = QtWidgets.QLineEdit(self.groupBox_6)
        self.photoelectricswitch_4_le.setObjectName("photoelectricswitch_4_le")
        self.gridLayout_14.addWidget(self.photoelectricswitch_4_le, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_14.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setObjectName("label_8")
        self.gridLayout_14.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_14.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setObjectName("label_12")
        self.gridLayout_14.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setObjectName("label_11")
        self.gridLayout_14.addWidget(self.label_11, 3, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_6, 4, 0, 2, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(ORIR_Debug_Page)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_13.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.statuslight_red_on_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.statuslight_red_on_btn.setObjectName("statuslight_red_on_btn")
        self.gridLayout_12.addWidget(self.statuslight_red_on_btn, 0, 0, 1, 1)
        self.statuslight_yellow_on_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.statuslight_yellow_on_btn.setObjectName("statuslight_yellow_on_btn")
        self.gridLayout_12.addWidget(self.statuslight_yellow_on_btn, 0, 1, 1, 1)
        self.statuslight_green_on_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.statuslight_green_on_btn.setObjectName("statuslight_green_on_btn")
        self.gridLayout_12.addWidget(self.statuslight_green_on_btn, 1, 0, 1, 1)
        self.statuslight_all_off_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.statuslight_all_off_btn.setObjectName("statuslight_all_off_btn")
        self.gridLayout_12.addWidget(self.statuslight_all_off_btn, 1, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_5, 5, 1, 1, 1)
        self.gridLayout_22.setColumnStretch(0, 1)
        self.gridLayout_22.setColumnStretch(1, 1)
        self.gridLayout_22.setColumnStretch(2, 20)
        self.gridLayout_23.addLayout(self.gridLayout_22, 0, 0, 1, 1)

        self.retranslateUi(ORIR_Debug_Page)
        QtCore.QMetaObject.connectSlotsByName(ORIR_Debug_Page)

    def retranslateUi(self, ORIR_Debug_Page):
        ORIR_Debug_Page.setWindowTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "设置", None, -1))
        self.net_type_cbb.setItemText(0, QtWidgets.QApplication.translate("ORIR_Debug_Page", "TCP服务器", None, -1))
        self.net_type_cbb.setItemText(1, QtWidgets.QApplication.translate("ORIR_Debug_Page", "TCP客户端", None, -1))
        self.net_type_cbb.setItemText(2, QtWidgets.QApplication.translate("ORIR_Debug_Page", "UDP服务器", None, -1))
        self.net_type_cbb.setItemText(3, QtWidgets.QApplication.translate("ORIR_Debug_Page", "UDP客户端", None, -1))
        self.port_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "8881", None, -1))
        self.ip_addr_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "127.0.0.1", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  端  口", None, -1))
        self.net_connect_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "连接", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  IP地址", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "网络类型", None, -1))
        self.get_local_ip_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "获取本机IP", None, -1))
        self.com_interface_cbb.setItemText(0, QtWidgets.QApplication.translate("ORIR_Debug_Page", "GRPC 接口", None, -1))
        self.com_interface_cbb.setItemText(1, QtWidgets.QApplication.translate("ORIR_Debug_Page", "通信协议接口", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "云台", None, -1))
        self.ptz_stop_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "停", None, -1))
        self.ptz_rightup_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "右上", None, -1))
        self.ptz_rightdown_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "右下", None, -1))
        self.ptz_right_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "右", None, -1))
        self.ptz_leftdown_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "左下", None, -1))
        self.ptz_up_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "上", None, -1))
        self.ptz_leftup_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "左上", None, -1))
        self.ptz_down_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "下", None, -1))
        self.ptz_left_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "左", None, -1))
        self.ptz_velocity_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "5", None, -1))
        self.ptz_set_velocity_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "设置速度", None, -1))
        self.ptz_query_velocity_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "速度查询", None, -1))
        self.ptz_set_zero_position_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "云台校正", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "到位反馈", None, -1))
        self.ptz_poweron_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "上电", None, -1))
        self.ptz_poweroff_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "下电", None, -1))
        self.ptz_pitching_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "0.00", None, -1))
        self.ptz_set_pitching_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "设置俯仰", None, -1))
        self.ptz_set_bearing_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "设置方位", None, -1))
        self.ptz_bearing_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "0.00", None, -1))
        self.ptz_query_bearing_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "查询方位", None, -1))
        self.ptz_query_pitching_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "查询俯仰", None, -1))
        self.ptz_set_bearing_pitching_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "同时设置", None, -1))
        self.ptz_query_bearing_pitching_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "同时查询", None, -1))
        self.groupBox_11.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "调试框", None, -1))
        self.cycle_send_period_ms_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "0", None, -1))
        self.clear_runinfo_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "清除", None, -1))
        self.send_debug_msg_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "发送", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "接收框", None, -1))
        self.send_debug_msg_te.setHtml(QtWidgets.QApplication.translate("ORIR_Debug_Page", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">12345</span></p></body></html>", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "发送框", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "ms", None, -1))
        self.send_hex_data_cb.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "十六进制发送", None, -1))
        self.is_show_as_hex_cb.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "十六进制显示", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "行走电机", None, -1))
        self.walkmotor_forward_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "前进", None, -1))
        self.walkmotor_poweron_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "上电", None, -1))
        self.walkmotor_backward_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "后退", None, -1))
        self.walkmotor_stop_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "停", None, -1))
        self.walkmotor_poweroff_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "下电", None, -1))
        self.walkmotor_set_pos_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "设置位置", None, -1))
        self.walkmotor_pos_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "0.0", None, -1))
        self.walkmotor_query_pos_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "查询位置", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  到位反馈", None, -1))
        self.walkmotor_velocity_le.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "1", None, -1))
        self.walkmotor_set_velocity_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "设置速度", None, -1))
        self.walkmotor_query_velocity_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "速度查询", None, -1))
        self.groupBox_7.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "局放", None, -1))
        self.partialdischarge_detect_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "探测", None, -1))
        self.groupBox_8.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "条形码", None, -1))
        self.barcode_query_position_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "查询位置", None, -1))
        self.groupBox_9.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "霍尔", None, -1))
        self.hall_query_position_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "查询位置", None, -1))
        self.groupBox_10.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "测距", None, -1))
        self.ranging_query_position_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "查询位置", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "升降杆", None, -1))
        self.lifter_up_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "升", None, -1))
        self.lifter_down_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "降", None, -1))
        self.lifter_stop_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "停", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  到位反馈", None, -1))
        self.lifter_query_pos_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "查询位置", None, -1))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "光电开关", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  开关3：", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  开关1：", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  开关5：", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  开关2：", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  开关4：", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "  开关6：", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("ORIR_Debug_Page", "状态灯", None, -1))
        self.statuslight_red_on_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "红灯亮", None, -1))
        self.statuslight_yellow_on_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "黄灯亮", None, -1))
        self.statuslight_green_on_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "绿灯亮", None, -1))
        self.statuslight_all_off_btn.setText(QtWidgets.QApplication.translate("ORIR_Debug_Page", "灭", None, -1))


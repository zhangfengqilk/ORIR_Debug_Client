#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PySide2.QtWidgets import QWidget, QLabel, QPushButton, QToolButton, QVBoxLayout, QHBoxLayout, QApplication,QSizePolicy
from PySide2.QtCore import Qt, QPoint,QDateTime, QPointF, QRectF, QTimer
from PySide2.QtGui import QFont, QCursor, QIcon
from PySide2 import QtGui
from PySide2.QtGui import QColor, QPainter, QPen, QFont, QFontMetrics, QLinearGradient, QPixmap

"""
1. 标题栏背景颜色
"""


class QTitleLabel(QLabel):
    """
    新建标题栏标签类
    """

    def __init__(self, *args):
        super(QTitleLabel, self).__init__(*args)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFixedHeight(30)


class QStatusLabel(QLabel):
    """
    新建状态栏标签类
    """

    def __init__(self, *args):
        super(QStatusLabel, self).__init__(*args)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFixedHeight(30)
        self.setContentsMargins(10,0,10,0)


class QStatusTimeLabel(QLabel):
    """
    右下角状态栏上的显示日期时间的label
    """
    def __init__(self, *args):
        super(QStatusTimeLabel, self).__init__(*args)
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.setFixedHeight(30)
        self.setFixedWidth(160)
        self._time_update_timer = QTimer(self)
        self._time_update_timer.start(1000)
        self._time_update_timer.timeout.connect(self._on_update_datetime)
        self.setContentsMargins(0,0,10,0)

    def _on_update_datetime(self):
        current_time = QDateTime.currentDateTime()
        time_str = current_time.toString("yyyy年MM月dd日 hh:mm:ss")
        self.setText(time_str)


class QTitleButton(QPushButton):
    """
    新建标题栏按钮类
    """

    def __init__(self, *args):
        super(QTitleButton, self).__init__(*args)
        self.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self.setFixedWidth(40)


class QFramelessWindow(QWidget):
    """
    无边框窗口类
    """

    def __init__(self):
        super(QFramelessWindow, self).__init__(None, Qt.FramelessWindowHint)  # 设置为顶级窗口，无边框

        # ----------------属性值------------#
        self._m_window_width = 1000  # type: int  # 默认窗口的宽度
        self._m_window_height = 900  # type: int  # 默认窗口的高度
        self._m_window_minimum_width = 250  # type: int  # 最小窗口宽度
        self._m_window_minimum_height = 200  # type: int  # 最小窗口高度
        self._m_padding = 5  # type: int  # 边界宽度
        self._m_title_text = '无边框窗口'  # type: str  # 窗口标题文字
        self._m_icon_path = ''  # type: str # 窗口图标所在的路径
        self._m_title_height = 60  # type: int  # 窗口标题栏的高度
        self._m_title_text_width = 40  # type: int  # 标题文字所占的宽度
        self._m_title_label = QTitleLabel(self)  # type: QTitleLabel  # 用于显示标题
        self._m_title_position = 0  # type: int  # 标题的相对位置：0 - 靠左，1 - 水平居中
        self._m_status_label = QStatusLabel(self)
        self._m_status_time_label = QStatusTimeLabel(self)  #  右下角显示日期时间的label

        # 设置鼠标跟踪判断扳机默认值
        self._m_move_drag = False
        self._m_corner_drag = False
        self._m_bottom_drag = False
        self._m_right_drag = False

        self._m_close_btn = None  # type: QTitleButton  # 右上角的关闭按钮
        self._m_minimum_btn = None  # type: QTitleButton  # 右上角的最小化按钮
        self._m_maximum_btn = None  # type: QTitleButton  # 右上角的最大化按钮，有两种状态：最大化、回复正常

        self._m_main_layout = QVBoxLayout()

        self.setMinimumSize(self._m_window_minimum_width, self._m_window_minimum_height)
        # 设置窗口居中
        screen_w = QApplication.desktop().screenGeometry().width()
        screen_h = QApplication.desktop().screenGeometry().height()
        self.setGeometry((screen_w - self._m_window_width) / 2, (screen_h - self._m_window_height) / 2,
                         self._m_window_width, self._m_window_height)
        self.setMouseTracking(True)  # 设置widget鼠标跟踪
        self._init_title_label()
        self._init_status_label()


    # -----------------API 接口--------------------------#
    def add_close_button(self):
        """
        在右上角添加关闭按钮
        :return:
        """
        self._m_close_btn = QTitleButton(b'\xef\x81\xb2'.decode("utf-8"), self)

        # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
        self._m_close_btn.setObjectName("CloseButton")
        self._m_close_btn.setToolTip("关闭窗口")
        # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
        self._m_close_btn.setMouseTracking(True)
        # 设置按钮高度为标题栏高度
        self._m_close_btn.setFixedHeight(self._m_title_height)
        # 按钮信号连接到关闭窗口的槽函数
        self._m_close_btn.clicked.connect(self.close)
        # self._m_close_btn.setStyleSheet("QPushButton{background: transparent;}")
        self._m_close_btn.setFlat(True)

    def add_minimum_button(self):
        """
        在右上角添加最小化按钮
        :return:
        """
        self._m_minimum_btn = QTitleButton(b'\xef\x80\xb0'.decode("utf-8"), self)
        self._m_minimum_btn.setObjectName("MinMaxButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
        self._m_minimum_btn.setToolTip("最小化")
        self._m_minimum_btn.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
        self._m_minimum_btn.setFixedHeight(self._m_title_height)  # 设置按钮高度为标题栏高度
        self._m_minimum_btn.clicked.connect(self.showMinimized)  # 按钮信号连接到最小化窗口的槽函数
        self._m_minimum_btn.setFlat(True)

    def add_maximum_button(self):
        """
        在右上角添加最大化按钮
        :return:
        """
        self._m_maximum_btn = QTitleButton(b'\xef\x80\xb1'.decode("utf-8"), self)
        self._m_maximum_btn.setObjectName("MinMaxButton")  # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
        self._m_maximum_btn.setToolTip("最大化")
        self._m_maximum_btn.setMouseTracking(True)  # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
        self._m_maximum_btn.setFixedHeight(self._m_title_height)  # 设置按钮高度为标题栏高度
        self._m_maximum_btn.clicked.connect(self._on_set_window_maximum)  # 按钮信号连接切换到恢复窗口大小按钮函数
        # self._m_maximum_btn.setStyleSheet("QPushButton{background: transparent;}")
        self._m_maximum_btn.setFlat(True)

    def set_window_title(self, title: str) -> None:
        """
        设置窗口的标题
        :param title:标题
        :return:
        """
        f = QFont(QFont('Microsoft YaHei', 14))
        fm = QFontMetrics(f)
        self._m_title_text_width = fm.width(title)
        self._m_title_label.setFont(f)
        self._m_title_label.setText(title)
        self._m_title_text = title
        self.setWindowTitle(title)
        self.update()

    def set_window_icon(self, icon_path: str)->None:
        """
        设置窗口图标
        :param icon_path: 图标文件所在的路径
        :return:
        """
        self._m_icon_path = icon_path
        self.setWindowIcon(QIcon(icon_path))
        self.update()

    def set_window_title_height(self, height: int) -> None:
        """
        设置窗口标题栏的高度
        :param height: 标题栏高度
        :return: None
        """
        self._m_title_height = height
        self._init_title_label()
        self.set_window_title(self._m_title_text)
        self._m_close_btn.setFixedHeight(self._m_title_height)
        self._m_maximum_btn.setFixedHeight(self._m_title_height)
        self._m_minimum_btn.setFixedHeight(self._m_title_height)
        self.resize(self.size())
        self.update()

    def set_window_title_position(self, position: int) -> None:
        """
        设置标题的位置：1-靠右，2-水平居中
        :param position: 1或2
        :return:
        """
        self._m_title_position = position

    def set_layout(self, widget=None, layout=None) -> None:
        """
        向该无边框窗口中设置控件或布局，只能通过此函数添加控件或布局
        :param widget: 控件
        :param layout: 布局
        :return:
        """
        self._m_main_layout.setContentsMargins(0, 0, 0, 0)
        self._m_main_layout.setSpacing(0)
        self._m_main_layout.addSpacing(self._m_title_height)
        if widget:
            self._m_main_layout.addWidget(widget)
        if layout:
            self._m_main_layout.addLayout(layout)



        self._m_main_layout.addSpacing(self._m_status_label.height())

        self.setLayout(self._m_main_layout)

    def _init_title_label(self) -> None:
        """
        在主窗口界面上安放用于显示标题的label
        :return:
        """
        # 设置标题栏标签鼠标跟踪（如不设，则标题栏内在widget上层，无法实现跟踪）
        self._m_title_label.setMouseTracking(True)
        # 设置标题栏文本缩进
        self._m_title_label.setIndent(10)
        self._m_title_label.setFixedHeight(self._m_title_height)
        # 标题栏安放到左上角
        if self._m_title_position == 0:
            self._m_title_label.move(10, 0)
        else:
            self._m_title_label.move((self.width() - self._m_title_text_width) / 2, 0)

    def set_status_text(self, str='状态栏'):
        self._m_status_label.setText(str)

    def _init_status_label(self):
        """
        创建状态栏
        :return:
        """
        self._m_status_label.setMouseTracking(True)

    # -------------槽函数-----------------#

    def _on_set_window_maximum(self):
        """
        点击了最大化按钮，将窗口最大化
        :return:
        """
        try:
            self.showMaximized()  # 先实现窗口最大化
            self._m_maximum_btn.setText(b'\xef\x80\xb2'.decode("utf-8"))  # 更改按钮文本
            self._m_maximum_btn.setToolTip("恢复")  # 更改按钮提示
            self._m_maximum_btn.disconnect()  # 断开原本的信号槽连接
            self._m_maximum_btn.clicked.connect(self._on_set_window_normal)  # 重新连接信号和槽
        except:
            pass

    def _on_set_window_normal(self):
        """
        点击了最大化按钮，将窗口恢复正常大小
        :return:
        """
        try:
            self.showNormal()
            self._m_maximum_btn.setText(b'\xef\x80\xb1'.decode("utf-8"))
            self._m_maximum_btn.setToolTip("最大化")
            self._m_maximum_btn.disconnect()
            self._m_maximum_btn.clicked.connect(self._on_set_window_maximum)
        except:
            pass

    # -------------------重载事件响应函数--------------#
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """
        重载paintEvent函数
        :param a0:
        :return:
        """
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.save()
        p.setPen(Qt.NoPen)

        lgt = QLinearGradient(QPointF(0, 0), QPointF(self.width(), 0))
        lgt.setColorAt(0.0, QColor('#511235'))
        lgt.setColorAt(1.0, QColor('red'))
        p.setBrush(lgt)
        p.drawRect(QRectF(0, 0, self.width(), self._m_title_height))
        p.drawRect(QRectF(0, self.height()-self._m_status_label.height(), self.rect().width(), self._m_status_label.height()))
        line_pen = QPen()
        line_pen.setColor(QColor(30, 144, 255, 30))
        line_pen.setWidth(1)
        p.setPen(line_pen)
        p.drawLine(0, self.rect().height() - self._m_status_label.height(), self.rect().width(),
                   self.rect().height() - self._m_status_label.height())

        # 在窗口左上角画图标

        if self._m_icon_path:
            imx = QPixmap(self._m_icon_path)
            p.drawPixmap(5, (self._m_title_label.height() - imx.height()) / 2, imx)

        p.restore()

    def resizeEvent(self, QResizeEvent):
        # 将标题标签始终设为窗口宽度
        self._m_title_label.setFixedWidth(self._m_title_text_width * 2)
        if self._m_title_position == 0:
            if self._m_icon_path:
                imx = QPixmap(self._m_icon_path)
                self._m_title_label.move(imx.width() + 5, 0)
        else:
            self._m_title_label.move((self.width() - self._m_title_text_width) / 2, 0)

        self._m_status_label.move(0, self.rect().height() - self._m_status_label.height())
        self._m_status_label.setFixedWidth(self.rect().width()-self._m_status_time_label.width())
        self._m_status_time_label.move(self._m_status_label.width(), self.rect().height() - self._m_status_label.height())
        # 分别移动三个按钮到正确的位置
        try:
            self._m_close_btn.move(self.width() - self._m_close_btn.width(),
                                   (self._m_title_height - self._m_close_btn.height()) / 2)
        except:
            pass
        try:
            self._m_minimum_btn.move(self.width() - (self._m_close_btn.width() + 1) * 3 + 1,
                                     (self._m_title_height - self._m_close_btn.height()) / 2 - 4)
        except:
            pass
        try:
            self._m_maximum_btn.move(self.width() - (self._m_close_btn.width() + 1) * 2 + 1,
                                     (self._m_title_height - self._m_close_btn.height()) / 2)
        except:
            pass
        # 重新调整边界范围以备实现鼠标拖放缩放窗口大小，采用三个列表生成式生成三个列表
        self._right_rect = [QPoint(x, y) for x in range(self.width() - self._m_padding, self.width() + 1)
                            for y in range(1, self.height() - self._m_padding)]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - self._m_padding)
                             for y in range(self.height() - self._m_padding, self.height() + 1)]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - self._m_padding, self.width() + 1)
                             for y in range(self.height() - self._m_padding, self.height() + 1)]

    def mouseDoubleClickEvent(self, event):
        if (event.button() == Qt.LeftButton) and (event.y() < self._m_title_height):
            # 鼠标左键双击标题栏区域，切换界面最大化和最小化
            windowstate = int(self.windowState())
            if windowstate == 0:
                self._on_set_window_maximum()
            elif windowstate == 2:
                self._on_set_window_normal()

            event.accept()

    def mousePressEvent(self, event):
        # 重写鼠标点击的事件
        if (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
            # 鼠标左键点击右下角边界区域
            self._m_corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            # 鼠标左键点击右侧边界区域
            self._m_right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            # 鼠标左键点击下侧边界区域
            self._m_bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < self._m_title_height):
            # 鼠标左键点击标题栏区域
            self._m_move_drag = True
            self.move_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        # 判断鼠标位置切换鼠标手势
        if QMouseEvent.pos() in self._corner_rect:
            self.setCursor(Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        # 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        # 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if Qt.LeftButton and self._m_right_drag:
            # 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._m_bottom_drag:
            # 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._m_corner_drag:
            # 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._m_move_drag:
            # 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.move_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        重载 mouseReleaseEvent 函数
        鼠标释放后，各扳机复位
        :param a0: 事件，没有用上
        :return: None
        """
        self._m_move_drag = False
        self._m_corner_drag = False
        self._m_bottom_drag = False
        self._m_right_drag = False


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet(open("../../../resources/Qss/frameless.qss").read())
    window = QFramelessWindow()
    # window.setTitleLabel(True)
    # window.setPageButton('1', 0, True)
    window.add_close_button()
    window.add_maximum_button()
    window.add_minimum_button()

    window.set_window_title('无边框窗口测试长度测试')
    window.set_window_title_height(40)
    window.set_status_text()
    window.show()
    sys.exit(app.exec_())

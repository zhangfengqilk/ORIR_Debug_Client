#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: Yi
Version: 0.1
Date: 2019-10-23
License: MIT
State: 可以正常使用

可以滑动的导航栏，用于实验选项卡切换
可以设置的属性有：
1. item 周边的线条：上、下、左、右、矩形五种形式
2. item 周边的线条的颜色和宽度
3. item 的背景颜色
4. bar 的背景颜色
5. bar 的方向：横向、纵向
6. 初始选中的 item
7. item 的背景圆角
8. bar 的背景圆角
9. item 字体大小和字体类型
10. 滑动速度和晃动速度
11. 设置使用按键移动
12. 设置item大小是否固定
13. 设置item 的背景大小
"""
from PySide2.QtWidgets import QWidget,QSizePolicy
from PySide2.QtGui import QColor, QPainter, QPen, QFont, QFontMetrics, QLinearGradient
from PySide2.QtCore import Qt, QPointF, QRectF, QTimer, Signal
from PySide2 import QtGui
from enum import Enum


class QSlideNavigationBar(QWidget):
    class ItemLineStyle(Enum):
        ItemNone = 1
        ItemTop = 2
        ItemRight = 3
        ItemBottom = 4
        ItemLeft = 5
        ItemRect = 6

    itemClicked = Signal(int, str)

    def __init__(self):
        super(QSlideNavigationBar, self).__init__()

        # -------成员变量定义------------#
        # ==========属性=========#
        self._m_bar_start_color = QColor('#511235')  # type: QColor  # 导航栏起始颜色
        self._m_bar_end_color = QColor('#150507')  # type: QColor  # 导航栏结束颜色
        self._m_bar_radius = 0  # type: int     # 导航栏四个角的圆弧半径
        self._m_item_start_color = QColor(255, 255, 255, 50)  # type: QColor  # item 的起始颜色
        self._m_item_end_color = QColor("black")  # type: QColor  # item 的结束颜色
        self._m_current_hover_index = -1  # type: int    # 当前光标所在的item的index
        self._m_item_hover_start_color = QColor(255, 0, 0, 25)  # type: QColor   # 光标所在的item 的起始颜色
        self._m_item_hover_end_color = QColor(255, 0, 255, 25)  # type: QColor
        self._m_item_text_color = QColor("red")  # type: QColor  # item 的文字颜色
        self._m_item_line_color = QColor("red")  # type: QColor  # item 的线的颜色
        self._m_item_line_width = 5  # type: int     # 线的宽度
        self._m_item_line_style = self.ItemLineStyle.ItemNone  # type: QSlideNavigationBar.ItemLineStyle  # 线的样式类型
        self._m_item_font = QFont('宋体')  # type: QFont   # 字体家族
        self._m_item_font_size = 16  # type: int     # 字体大小
        self._m_item_radius = 0  # type: int     # item 的圆角半径
        self._m_space = 40  # type: int     # 间距大小, item 背景大小
        self._m_orientation = Qt.Horizontal  # type: Qt.Orientation  # 导航栏的方向：横向，纵向
        self._m_enable_key_move = True  # type: bool    # 是否可以使用按键切换item
        self._m_fixed = False  # type: bool    # 大小固定
        self._m_slide_velocity = 10  # type: int     # 滑动速度
        self._m_shake_velocity = 10  # type: int     # 晃动速度

        # ===========内部变量=========#
        self._m_item_maps = {}  # type: map(int, list(str, QRectF)) # 保存的item列表
        self._m_total_text_width = 0  # type: int     # 总的文字的宽度
        self._m_total_text_height = 0  # type: int     # 总的文字的高度
        self._m_current_index = 0  # type: int     # 当前选中的item 的索引
        self._m_start_rect = QRectF()  # type：QRectF  #起始矩形
        self._m_stop_rect = QRectF()  # type: QRectF  # 结束矩形
        self._m_slide_timer = QTimer(self)  # type: QTimer  # 滑动的定时器
        self._m_shake_timer = QTimer(self)  # type: QTimer  # 晃动的定时器
        self._m_forward = False  # type: bool    # 前进

        # ----------执行初始化动作-------------#
        self.setAttribute(Qt.WA_TranslucentBackground)
        self._m_slide_timer.setInterval(self._m_slide_velocity)
        self._m_slide_timer.timeout.connect(self._on_do_slide)
        self._m_shake_timer.setInterval(self._m_shake_velocity)
        self._m_shake_timer.timeout.connect(self._on_do_shake)

        self.setFocusPolicy(Qt.ClickFocus)
        self.setMouseTracking(True)

    # ---------以下是 API 接口----------#
    def add_item(self, item_str: str):
        """
        向导航栏中添加项目（代表一个选项卡），添加之前会查重
        :param item_str:项目名称（显示出来的文字）
        :return:None
        """
        if not item_str:
            return

        for key, value in self._m_item_maps.items():
            if value[0] == item_str:
                return  # 如果存在同名item，则返回

        f = QFont()
        f.setPointSize(self._m_item_font_size)
        fm = QFontMetrics(f)

        text_width = fm.width(item_str)
        text_height = fm.height()
        item_count = len(self._m_item_maps)
        if item_count > 0:
            if self._m_orientation == Qt.Horizontal:
                top_left = QPointF(self._m_total_text_width, 0)
                self._m_total_text_width += text_width + self._m_space
                bottom_right = QPointF(self._m_total_text_width, self._m_total_text_height)
            else:
                top_left = QPointF(0, self._m_total_text_height)
                self._m_total_text_height += text_height + self._m_space
                bottom_right = QPointF(self._m_total_text_width, self._m_total_text_height)

            self._m_item_maps[item_count] = [item_str, QRectF(top_left, bottom_right)]
        else:
            if self._m_orientation == Qt.Horizontal:
                # 水平方向，水平各占1个space， 竖直占1个space
                self._m_total_text_width = text_width + self._m_space
                self._m_total_text_height = text_height + self._m_space
            else:
                # 竖直方向， 水平各占2个space， 竖直占一个space
                self._m_total_text_width = text_width + 2 * self._m_space
                self._m_total_text_height = text_height + self._m_space

            top_left = QPointF(0.0, 0.0)
            bottom_right = QPointF(self._m_total_text_width, self._m_total_text_height)
            self._m_item_maps[item_count] = [item_str, QRectF(top_left, bottom_right)]
        self.setMinimumSize(self._m_total_text_width, self._m_total_text_height)

        if self._m_fixed:
            if self._m_orientation == Qt.Horizontal:
                self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)  # 固定高度
            else:
                self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)  # 固定宽度
        if len(self._m_item_maps):
            self._m_start_rect = QRectF(self._m_item_maps[0][1])
        self.update()

    def set_items(self, items_list: list):
        """
        一次性设置一组项目， 会清空之前设置的项目
        :param items_list: 项目名称列表
        :return: None
        """
        pass

    def get_items(self):
        pass

    def set_bar_start_color(self, color: QColor):
        """
        设置导航栏背景的起始颜色（渐变色的起始）
        :param color:QColor类型
        :return: None
        """
        if color != self._m_bar_start_color:
            self._m_bar_start_color = color
            self.update()

    def set_bar_end_color(self, color: QColor):
        """
        设置导航栏背景的结束颜色（渐变色的结束）
        :param color: QColor 类型
        :return: None
        """
        if color != self._m_bar_end_color:
            self._m_bar_end_color = color
            self.update()

    def set_item_start_color(self, color: QColor):
        """
        设置项目的背景色的起始颜色（渐变色的起始）
        :param color: QColor 类型
        :return: None
        """
        if color != self._m_item_start_color:
            self._m_item_start_color = color
            self.update()

    def set_item_end_color(self, color: QColor):
        """
        设置项目的背景色的结束颜色（渐变色的结束）
        :param color: QColor 类型
        :return: None
        """
        if color != self._m_item_end_color:
            self._m_item_end_color = color
            self.update()

    def set_item_text_color(self, color: QColor) -> None:
        """
        设置 item 的文字颜色
        :param color: QColor 类型
        :return:  None
        """
        if color != self._m_item_text_color:
            self._m_item_text_color = color
            self.update()

    def set_item_line_color(self, color: QColor) -> None:
        """
        设置 item 的线的颜色
        :param color: QColor 类型
        :return:  None
        """
        if color != self._m_item_line_color:
            self._m_item_line_color = color
            self.update()

    def set_bar_radius(self, radius: int):
        """
        设置导航栏四个角的圆弧半径
        :param radius: int 类型
        :return: None
        """
        if radius >= 0 and radius != self._m_bar_radius:
            self._m_bar_radius = radius
            self.update()

    def set_item_radius(self, radius: int):
        """
        设置项目的四个角的圆弧半径
        :param radius: int 类型
        :return: None
        """
        if radius >= 0 and radius != self._m_item_radius:
            self._m_item_radius = radius
            self.update()

    def set_space(self, space: int):
        """
        设置 item 所占的空间大小
        :param space: int 类型
        :return: None
        """
        if space >= 0 and space != self._m_space:
            self._m_space = space
            self.update()

    def set_item_line_width(self, width: int):
        """
        设置项目周围的线宽度
        :param width: int 类型
        :return: None
        """
        if width >= 0 and width != self._m_item_line_width:
            self._m_item_line_width = width
            self.update()

    def set_item_line_style(self, style: ItemLineStyle):
        """
        设置项目周围的线的类型：不显示，上方，下方，左方， 右方， 矩形
        :param style: 枚举类型
        :return: None
        """
        if style != self._m_item_line_style:
            self._m_item_line_style = style
            self.update()

    def set_orientation(self, orientation: Qt.Orientation):
        """
        设置导航栏是横向还是纵向
        :param orientation: Qt.Orientation 类型
        :return: None
        """
        if orientation != self._m_orientation:
            self._m_orientation = orientation
            self.update()

    def set_fixed(self, fixed: bool):
        """
        设置导航栏尺寸固定，不随窗口大小进行缩放
        :param fixed:  bool 类型
        :return:  None
        """
        if fixed != self._m_fixed:
            self._m_fixed = fixed
            self.update()

    def get_current_item_index(self):
        """
        返回当前选中项目的索引号
        :return: int类型，索引号
        """
        return self._m_current_index

    # -----------以下是槽函数--------------#
    def on_set_enable_key_move(self, enable: bool):
        """
        设置可以使用按键来切换导航项目
        :param enable: bool 类型
        :return: None
        """
        if enable != self._m_enable_key_move:
            self._m_enable_key_move = enable

    def on_move_to_first_item(self):
        """
        切换到第一个项目
        :return: None
        """
        self.on_move_to_index(0)

    def on_move_to_last_item(self):
        """
        切换到最后一个项目
        :return: None
        """
        self.on_move_to_index(len(self._m_item_maps) - 1)

    def on_move_to_previous_item(self):
        """
        切换到上一个项目
        :return: None
        """
        if self._m_current_index == 0:
            return
        self.on_move_to_index(self._m_current_index - 1)

    def on_move_to_next_item(self):
        """
        切换到下一个项目
        :return: None
        """
        if self._m_current_index == len(self._m_item_maps) - 1:
            return

        self.on_move_to_index(self._m_current_index + 1)

    def on_move_to_index(self, index: int):
        """
        切换到指定索引的项目
        :param index: int, 项目的索引号
        :return: None
        """
        if (index >= 0) and (index < len(self._m_item_maps)) and (index != self._m_current_index):
            self.itemClicked.emit(index, self._m_item_maps[index][0])
            if self._m_current_index == -1:
                self._m_start_rect = QRectF(self._m_item_maps[index][1])

            self._m_forward = index > self._m_current_index
            self._m_current_index = index
            self._m_stop_rect = QRectF(self._m_item_maps[index][1])
            self._m_slide_timer.start()

    def on_move_to_name(self, name: str):
        """
        切换到指定名称的项目
        :param name: 项目的名称，str类型
        :return: None
        """
        for key, value in self._m_item_maps.items():
            if value[0] == name:
                target_index = key
                if target_index == self._m_current_index:
                    return
                self.on_move_to_index(target_index)
                break

    def on_move_to_position(self, point: QPointF):
        """
        切换到指定位置的项目
        :param point: 位置坐标，QPointF类型
        :return: None
        """
        for key, value in self._m_item_maps.items():
            if value[1].contains(point):
                target_index = key
                if target_index == self._m_current_index:
                    return
                self.on_move_to_index(target_index)
                break

    def on_set_current_item_index(self, index: int):
        """
        将当前选中项目切换到指定索引的项目
        :param index: 索引号， int
        :return: NOne
        """
        self.on_move_to_index(index)

    # ------------以下是私有槽函数---------#
    def _on_do_slide(self):
        """
        完成滑动动作
        :return: None
        """
        if self._m_space <= 0 or self._m_start_rect == self._m_stop_rect:
            self.update()
            self._m_slide_timer.stop()
            return
        if self._m_orientation == Qt.Horizontal:
            dx = self._m_space / 2.0
            dy = 0
        else:
            dx = 0
            dy = self._m_space / 2.0

        if self._m_forward:
            self._m_start_rect.adjust(dx, dy, dx, dy)
            if ((self._m_orientation == Qt.Horizontal) and
                (self._m_start_rect.topLeft().x() >= self._m_stop_rect.topLeft().x())) or \
                    ((self._m_orientation == Qt.Vertical) and
                     (self._m_start_rect.topLeft().y() >= self._m_stop_rect.topLeft().y())):
                self._m_slide_timer.stop()
                if self._m_start_rect != self._m_stop_rect:
                    self._m_shake_timer.start()
        else:
            self._m_start_rect.adjust(-dx, -dy, -dx, -dy)
            if ((self._m_orientation == Qt.Horizontal) and
                (self._m_start_rect.topLeft().x() <= self._m_stop_rect.topLeft().x())) or \
                    ((self._m_orientation == Qt.Vertical) and
                     (self._m_start_rect.topLeft().y() <= self._m_stop_rect.topLeft().y())):
                self._m_slide_timer.stop()
                if self._m_start_rect != self._m_stop_rect:
                    self._m_shake_timer.start()
        self.update()

    def _on_do_shake(self):
        """
        完成晃动动作
        :return: None
        """
        delta = 2.0
        dx1 = dx2 = dy1 = dy2 = 0.0
        if self._m_start_rect.topLeft().x() > self._m_stop_rect.topLeft().x():
            dx1 = -delta
        elif self._m_start_rect.topLeft().x() < self._m_stop_rect.topLeft().x():
            dx1 = delta
        if self._m_start_rect.topLeft().y() > self._m_stop_rect.topLeft().y():
            dy1 = -delta
        elif self._m_start_rect.topLeft().y() < self._m_stop_rect.topLeft().y():
            dy1 = delta
        if self._m_start_rect.bottomRight().x() > self._m_stop_rect.bottomRight().x():
            dx2 = -delta
        elif self._m_start_rect.bottomRight().x() < self._m_stop_rect.bottomRight().x():
            dx2 = delta
        if self._m_start_rect.bottomRight().y() > self._m_stop_rect.bottomRight().y():
            dy2 = -delta
        elif self._m_start_rect.bottomRight().y() < self._m_stop_rect.bottomRight().y():
            dy2 = delta

        self._m_start_rect.adjust(dx1, dy1, dx2, dy2)

        if abs(self._m_start_rect.topLeft().x() - self._m_stop_rect.topLeft().x()) <= delta:
            self._m_start_rect.setLeft(self._m_stop_rect.topLeft().x())
        if abs(self._m_start_rect.topLeft().y() - self._m_stop_rect.topLeft().y()) <= delta:
            self._m_start_rect.setTop(self._m_stop_rect.topLeft().y())
        if abs(self._m_start_rect.bottomRight().x() - self._m_stop_rect.bottomRight().x()) <= delta:
            self._m_start_rect.setRight(self._m_stop_rect.bottomRight().x())
        if abs(self._m_start_rect.bottomRight().y() - self._m_stop_rect.bottomRight().y()) <= delta:
            self._m_start_rect.setBottom(self._m_stop_rect.bottomRight().y())
        if self._m_start_rect == self._m_stop_rect:
            self._m_shake_timer.stop()
        self.update()

    # -----------以下是事件响应函数的重载函数-----------#
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        """
        重载paintEvent函数
        :param a0:
        :return:
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self._draw_bar_background(painter)
        self._draw_item_background(painter)
        self._draw_item_line(painter)
        self._draw_text(painter)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """
        重载resizeEvent函数
        :param a0:
        :return:
        """
        self._adjust_item_size()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        重载mousePressEvent函数
        :param a0: 事件
        :return:None
        """
        self.on_move_to_position(a0.pos())

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        """
        重载mouseMoveEvent函数
        :param a0: 事件
        :return: None
        """
        is_on_item = False
        for key, value in self._m_item_maps.items():
            if value[1].contains(a0.pos()):
                self._m_current_hover_index = key
                is_on_item = True
                break
        if not is_on_item:
            self._m_current_hover_index = -1

        self.update()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        """
        重载keyPressEvent函数
        :param a0:
        :return:
        """
        if not self._m_enable_key_move:
            # self.keyPressEvent(a0)
            return
        if a0.key() == Qt.Key_Home:
            self.on_move_to_first_item()
        elif a0.key() == Qt.Key_End:
            self.on_move_to_last_item()
        elif a0.key() == Qt.Key_Up or a0.key() == Qt.Key_Left:
            self.on_move_to_previous_item()
        elif a0.key() == Qt.Key_Down or a0.key() == Qt.Key_Right:
            self.on_move_to_next_item()
        else:
            # self.keyPressEvent(a0)
            return

    # -----------------以下是私有成员函数---------------------#
    def _draw_bar_background(self, p: QPainter):
        """
        绘制导航栏的背景
        :param p: 画刷
        :return: None
        """
        p.save()
        p.setPen(Qt.NoPen)
        lgt = QLinearGradient(QPointF(0, 0), QPointF(0, self.height()))
        lgt.setColorAt(0.0, self._m_bar_start_color)
        lgt.setColorAt(1.0, self._m_bar_end_color)
        p.setBrush(lgt)
        p.drawRoundedRect(self.rect(), self._m_bar_radius, self._m_bar_radius)
        p.restore()

    def _draw_item_background(self, p: QPainter):
        """
        绘制项目的背景
        :param p: 画刷
        :return: None
        """
        if self._m_start_rect.isNull():
            return

        p.save()
        lgt = QLinearGradient(self._m_start_rect.topLeft(), self._m_start_rect.bottomRight())
        lgt.setColorAt(0.0, self._m_item_start_color)
        lgt.setColorAt(1.0, self._m_item_end_color)
        p.setPen(Qt.NoPen)
        p.setBrush(lgt)
        p.drawRoundedRect(self._m_start_rect, self._m_item_radius, self._m_item_radius)

        # 绘制 hover 状态下的item
        if self._m_current_hover_index != -1:
            hover_rect = QRectF(self._m_item_maps[self._m_current_hover_index][1])
            lgt = QLinearGradient(hover_rect.topLeft(), hover_rect.bottomRight())
            lgt.setColorAt(0.0, self._m_item_hover_start_color)
            lgt.setColorAt(1.0, self._m_item_hover_end_color)
            p.setPen(Qt.NoPen)
            p.setBrush(lgt)
            p.drawRoundedRect(hover_rect, self._m_item_radius, self._m_item_radius)
        p.restore()

    def _draw_item_line(self, p: QPainter) -> None:
        """
        绘制项目周边的线条
        :param p: 画刷
        :return: None
        """
        if self._m_start_rect.isNull():
            return

        if self._m_item_line_style == self.ItemLineStyle.ItemNone:
            return
        elif self._m_item_line_style == self.ItemLineStyle.ItemTop:
            p1 = self._m_start_rect.topLeft()
            p2 = self._m_start_rect.topRight()
        elif self._m_item_line_style == self.ItemLineStyle.ItemRight:
            p1 = self._m_start_rect.topRight()
            p2 = self._m_start_rect.bottomRight()
        elif self._m_item_line_style == self.ItemLineStyle.ItemBottom:
            p1 = self._m_start_rect.bottomLeft()
            p2 = self._m_start_rect.bottomRight()
        elif self._m_item_line_style == self.ItemLineStyle.ItemLeft:
            p1 = self._m_start_rect.topLeft()
            p2 = self._m_start_rect.bottomLeft()
        elif self._m_item_line_style == self.ItemLineStyle.ItemRect:
            p1 = self._m_start_rect.topLeft()
            p2 = self._m_start_rect.bottomRight()
        else:
            return

        p.save()
        line_pen = QPen()
        line_pen.setColor(self._m_item_line_color)
        line_pen.setWidth(self._m_item_line_width)
        p.setPen(line_pen)
        if self._m_item_line_style == self.ItemLineStyle.ItemRect:
            p.drawRoundedRect(QRectF(p1, p2), self._m_item_radius, self._m_item_radius)
        else:
            p.drawLine(p1, p2)

        p.restore()

    def _draw_text(self, p: QPainter) -> None:
        """
        绘制项目的名称
        :param p: 画刷
        :return: None
        """
        p.save()
        p.setPen(self._m_item_text_color)
        for key, value in self._m_item_maps.items():
            self._m_item_font.setPointSize(self._m_item_font_size)
            p.setFont(self._m_item_font)
            p.drawText(value[1], Qt.AlignCenter, value[0])
        p.restore()

    def _adjust_item_size(self) -> None:
        """
        调整Item大小
        :return:
        """

        if self._m_fixed:
            return

        item_count = len(self._m_item_maps)

        if self._m_orientation == Qt.Horizontal:
            add_width = 1.0 * (self.width() - self._m_total_text_width) / item_count
            add_height = 1.0 * (self.height() - self._m_total_text_height)
        else:
            add_width = 1.0 * (self.width() - self._m_total_text_width)
            add_height = 1.0 * (self.height() - self._m_total_text_height) / item_count

        dx = dy = 0.0
        for key, value in self._m_item_maps.items():
            # f = QFont()
            fm = QFontMetrics(self._m_item_font)
            text_width = fm.width(value[0])
            text_height = fm.height()
            if self._m_orientation == Qt.Horizontal:
                topLeft = QPointF(dx, 0)
                dx += text_width + self._m_space + add_width
                dy = self._m_total_text_height + add_height
            else:
                topLeft = QPointF(0, dy)
                dx = self._m_total_text_width + add_width
                dy += text_height + self._m_space + add_height

            bottomRight = QPointF(dx, dy)
            text_rect = QRectF(topLeft, bottomRight)
            self._m_item_maps[key] = [value[0], QRectF(text_rect)]
            if key == self._m_current_index:
                self._m_start_rect = text_rect
                self._m_stop_rect = text_rect

        self.update()

from src.depends.QSlideNavigationBar.QSlideNavigationBar import QSlideNavigationBar
from src.depends.FramelessWindow.FrameLessWindow import QFramelessWindow
from src.pages.ORIR_Debug_Page import ORIR_Debug
from src.pages.ORIR_LogAnalysis_Page import ORIR_LogAnalysis
from src.pages.ORIR_Collection_Data_Page import ORIR_CollectionData
from src.pages.ORIR_Debug_Help_Page import ORIR_Help
import sys
from PySide2.QtWidgets import QHBoxLayout, QApplication, QStackedWidget,QMessageBox
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt


class ORIRMain(QFramelessWindow):
    def __init__(self):
        super(ORIRMain, self).__init__()
        self._m_navigation_bar = QSlideNavigationBar()
        self._m_stacked_widget = QStackedWidget()
        self._m_stacked_widget.setMouseTracking(True)
        self._layout = QHBoxLayout()

        self._init_navigation_bar()
        self._layout.addWidget(self._m_navigation_bar)
        self._layout.addWidget(self._m_stacked_widget)
        self._layout.setStretchFactor(self._m_navigation_bar, 1)
        self._layout.setStretchFactor(self._m_stacked_widget, 40)
        self.set_layout(None, self._layout)

        self._debug_page = ORIR_Debug()
        self._m_stacked_widget.addWidget(self._debug_page)
        self._loganalysis_page = ORIR_LogAnalysis()
        self._m_stacked_widget.addWidget(self._loganalysis_page)
        self._collectiondata_page = ORIR_CollectionData()
        self._m_stacked_widget.addWidget(self._collectiondata_page)

        self._help_page = ORIR_Help()
        self._m_stacked_widget.addWidget(self._help_page)


        self._m_navigation_bar.itemClicked.connect(self._on_change_page)
        # self.set_window_icon('../resources/icons/battery.ico')
        self.setWindowFlags(Qt.FramelessWindowHint or Qt.WindowSystemMenuHint or Qt.WindowMinMaxButtonsHint)

    def _on_update_status_bar(self, str):
        """
        更新状态栏
        :param str:要更新的信息
        :return:
        """
        self.set_status_text(str)

    def _on_change_page(self, index: int, item_name: str):
        """
        切换页面的槽函数
        :param index:
        :param item_name:
        :return:
        """
        self._m_stacked_widget.setCurrentIndex(index)

    def _init_navigation_bar(self):
        """
        初始化导航栏
        :return: None
        """
        self._m_navigation_bar.set_orientation(Qt.Vertical)
        self._m_navigation_bar.set_fixed(True)
        self._m_navigation_bar.add_item('前期调试')
        self._m_navigation_bar.add_item('日志分析')
        self._m_navigation_bar.add_item('采点工具')
        self._m_navigation_bar.add_item('帮助')
        self._m_navigation_bar.set_item_line_style(QSlideNavigationBar.ItemLineStyle.ItemLeft)
        self._m_navigation_bar.set_item_line_color(QColor('red'))
        self._m_navigation_bar.setMaximumWidth(20)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ORIRMain()

    with open('../resources/Qss/wineRed.qss', encoding='utf-8') as stylesheet:
        window.setStyleSheet(stylesheet.read())  # 此处不可以设置app的stylesheet，否则弹出的matplotlib绘图会受到qss影响
    window.add_close_button()
    window.add_maximum_button()
    window.add_minimum_button()
    window.set_status_text()

    window.set_window_title('挂轨机器人调试上位机 V0.3.2 2020-05-25 by Yi')
    # window.set_window_title_height(40)
    window.show()
    sys.exit(app.exec_())

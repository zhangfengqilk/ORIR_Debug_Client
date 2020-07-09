from src.depends.QSlideNavigationBar.QSlideNavigationBar import QSlideNavigationBar
import sys
from PySide2.QtWidgets import QApplication

from PySide2.QtGui import QColor
from PySide2.QtCore import Qt

class SlideNavigator(QSlideNavigationBar):
    def __init__(self):
        super(SlideNavigator, self).__init__()
        # self.setupUi(self)
        # self.widget = QSlideNavigationBar()
        self.set_orientation(Qt.Vertical)
        self.add_item('系统设置1111')
        self.add_item('系统设置')
        self.add_item('防区管理')
        self.add_item('警情查询')
        self.set_item_text_color(QColor('yellow'))
        self.on_set_enable_key_move(True)
        self.set_space(25)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = SlideNavigator()
    s.show()
    sys.exit(app.exec_())
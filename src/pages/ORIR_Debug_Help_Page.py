from src.uibasewindow.Ui_ORIR_Debug_Help import Ui_ORIR_Debug_Help
from PySide2.QtWidgets import QWidget,QFileDialog

class ORIR_Help(QWidget, Ui_ORIR_Debug_Help):
    def __init__(self):
        super(ORIR_Help, self).__init__()
        self.setupUi(self)
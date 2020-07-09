from src.uibasewindow.Ui_ORIR_Debug_LogAnalysis_Page import Ui_ORIR_LogAnalysis_Page
from PySide2.QtWidgets import QWidget,QFileDialog


class ORIR_LogAnalysis(QWidget, Ui_ORIR_LogAnalysis_Page):
    def __init__(self):
        super(ORIR_LogAnalysis, self).__init__()
        self.setupUi(self)
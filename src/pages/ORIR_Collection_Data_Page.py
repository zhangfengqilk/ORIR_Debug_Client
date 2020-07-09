from src.uibasewindow.Ui_ORIR_Debug_Collectiong_Data_Page import Ui_ORIR_Debug_Collection_Data_Page
from PySide2.QtWidgets import QWidget,QFileDialog


class ORIR_CollectionData(QWidget, Ui_ORIR_Debug_Collection_Data_Page):
    def __init__(self):
        super(ORIR_CollectionData, self).__init__()
        self.setupUi(self)
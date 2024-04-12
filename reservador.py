from PyQt5.QtWidgets import QApplication
from gui.login import Login

class Reservador():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()
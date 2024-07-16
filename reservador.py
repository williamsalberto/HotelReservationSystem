from PyQt6.QtWidgets import QApplication
from login import Login

class Reservador():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()
        
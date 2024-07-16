<<<<<<< HEAD
from PyQt6.QtWidgets import QApplication
=======
from PyQt5.QtWidgets import QApplication
>>>>>>> 454cd2d8fd3bdcdae28015e1cb239bb809d007ab
from login import Login

class Reservador():
    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()
        
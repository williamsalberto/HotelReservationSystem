#En este archivo se hacen las importaciones necesarias para poder pintar el mainWindows de ui a .py

from PyQt5 import uic #Esta importacion convierte el .ui a un .py manipulable
from PyQt5.QtWidgets import QMessageBox
from conexion import conectar

# Clase MainWindows
class MainWindows():
    # Constructor
    def __init__(self):
        # conversion de .ui a .py
        self.mainWindows = uic.loadUi('gui/mainWindows.ui')
        self.mainWindows.show()
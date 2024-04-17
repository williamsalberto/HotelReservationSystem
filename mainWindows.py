#En este archivo se hacen las importaciones necesarias para poder pintar el mainWindows de ui a .py

from PyQt5 import uic #Esta importacion convierte el .ui a un .py manipulable
from PyQt5.QtWidgets import QMessageBox
from conexion import conectar
# Otras importaciones
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QPropertyAnimation

# Clase MainWindows
class MainWindows():
    # Constructor
    def __init__(self):
        # conversion de .ui a .py
        self.mainWindows = uic.loadUi('gui/mainWindows.ui')
        self.mainWindows.show()
        # acceder a paginas del stacked widgets
        # pagina de reservas
        self.mainWindows.bt_reservas.clicked.connect(lambda: self.mainWindows.stackedWidget.setCurrentWidget(self.mainWindows.page_reservar))
        # pagina de calendario
        self.mainWindows.bt_calendario.clicked.connect(lambda: self.mainWindows.stackedWidget.setCurrentWidget(self.mainWindows.page_calendario))
        # pagina de ver pagos
        self.mainWindows.bt_pagos.clicked.connect(lambda: self.mainWindows.stackedWidget.setCurrentWidget(self.mainWindows.page_verPagos))
        # pagina de ver deudas
        self.mainWindows.bt_deudas.clicked.connect(lambda: self.mainWindows.stackedWidget.setCurrentWidget(self.mainWindows.page_verDeudas))
        # pagina de proyeccion
        self.mainWindows.bt_proyeccion.clicked.connect(lambda: self.mainWindows.stackedWidget.setCurrentWidget(self.mainWindows.page_graficaMensual))

        # Ver menu lateral izquierdo
        self.mainWindows.pushButton_menu.clicked.connect(self.toggle_menu)

    def toggle_menu(self):
        self.mover_menu()

    def mover_menu(self):
        width = self.mainWindows.frame_lateral_izquierdo.width()
        normal = 0
        extender = 200 if width == 0 else normal
        self.mainWindows.frame_lateral_izquierdo.setMinimumWidth(extender)
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QPushButton

class VentanaPrincipal():
    def __init__(self):
        #Cargamos el archivo .ui de la vista
        self.main = uic.loadUi('gui/main.ui')
        self.inicializar_interfaz()
        #Mostramos la ventana
        self.main.show()
        self.main.icon_name_widget.setHidden(True)

        #Para cada boton del menu (minimizado o no), al ser clickeado, se llama al slot al que esta conectado
        #Esto para cambiar entre los indices de la pagina
        self.main.btnDashboard_1.clicked.connect(self.cambiar_pagina_dashboard)
        self.main.btnDashboard_2.clicked.connect(self.cambiar_pagina_dashboard)

        self.main.btnReservar_1.clicked.connect(self.cambiar_pagina_hacer_reserva)
        self.main.btnReservar_2.clicked.connect(self.cambiar_pagina_hacer_reserva)

        self.main.btnActualizar_1.clicked.connect(self.cambiar_pagina_actualizar_reserva)
        self.main.btnActualizar_2.clicked.connect(self.cambiar_pagina_actualizar_reserva)

        self.main.btnDeudas_1.clicked.connect(self.cambiar_pagina_deuda)
        self.main.btnDeudas_2.clicked.connect(self.cambiar_pagina_deuda)

        self.main.btnIngresos_1.clicked.connect(self.cambiar_pagina_pagos)
        self.main.btnIngresos_2.clicked.connect(self.cambiar_pagina_pagos)

        self.main.btnGrafico_1.clicked.connect(self.cambiar_pagina_grafico)
        self.main.btnGrafico_2.clicked.connect(self.cambiar_pagina_grafico)
    
    #Definimos los metodos para cada boton sea capaz de cambiar entre paginas
    def cambiar_pagina_dashboard(self):
        self.main.stackedWidget.setCurrentIndex(0)
    
    def cambiar_pagina_hacer_reserva(self):
        self.main.stackedWidget.setCurrentIndex(1)

    def cambiar_pagina_actualizar_reserva(self):
        self.main.stackedWidget.setCurrentIndex(2)

    def cambiar_pagina_deuda(self):
        self.main.stackedWidget.setCurrentIndex(3)
    def cambiar_pagina_pagos(self):
        self.main.stackedWidget.setCurrentIndex(4)

    def cambiar_pagina_grafico(self):
        self.main.stackedWidget.setCurrentIndex(5)
    
    def inicializar_interfaz(self):
         self.main.btnDashboard_1.clicked.connect(self.cambiar_pagina_dashboard)
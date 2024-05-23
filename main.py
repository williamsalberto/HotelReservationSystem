from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox, QPushButton
# Libreria para convertir texto a fecha
from datetime import datetime
# Importar conexion
import conexion as conexion 
class VentanaPrincipal():
    def __init__(self):
        #Cargamos el archivo .ui de la vista
        self.main = uic.loadUi('gui/main.ui')
        self.inicializar_interfaz()
        #Mostramos la ventana
        self.main.showMaximized()
        self.main.show()
        self.main.icon_name_widget.setHidden(True)

        #Para cada boton del menu (minimizado o no), al ser clickeado, se llama al slot al que esta conectado
        #Esto para cambiar entre los indices de la pagina
        self.main.btnDashboard_1.clicked.connect(self.cambiar_pagina_dashboard)
        self.main.btnDashboard_2.clicked.connect(self.cambiar_pagina_dashboard)

        self.main.btnAggHuesped_1.clicked.connect(self.cambiar_pagina_agg_huesped)
        self.main.btnAggHuesped_2.clicked.connect(self.cambiar_pagina_agg_huesped)

        self.main.btnHabitaciones_1.clicked.connect(self.cambiar_pagina_habitacion)
        self.main.btnHabitaciones_2.clicked.connect(self.cambiar_pagina_habitacion)

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

        # Botones de page registar huesped
        self.main.pushButton_Registrar.clicked.connect(self.registrar_huesped)
        self.main.pushButton_Limpiar.clicked.connect(self.limpiar_casillas_huesped)

        # Botones de page reservar
        self.main.pushButton_registrar_Reserva.clicked.connect(self.registrar_reserva)
        self.main.pushButton_limpiar_Reserva.clicked.connect(self.limpiar_casillas_reserva)
        # Rellenar select de page reservar
        self.main.comboBox_status_pago.addItem('SELECCIONA UNA OPCIÓN') 
        list_status = {'CANCELADO', 'POR CANCELAR'}
        for status in list_status:
                self.main.comboBox_status_pago.addItem(status) 
        self.main.comboBox_status_pago.setCurrentIndex(0)
    #Definimos los metodos para cada boton sea capaz de cambiar entre paginas
    def cambiar_pagina_dashboard(self):
        self.main.stackedWidget.setCurrentIndex(0)
    
    def cambiar_pagina_agg_huesped(self):
        self.main.stackedWidget.setCurrentIndex(1)

    def cambiar_pagina_habitacion(self):
        self.main.stackedWidget.setCurrentIndex(2)

    def cambiar_pagina_hacer_reserva(self):
        self.main.stackedWidget.setCurrentIndex(3)

    def cambiar_pagina_actualizar_reserva(self):
        self.main.stackedWidget.setCurrentIndex(4)

    def cambiar_pagina_deuda(self):
        self.main.stackedWidget.setCurrentIndex(5)

    def cambiar_pagina_pagos(self):
        self.main.stackedWidget.setCurrentIndex(6)

    def cambiar_pagina_grafico(self):
        self.main.stackedWidget.setCurrentIndex(7)

    def registrar_huesped(self):
        if self.main.lineEdit_cedula.text() != '':
            # Obtener los datos para registrar
            nombre = self.main.lineEdit_nombre.text()
            apellido = self.main.lineEdit_apellido.text()
            cedula = self.main.lineEdit_cedula.text()
            empresa = self.main.lineEdit_empresa.text()
            fechaNacimiento = self.main.lineEdit_fechaNacimiento.text()
            # transformar texto a fecha
            dia, mes, anio = self.obtener_componentes_fecha(fechaNacimiento)

            estadoCivil = self.main.lineEdit_estadoCivil.text()
            procedencia = self.main.lineEdit_procedencia.text()
            telefono = self.main.lineEdit_telefono.text()
            profesion = self.main.lineEdit_profesion.text()
            # registrar huesped
            conn = conexion.conectar()
            if conn:
                cursor = conn.cursor()
                try:
                    # Consulta para verificar que el cliente no existe
                    consultica = "SELECT * FROM huesped WHERE documento_identidad = %s"
                    cursor.execute(consultica, (cedula,))
                    resultado = cursor.fetchone()

                    # Si el resultado encuentra una coincidencia
                    if resultado:
                        QMessageBox.warning(self.main, "Aviso", "Ya existe un huesped con este documento de identidad.")
                    else:
                        # Registrar huesped si no hay coincidencia
                        consultica = "INSERT INTO huesped (nombre, apellido, documento_identidad, empresa, dia_nacimiento, mes_nacimiento, anio_nacimiento, edo_civil, procedencia, profesion, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        cursor.execute(consultica, (nombre, apellido, cedula, empresa, dia, mes, anio, estadoCivil, profesion, telefono, procedencia))
                        conn.commit()
                        QMessageBox.information(self.main, "Éxito", "Huesped registrado correctamente.")
                        self.limpiar_casillas_huesped()
                except Exception as e:
                    QMessageBox.critical(self.main, "Error", "Ocurrió un error al registrar el huesped:\n{}".format(str(e)))
                finally:
                    conn.close()
            else:
                QMessageBox.critical(self.main, "Error", "Ocurrió un error al conectar con la base de datos.")
        else:
                QMessageBox.critical(self.main, "Error", "Es obligatorio ingresar un documento de identidad.")        
    
    def limpiar_casillas_huesped(self):
        self.main.lineEdit_nombre.clear()
        self.main.lineEdit_apellido.clear()
        self.main.lineEdit_cedula.clear()
        self.main.lineEdit_empresa.clear()
        self.main.lineEdit_fechaNacimiento.clear()
        self.main.lineEdit_estadoCivil.clear()
        self.main.lineEdit_procedencia.clear()
        self.main.lineEdit_telefono.clear()
        self.main.lineEdit_profesion.clear()
        
    def inicializar_interfaz(self):
        self.main.btnDashboard_1.clicked.connect(self.cambiar_pagina_dashboard)

    # Convertir texto a fecha
    def obtener_componentes_fecha(self, texto):
        try:
            # Intenta convertir el texto en un objeto de fecha con el formato dd/mm/yyyy
            fecha = datetime.strptime(texto, '%d/%m/%Y')
        except ValueError:
            try:
                # Si no funciona, intenta convertir el texto en un objeto de fecha con el formato dd-mm-yyyy
                fecha = datetime.strptime(texto, '%d-%m-%Y')
            except ValueError:
                # Si ninguno de los formatos coincide, muestra un mensaje de error
                print("El formato de fecha no es válido.")
                return None, None, None
    
        # Obtener el día, mes y año por separado
        dia = fecha.day
        mes = fecha.month
        ano = fecha.year
    
        return dia, mes, ano

    def registrar_reserva(self):
        pass

    def limpiar_casillas_reserva(self):
        self.main.lineEdit_cliente_Reserva.clear()
        self.main.comboBox_habitacion.clear()
        self.main.lineEdit_monto_Cancelar.clear()
        self.main.comboBox_status_pago.setCurrentIndex(0)
        self.main.lineEdit_fecha_inicio_Reserva.clear()
        self.main.textEdit_nota_Reserva.clear()
        self.main.textEdit_nota_pago_Reserva.clear()
        self.main.textEdit_nota_reporte_Reserva.clear()

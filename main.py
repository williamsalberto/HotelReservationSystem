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
                self.main.comboBox_EstagoPagoActualizar.addItem(status) 
        
        self.main.comboBox_habitacion.addItem('SELECCIONA UNA HABITACION') 
        list_habitaciones = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15')
        for habitacion in list_habitaciones:
            self.main.comboBox_habitacion.addItem(habitacion)

        self.main.btn_BuscarReservaActualizar.clicked.connect(self.actualizar_reserva)
        self.main.btn_ActualizarReserva.clicked.connect(self.guardar_actualizacion_reserva)

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
        if self.main.lineEdit_cliente_Reserva.text() != '':
            #Obtenemos los datos para registrar una reserva
            cedula_cliente = self.main.lineEdit_cliente_Reserva.text()
            habitacion = self.main.comboBox_habitacion.text()
            #El nro de habitacion viene como string por lo tanto debe pasarse a entero para que coincida con la bd
            nro_habitacion = int(habitacion)
            monto_cancelar = self.main.lineEdit_monto_Cancelar.text()
            estado_pago = self.main.comboBox_status_pago.text()
            fecha_inicio = self.main.lineEdit_fecha_inicio_Reserva.text()
            fecha_salida = self.main.lineEdit_fecha_salida_Reserva.text()
            nota = self.main.textEdit_nota_Reserva.text()
            nota_de_pago = self.main.textEdit_nota_pago_Reserva.text()
            nota_reporte = self.main.textEdit_nota_reporte_Reserva.text()
            
            #Obtenemos por separado el día, mes y año de las fechas de inicio y salida
            dia_inicio, mes_inicio, anio_inicio = self.obtener_componentes_fecha(fecha_inicio)
            dia_salida, mes_salida, anio_salida = self.obtener_componentes_fecha(fecha_salida)
            
            #Pasamos a registrar la reserva, similar al registro de huéspedes
            conn = conexion.conectar()
            if conn:
                cursor = conn.cursor()
                try:
                    # Consultamos si el cliente (con su cédula de identidad) está registrado
                    consulta_cliente = "SELECT * FROM huesped WHERE documento_identidad = %s"
                    cursor.execute(consulta_cliente, (cedula_cliente,))
                    resultado_cliente = cursor.fetchone()
                    
                    if resultado_cliente:
                        #Verificamos si ya existe una reserva con los mismos valores
                        consulta_reserva = "SELECT * FROM reserva WHERE codigo_habitacion = %s AND codigo_huesped = %s AND dia_inicio = %s AND mes_inicio = %s AND anio_inicio = %s AND dia_fin = %s AND mes_fin = %s AND anio_fin = %s"
                        cursor.execute(consulta_reserva, (nro_habitacion, cedula_cliente, dia_inicio, mes_inicio, anio_inicio, dia_salida, mes_salida, anio_salida))
                        resultado_reserva = cursor.fetchone()
                        
                        if resultado_reserva:
                            QMessageBox.warning(self.main, "Aviso", "Ya existe una reserva con los mismos valores.")
                        else:
                            #Si no existe una idéntica, registramos la nueva reserva
                            consulta_insertar_reserva = "INSERT INTO reserva (codigo_habitacion, codigo_huesped, dia_inicio, mes_inicio, anio_inicio, dia_fin, mes_fin, anio_fin, nota_importante, nota_reporte_huesped, nota_pago, monto, estado_pago) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            cursor.execute(consulta_insertar_reserva, (nro_habitacion, cedula_cliente, dia_inicio, mes_inicio, anio_inicio, dia_salida, mes_salida, anio_salida, nota, nota_reporte, nota_de_pago, monto_cancelar, estado_pago))
                            conn.commit()
                            
                            #Obtenemos el ID de la reserva recién insertada
                            id_reserva = cursor.lastrowid
                            QMessageBox.information(self.main, "Éxito", f"Reserva registrada correctamente. ID de reserva: {id_reserva}")
                            self.limpiar_casillas_reserva()
                    else:
                        QMessageBox.warning(self.main, "Aviso", "No existe un huésped con el número de cédula especificado.")
                except Exception as e:
                    QMessageBox.critical(self.main, "Error", f"Ocurrió un error al registrar la reserva:\n{str(e)}")
                finally:
                    conn.close()

    def actualizar_reserva(self):
        codigo = self.main.lineEdit_IDReservaActualizar.text()
        if not codigo:
            QMessageBox.warning(self.main, "Aviso", "Ingresa un ID de reserva válido.")
            return

        try:
            codigo_reserva = int(codigo)
            conn = conexion.conectar()
            if conn:
                cursor = conn.cursor()
                
                #Consultamos los datos
                consulta = "SELECT dia_fin, mes_fin, anio_fin, monto, nota, nota_huesped, nota_reporte_pago FROM reserva WHERE codigo = %s"
                cursor.execute(consulta, (codigo_reserva,))
                resultado = cursor.fetchone()
                
                if resultado:
                    dia_fin, mes_fin, anio_fin, monto, nota, nota_huesped, nota_reporte_pago = resultado
                    self.main.lineEdit_DiaSalidaActualizar.setText(str(dia_fin))
                    self.main.lineEdit_MesSalidaActualizar.setText(str(mes_fin))
                    self.main.lineEdit_AnioSalidaActualizar.setText(str(anio_fin))
                    self.main.lineEdit_MontoActualizar.setText(str(monto))
                    self.main.textEdit_NotaActualizar.setPlainText(nota)
                    self.main.textEdit_NotaPagoActualizar.setPlainText(nota_reporte_pago)
                    self.main.textEdit_NotaHuespedActualizar.setPlainText(nota_huesped)
                else:
                    QMessageBox.warning(self.main, "Aviso", "No existe una reserva con el ID especificado.")

        except ValueError:
            QMessageBox.warning(self.main, "Error", "Ingresa un ID de reserva válido (número entero).")
        except Exception as e:
            QMessageBox.critical(self.main, "Error", f"Ocurrió un error al actualizar la reserva: {str(e)}")
        finally:
            if conn:
                conn.close()

    def guardar_actualizacion_reserva(self):
        codigo = self.main.lineEdit_IDReservaActualizar.text()
        dia_salida = self.main.lineEdit_DiaSalidaActualizar.text()
        mes_salida = self.main.lineEdit_MesSalidaActualizar.text()
        anio_salida = self.main.lineEdit_AnioSalidaActualizar.text()
        monto = self.main.lineEdit_MontoActualizar.text()
        nota = self.main.textEdit_NotaActualizar.toPlainText()
        nota_reporte_pago = self.main.textEdit_NotaPagoActualizar.toPlainText()
        nota_huesped = self.main.textEdit_NotaHuespedActualizar.toPlainText()
        
        try:
            codigo_reserva = int(codigo)
            conn = conexion.conectar()
            if conn:
                cursor = conn.cursor()
                #Actualizamos los datos en la base de datos
                consulta = """
                    UPDATE reserva
                    SET dia_fin = %s, mes_fin = %s, anio_fin = %s,
                        monto = %s, nota = %s, nota_huesped = %s, nota_reporte_pago = %s
                    WHERE codigo = %s
                """
                cursor.execute(consulta, (dia_salida, mes_salida, anio_salida,
                                      monto, nota, nota_huesped, nota_reporte_pago, codigo_reserva))
                conn.commit()
                QMessageBox.information(self.main, "Éxito", "Reserva actualizada correctamente.")
            else:
                QMessageBox.warning(self.main, "Error", "No se pudo conectar a la base de datos.")

        except ValueError:
            QMessageBox.warning(self.main, "Error", "Ingresa un ID de reserva válido (número entero).")
        except Exception as e:
            QMessageBox.critical(self.main, "Error", f"Ocurrió un error al actualizar la reserva: {str(e)}")
        finally:
            if conn:
                conn.close()



    def limpiar_casillas_reserva(self):
        self.main.lineEdit_cliente_Reserva.clear()
        self.main.comboBox_habitacion.clear()
        self.main.lineEdit_monto_Cancelar.clear()
        self.main.comboBox_status_pago.setCurrentIndex(0)
        self.main.lineEdit_fecha_inicio_Reserva.clear()
        self.main.textEdit_nota_Reserva.clear()
        self.main.textEdit_nota_pago_Reserva.clear()
        self.main.textEdit_nota_reporte_Reserva.clear()

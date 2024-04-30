#En este archivo se hacen las importaciones necesarias para poder pintar el login de ui a .py
from PyQt5 import uic #Esta importacion convierte el .ui a un .py manipulable
from PyQt5.QtWidgets import QMessageBox
import conexion as conexion 
from main import *
#Definimos nuestra clase de Login para tener sus funcionalidades y la conversion del archivo
class Login():
    def __init__(self):
        self.login = uic.loadUi('gui/loginfinal.ui')
        self.iniciar_interfaz()
        self.login.lblMensaje.setText("")
        self.login.show()
    
    def ingresar(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText("Ingrese un usuario valido")
            self.login.txtUsuario.setFocus()
        
        elif len(self.login.txtClave.text()) < 3:
            self.login.lblMensaje.setText("Ingrese una clave valida")
            self.login.txtClave.setFocus()
        
        else:
            try:
                conn = conexion.conectar()
                if conn:
                    cursor = conn.cursor()
                    #Consulta para validar las credenciales
                    consultica = "SELECT * FROM usuario_empleado WHERE alias = %s AND clave = %s"
                    cursor.execute(consultica, (self.login.txtUsuario.text(), self.login.txtClave.text()))
                    resultado = cursor.fetchone()

                    if resultado:
                        self.login.lblMensaje.setText("Bienvenido!")
                        self.main = VentanaPrincipal()
                        self.login.hide()
                    else:
                        self.login.lblMensaje.setText("Credenciales Incorrectas, intente nuevamente")
                    
                    conn.close()
                else:
                    self.login.lblMensaje.setText("Error al conectarse a la base de datos.")
            
            except Exception as e:
                print(f'Error al validar credenciales: {e}')
            
            finally:
                conn.close()
    
    def iniciar_interfaz(self):
        self.login.btnIngresar.clicked.connect(self.ingresar)    
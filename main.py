from ventana_ui4 import * 
from Logica.tabla import * 
from Logica.hokaCalc import * 
from Logica.letraCambio import * 

import shutil
import subprocess
_translate = QtCore.QCoreApplication.translate
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import os
import win32gui, win32con
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
class MainWindow(QtWidgets.QMainWindow, Ui_Huertas):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        
        self.btnContrato.clicked.connect(self.getFecha)
        self.btnInicial.clicked.connect(self.getFechaIni)
        self.btnCalcular.clicked.connect(self.calcular)
        
     
    #Funcionalidades de los botones
        
    def getFecha(self):
                fecha=self.calendarWidget.selectedDate()
                fecha=fecha.toString(Qt.ISODate)
                self.lineEdit.setText(fecha)
     
                
    def getFechaIni(self):
                fecha=self.calendarWidget.selectedDate()
                fecha=fecha.toString(Qt.ISODate)
                self.lineEdit_2.setText(fecha)
      
        
    def calcular(self):
                name=self.name.text()
                lastname=self.lastname.text()
                fullname=f'{name} {lastname}'
                dni=self.dni.text()
                dni=int(dni)
                importe=float(self.importe.text())
                inicial=float(self.inicial.text())
                pendiente=importe-inicial
                cuota=int(self.cuota.text())
                lote=self.lote.text()
                proyecto=str(self.comboBox.currentText())
                categoria=str(self.comboBox_2.currentText())
                
                if(self.radioButton_2.isChecked()):
                    moneda="Dolar"
                else:
                    moneda="Sol"
                fechaInicial=self.lineEdit_2.text()
                fechaContrato=self.lineEdit.text()
                tabla=[]
                tabla.append(importe)    
                tabla.append(inicial)    
                tabla.append(cuota)
                tabla.append(fechaInicial)
                tabla.append(fechaContrato)
                datos=Calculo(tabla)
                
                
               
                
                if(proyecto=='Olivar'):
                    if(self.radioButton_2.isChecked()):
                        fuente = "Plantilla/plantillaDolar-Olivar.xlsx"
                    else:
                        fuente = "Plantilla/plantillaSoles-Olivar.xlsx"
                if(proyecto=='Oasis'):
                    if(self.radioButton_2.isChecked()):
                        fuente = "Plantilla/plantillaDolar-Oasis.xlsx"
                    else:
                        fuente = "Plantilla/plantillaSoles-Oasis.xlsx"
                if(proyecto=='Apolo'):
                    if(self.radioButton_2.isChecked()):
                        fuente = "Plantilla/plantillaDolar-Apolo.xlsx"
                    else:
                        fuente = "Plantilla/plantillaSoles-Apolo.xlsx"
                
                resultado = "Pago-Cuotas.xlsx"
                print(categoria)
                archletras=f'{cuota}.xlsx'

                if(categoria=="Precio de Lote"):
                    fuenteletra=f'Plantilla/LetraCambio/lote/{archletras}'
                else:
                    fuenteletra=f'Plantilla/LetraCambio/habilitacion/{archletras}'
                        
                
                resultadoletra="letras.xlsx"
                
                shutil.copyfile(fuente, resultado)
                shutil.copyfile(fuenteletra, resultadoletra)
                dataExcel(proyecto,fullname,dni,tabla,datos,fechaContrato,moneda,pendiente,lote)
                
                 #letra de cambio 
                domicilio=self.domicilio.text()
                telefono=self.telefono.text()
                fiador=self.fiador.text()
                avalNombre=self.avalNombre.text()
                avalDomicilio=self.avalDomicilio.text()
                avalDOI=self.avalDOI.text()
                avalTelefono=self.avalTelefono.text()
                banco=self.banco.text()
                cuentabanco=self.cuentabanco.text()
                cci=self.cci.text()
                
                
                letraCambio(fullname,dni,tabla,datos,moneda,domicilio,telefono,fiador,avalNombre,avalDomicilio,avalDOI,avalTelefono,banco,cuentabanco,cci)
                
                os.startfile("letras.xlsx")
                os.startfile("Pago-Cuotas.xlsx")

                
                  
                
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
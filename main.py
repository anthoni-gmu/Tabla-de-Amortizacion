from ventana_ui import * 
from Logica.tabla import * 
from Logica.hokaCalc import * 
import shutil
import subprocess
_translate = QtCore.QCoreApplication.translate
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import os


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
                try:
                    dni=int(dni)
                except:
                    self.label_10.setText(_translate("Huertas", "<html><head/><body><p align=\"center\">DNI no valido!</p></body></html>"))
                importe=float(self.importe.text())
                inicial=float(self.inicial.text())
                pendiente=importe-inicial
                cuota=int(self.cuota.text())
                if(pendiente<=0):
                    self.label_10.setText(_translate("Huertas", "<html><head/><body><p align=\"center\">La inicial no puede ser igual o mayor al importe!</p></body></html>"))
                proyecto=str(self.comboBox.currentText())
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
    
                shutil.copyfile(fuente, resultado)
                dataExcel(proyecto,fullname,dni,tabla,datos,fechaContrato,moneda,pendiente)
                os.startfile("Pago-Cuotas.xlsx")

                
                  
                
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
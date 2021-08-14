from ui import * 
from datetime import datetime

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnContrato.clicked.connect(self.getFecha)
        self.btnInicial.clicked.connect(self.getFechaIni)
        
        
        
        
    def getFecha(self):
                fecha=self.calendarWidget.selectedDate()
                fecha=fecha.toString(Qt.ISODate)
                self.lineEdit.setText(fecha)
    def getFechaIni(self):
                fecha=self.calendarWidget.selectedDate()
                fecha=fecha.toString(Qt.ISODate)
                self.lineEdit_2.setText(fecha)
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
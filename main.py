from ui import * 
from datetime import datetime

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clicked)
    def clicked(self):
                # self.progressBar.setVisible(True)
                # correoEmisor=self.correo.text()
                # passEmisor=self.passs.text()
                fecha=self.calendarWidget.selectedDate()
                print(fecha.toString(Qt.ISODate))
                
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
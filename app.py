from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QGridLayout,QHBoxLayout
import sys
from PySide6.QtCore import Qt

from components.time_date import DateTime
from components.cpu import CPU
from components.ram import Ram
from components.disk import Disk
from components.system_info import SystemInfo
from components.plots import RamPlot,DiskPlot

class MainLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SYSVIEW")

        self.setGeometry(300,0,1000,600)

        mainbox = QGridLayout()
         
        mainbox.addWidget(DateTime(),0,0,1,20)
        mainbox.addWidget(SystemInfo(),2,0,15,5)

        mainbox.addWidget(RamPlot(),2,6,6,6)
        mainbox.addWidget(Ram(),8,6,5,7 )

        mainbox.addWidget(DiskPlot() ,2,13,6,7 )
        mainbox.addWidget(Disk(),8,13,4,7 )
        
        
        
        mainbox.addWidget(CPU(),14,6,8,14)
        
       

        self.setLayout(mainbox)




app = QApplication(sys.argv)
with open("components/style.css","r")as f:
    app.setStyleSheet(f.read())
window = MainLayout()
window.show()
app.exec()
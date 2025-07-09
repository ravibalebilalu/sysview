from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout
import sys
from PySide6.QtCore import Qt

from components.time_date import DateTime
from components.cpu import CPU
from components.ram import Ram

class MainLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SYSVIEW")

        self.setGeometry(300,0,1000,600)

        mainbox = QVBoxLayout()
        mainbox.addWidget(Ram())
        mainbox.addWidget(DateTime(),alignment=Qt.AlignmentFlag.AlignTop)
        mainbox.addWidget(CPU())

        self.setLayout(mainbox)




app = QApplication(sys.argv)
with open("components/style.css","r")as f:
    app.setStyleSheet(f.read())
window = MainLayout()
window.show()
app.exec()
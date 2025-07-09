import psutil

from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout,QListWidget
from PySide6.QtCore import Qt,QTimer

class Ram(QWidget):
    def __init__(self):
        super().__init__()
        self.ram_label = QLabel("Memory")
        self.ram_list = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_list)
        
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_ram_info)
        timer.start(1000)
        self.update_ram_info()

    def update_ram_info(self):
        self.ram_list.clear()
        mem = psutil.virtual_memory()
        info = [
            f"Total: {mem.total // (1024**2)} MB",
            f"Available: {mem.available // (1024**2)} MB",
            f"Used: {mem.used // (1024**2)} MB",
            f"Usage: {mem.percent} %"
        ]
        self.ram_list.addItems(info)

        

       


       




 

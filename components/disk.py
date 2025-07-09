import psutil

from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout,QListWidget
from PySide6.QtCore import Qt,QTimer

class Disk(QWidget):
    def __init__(self):
        super().__init__()

        self.disk_info_list = QListWidget()
        self.disk_label = QLabel("Disk")
        layout = QVBoxLayout()
        layout.addWidget(self.disk_label)
        layout.addWidget(self.disk_info_list)

        self.setLayout(layout)

        timer = QTimer()
        timer.timeout.connect(self.update_disk_info)
        timer.start(1000)
        self.update_disk_info()

    def update_disk_info(self):
        self.disk_info_list.clear()
        disk_info = psutil.disk_usage("/")
        info = [
            f"Total: {disk_info.total//(10**9)} GB", f"Used: {disk_info.used//(10**9)} GB", f"Free: {disk_info.free //(10 ** 9)} GB"
        ]
        self.disk_info_list.addItems(info)


#total=250373009408, used=112658259968, free=124921966592, percent=47.4

        

       


       




 

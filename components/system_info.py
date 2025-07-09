from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout
from PySide6.QtCore import Qt,QTimer
import  platform
import getpass
import datetime
import psutil



class SystemInfo(QWidget):
    def __init__(self):
        super().__init__()

        self.sys_label = QLabel("System Information")
         
        self.user_name_label = QLabel(f"User : {getpass.getuser()}")

        self.kernal_label = QLabel(f"Kernal : {platform.uname().system}")

        self.hostName = QLabel(f"Host : {platform.uname().node}")
        self.processor_label = QLabel(f"Processor : {platform.processor()}")
        self.arch_label = QLabel(f"Architecture : {platform.machine()}")
        self.os_version_label = QLabel(f"OS : {platform.system()} {platform.release()}")


        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        boot_time_str = boot_time.strftime("%d-%m-%Y %H:%M:%S")
        self.boot_time_label = QLabel(f"Boot Time : {boot_time_str}")
        self.uptime_label = QLabel("Up Time : ")


        
        

        layout = QVBoxLayout()
        layout.addWidget(self.sys_label)
        layout.addWidget(self.user_name_label)
        layout.addWidget(self.kernal_label)
        layout.addWidget(self.hostName)
        layout.addWidget(self.arch_label)
        layout.addWidget(self.os_version_label)
        layout.addWidget(self.processor_label)
        layout.addWidget(self.boot_time_label)
        layout.addWidget(self.uptime_label)
       

        self.setLayout(layout)


        
        timer = QTimer(self)
        timer.timeout.connect(self.update_uptime)
        timer.start(1000)

        self.update_uptime()

    def update_uptime(self):
        now = datetime.datetime.now()
         
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime = now - boot_time
        uptime_str = str(uptime).split('.')[0] 
        self.uptime_label.setText(f"Up Time : {uptime_str}")


         





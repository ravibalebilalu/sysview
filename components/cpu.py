from PySide6.QtWidgets import QLabel,QWidget,QVBoxLayout,QListWidget
import psutil

from PySide6.QtCore import QTimer,Qt
class CPU(QWidget):
    def __init__(self):
        super().__init__()
        #labels
        self.subheader = QLabel("CPU")
        self.current_usage_label = QLabel()
        self.physical_cores_label = QLabel()
        self.logical_cores_label = QLabel()
        self.freq_label = QLabel("Frequency")
        self.cpu_frequency_list = QListWidget()
        self.temp_label = QLabel("Temperature")
        self.cpu_temperature_list = QListWidget()
        #layout
        layout = QVBoxLayout()
        layout.addWidget(self.subheader)
        layout.addWidget(self.current_usage_label)
        layout.addWidget(self. physical_cores_label)
        layout.addWidget(self. logical_cores_label)
        layout.addWidget(self.freq_label)
        layout.addWidget(self.cpu_frequency_list)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.cpu_temperature_list)

        self.setLayout(layout)
        #timer
        timer = QTimer(self)
        timer.timeout.connect(self.update_cpu_percent)
        timer.timeout.connect(self.update_cores)
        timer.timeout.connect(self.update_cpu_fequency)
        timer.timeout.connect(self.update_cpu_temperature)
        timer.start(1000)
        self.update_cpu_percent()

    def update_cpu_percent(self):
        cpu_usage = psutil.cpu_percent()
        self.current_usage_label.setText(f"CPU usage : {cpu_usage}")

    def update_cores(self):
        physical_cpu_cores = psutil.cpu_count(logical=False)
        logical_cpu_cores = psutil.cpu_count(logical=True)
        self.physical_cores_label .setText(f"CPU cores(physical) : {physical_cpu_cores}")
        self.logical_cores_label .setText(f"CPU cores(logical) : {logical_cpu_cores }")

    def update_cpu_fequency(self):
        self.cpu_frequency_list.clear()
        frequencies= psutil.cpu_freq() 
        items = [
            f"Current : {frequencies.current:.2f} MH",
            f"Min : {frequencies.min:.2f} MH",
            f"Max : {frequencies.max:.2f} MH"
        ]
        self.cpu_frequency_list.addItems(items)
         

    def update_cpu_temperature(self):
        self.cpu_temperature_list.clear()
        temps = psutil.sensors_temperatures()
        tempList = []
        if "coretemp" in temps:
            for entry in temps["coretemp"]:
                tempList.append(f"{entry.label}: {entry.current} °C")
        self.cpu_temperature_list.addItems(tempList)
                
         
   
        

    #{'acpitz': [shwtemp(label='', current=27.8, high=106.0, critical=106.0), shwtemp(label='', current=29.8, high=106.0, critical=106.0)], 
     #'coretemp': [shwtemp(label='Package id 0', current=39.0, high=85.0, critical=105.0), shwtemp(label='Core 0', current=42.0, high=85.0, critical=105.0), shwtemp(label='Core 1', current=33.0, high=85.0, critical=105.0), shwtemp(label='Core 2', current=34.0, high=85.0, critical=105.0), shwtemp(label='Core 3', current=31.0, high=85.0, critical=105.0)]}




 
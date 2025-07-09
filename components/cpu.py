from PySide6.QtWidgets import QLabel,QWidget,QVBoxLayout,QListWidget,QHBoxLayout
import psutil

from PySide6.QtCore import QTimer,Qt
class CPU(QWidget):
    def __init__(self):
        super().__init__()
        #labels
        self.subheader = QLabel("CPU")
        self.subheader.setStyleSheet("font-size:25px;font-weight:bold;")
        self.current_usage_label = QLabel()
        self.physical_cores_label = QLabel()
        self.logical_cores_label = QLabel()
        self.freq_label = QLabel("Frequency")
        self.cpu_frequency_list = QListWidget()
         
        self.temp_label = QLabel("Temperature")
        self.cpu_temperature_list = QListWidget()
        #layout
        layout = QVBoxLayout()
        
        cpu_layout = QHBoxLayout()
        cpu_layout.addWidget(self.subheader)
        cpu_layout.addWidget(self.current_usage_label)
        cpu_layout.addWidget(self. physical_cores_label)
        cpu_layout.addWidget(self. logical_cores_label)
        
        cpu_widget = QWidget()
        cpu_widget.setStyleSheet("border:1px solid #555;")
        cpu_widget.setLayout(cpu_layout)
        layout.addWidget(cpu_widget)
         
        #frequency
        frequency_layout = QHBoxLayout()
        frequency_layout .addWidget(self.freq_label)
        frequency_layout.addWidget(self.cpu_frequency_list)
        frequency_widget = QWidget()
        frequency_widget.setStyleSheet("border:1px solid #555;")
        frequency_widget.setLayout(frequency_layout)
        layout.addWidget(frequency_widget)

        #temperature
        temperature_layout = QHBoxLayout()
        temperature_layout.addWidget(self.temp_label)
        temperature_layout.addWidget(self.cpu_temperature_list)
        temperature_widget = QWidget()
        temperature_widget.setLayout(temperature_layout)
        layout.addWidget(temperature_widget)

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
        self.current_usage_label.setText(f"CPU usage : {cpu_usage}%")

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




 
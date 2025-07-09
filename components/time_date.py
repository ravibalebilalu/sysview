from PySide6.QtWidgets import QWidget,QLabel,QHBoxLayout
from PySide6.QtCore import Qt,QTimer
from datetime import datetime


class DateTime(QWidget):
    def __init__(self):
        super().__init__()
        
        
        self.time_label = QLabel("Time")
        self.time_label.setObjectName("timelabel")
        self.date_label = QLabel("Date")
        self.date_label.setObjectName("datelabel")
        self.day_label = QLabel("Day")
        self.day_label.setObjectName("daylabel")

        for lb in [self.time_label,self.date_label,self.day_label]:
            lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        layout = QHBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)
        layout.addWidget(self.day_label)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        self.update_time()

    def update_time(self):
        curent_time_raw = datetime.now()
         
        self.time_label.setText(curent_time_raw.strftime("%I:%M:%S %p"))
        self.date_label.setText(curent_time_raw.strftime("%d %B %Y"))
        self.day_label.setText(curent_time_raw.strftime("%A"))


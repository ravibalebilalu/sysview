from PySide6.QtWidgets import QWidget,QVBoxLayout
from PySide6.QtCore import Qt,QTimer
import matplotlib.pyplot as plt
import seaborn as sns 
import psutil

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class RamPlot(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        sns.set_style("darkgrid")
        self.figure,self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setFixedSize(250, 225)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.draw_pie)
        timer.start(1000)
        self.draw_pie()


    def draw_pie(self):
        mem = psutil.virtual_memory()
        labels = ['Used', 'Free']
        sizes = [mem.used, mem.available]
        self.ax.clear()
        self.ax.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=140,colors=sns.color_palette("pastel"))
        self.ax.set_title("RAM USAGE")
        self.canvas.draw()


class DiskPlot(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        sns.set_style("darkgrid")
        self.figure,self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setFixedSize(250, 225)
        layout.addWidget(self.canvas)
        self.setLayout(layout)


        

        self.draw_pie()


    def draw_pie(self):
        disk = psutil.disk_usage("/")
        labels = ['Used', 'Free']
        sizes = [disk.used, disk.free]
        self.ax.clear()
        self.ax.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=140,colors=sns.color_palette("pastel"))
        self.ax.set_title("DISK USAGE")
        self.canvas.draw()





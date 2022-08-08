from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.widgets import DirectoryFinder
from schedule.publish import schedule


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("VideoEdit")
        width = 300
        height = 400
        self.setMinimumWidth(width)

        username_label = QLabel("Username")
        username_input = QLineEdit()
        start_button = QPushButton("Start")
        self.directory_widget = DirectoryFinder()
        self.calendar = QCalendarWidget()

        

        layout = QVBoxLayout()

        username_layout = QHBoxLayout()
        username_layout.addWidget(username_label)
        username_layout.addWidget(username_input)
        layout.addLayout(username_layout)

        layout.addWidget(self.directory_widget)
        layout.addWidget(self.calendar)
        layout.addWidget(start_button)
        
        self.setLayout(layout)

        start_button.clicked.connect(self.start_scheduling)

    def start_scheduling(self):
        date = self.calendar.selectedDate().getDate()
        schedule(self.directory_widget.file_directory, date)
        
    
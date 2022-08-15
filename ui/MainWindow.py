from inspect import getmembers
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui.widgets import DirectoryFinder, FileFinder
from schedule.publish import schedule

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # For custom stylesheets
        # sshFile="static/styles/style.qss"
        # with open(sshFile,"r") as fh:
        #     self.setStyleSheet(fh.read())

        self.setWindowTitle("VideoEdit")
        width = 350
        self.setMinimumWidth(width)

        layout = QVBoxLayout()

        desc_input = QTextEdit()
        tags_input = QLineEdit()

        start_button = QPushButton("Start")
        #self.selection = QRadioButton()
        self.directory_widget = DirectoryFinder()
        self.file_widget = FileFinder()
        self.calendar = QCalendarWidget()
        self.time = QTimeEdit()

        layout_form = QFormLayout()

        layout_form.addRow("Description", desc_input)
        layout_form.addRow("Tags", tags_input)
        layout.addLayout(layout_form)

        #layout.addWidget(self.selection)
        layout.addWidget(self.directory_widget)
        layout.addWidget(self.file_widget)
        layout.addWidget(self.calendar)
        layout.addWidget(self.time)
        layout.addWidget(start_button)
        
        self.setLayout(layout)

        start_button.clicked.connect(self.start_scheduling)

    def start_scheduling(self):
        date = self.calendar.selectedDate().getDate()
        schedule(self.directory_widget.file_directory, date)
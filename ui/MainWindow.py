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

        self.layout = QVBoxLayout()

        desc_input = QTextEdit()
        tags_input = QLineEdit()

        start_button = QPushButton("Start")
        self.directory_widget = DirectoryFinder()
        self.file_widget = FileFinder()
        self.calendar = QCalendarWidget()
        self.time = QTimeEdit()

        selection_layout = QHBoxLayout()
        self.selection_file = QRadioButton("Single Video")
        self.selection_file.setChecked(True)
        self.selection_file.toggled.connect(lambda:self.swap_filefolder(self.selection_file))

        self.selection_folder = QRadioButton("Folder")
        self.selection_file.toggled.connect(lambda:self.swap_filefolder(self.selection_folder))

        selection_layout.addWidget(self.selection_file)
        selection_layout.addWidget(self.selection_folder)

        layout_form = QFormLayout()

        layout_form.addRow("Description", desc_input)
        layout_form.addRow("Tags", tags_input)
        self.layout.addLayout(layout_form)

        self.layout.addLayout(selection_layout)
        self.layout.addWidget(self.file_widget)

        self.layout.addWidget(self.calendar)
        self.layout.addWidget(self.time)
        self.layout.addWidget(start_button)
        
        self.setLayout(self.layout)

        start_button.clicked.connect(self.start_scheduling)

    def start_scheduling(self):
        # File handling not supported in publish.py
        if(print(self.selection_file.isChecked())):
            print("Feature not supported")
            return

        date = self.calendar.selectedDate().getDate()
        time = (self.time.time().hour(), self.time.time().minute())
        schedule(self.directory_widget.file_directory, date, time)

    def swap_filefolder(self, state):

        if state.text() == "Single Video":
            if state.isChecked():
                self.layout.insertWidget(len(self.layout)-3, self.file_widget)
                self.directory_widget.deleteLater()
                self.directory_widget = DirectoryFinder()
        if state.text() == "Folder":
            if state.isChecked():
                self.layout.insertWidget(len(self.layout)-3, self.directory_widget)
                self.file_widget.deleteLater()
                self.file_widget = FileFinder()
                
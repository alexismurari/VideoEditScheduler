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

        self.getSettingsValues()

        self.setWindowTitle("VideoEdit")
        width = 350
        self.setMinimumWidth(width)

        height = self.setting_window.value('window_height')
        width = self.setting_window.value('window_width')

        self.layout = QVBoxLayout()

        desc_value = self.setting_variable.value('desc')
        self.desc_input = QTextEdit()
        self.desc_input.setText(desc_value)

        tags_value = self.setting_variable.value('tags')
        self.tags_input = QLineEdit()
        self.tags_input.setText(tags_value)

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

        layout_form.addRow("Description", self.desc_input)
        layout_form.addRow("Tags", self.tags_input)
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

        date = list(self.calendar.selectedDate().getDate())
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
                

    def getSettingsValues(self):
        self.setting_window = QSettings('videoedit', 'Window Size')
        self.setting_variable = QSettings('videoedit', 'Variables')
        print(self.setting_variable.fileName())

    def closeEvent(self, event):
        self.setting_window.setValue('window_height', self.rect().height())
        self.setting_window.setValue('window_width', self.rect().width())
        self.setting_variable.setValue('tags', self.tags_input.text())
        self.setting_variable.setValue('desc', self.desc_input.toPlainText())
        
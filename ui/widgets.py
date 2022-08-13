from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class DirectoryFinder(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        directory_label = QLabel("Directory")
        layout.addWidget(directory_label)
        
        self.folder_line = QLineEdit("Select Directory")
        self.folder_line.setEnabled(False)
        layout.addWidget(self.folder_line)

        folder_button = QPushButton("...")
        folder_button.clicked.connect(self.button_clicked)
        layout.addWidget(folder_button)

        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        self.file_directory = None

    def button_clicked(self):
        self.file_directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.folder_line.setText('{}'.format(self.file_directory))


class FileFinder(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        file_label = QLabel("File")
        layout.addWidget(file_label)
        
        self.file_line = QLineEdit("Select File")
        self.file_line.setEnabled(False)
        layout.addWidget(self.file_line)

        file_button = QPushButton("...")
        file_button.clicked.connect(self.button_clicked)
        layout.addWidget(file_button)

        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)

        self.file_path = None

    def button_clicked(self):
        self.file_path = str(QFileDialog.getOpenFileUrl(self, "Select Directory"))
        self.file_line.setText('{}'.format(self.file_path))
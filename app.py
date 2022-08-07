from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from ui import FileMenu

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VideoEdit")
        width = 300
        height = 400
        self.setMinimumSize(width, height)
                
        directory_widget = DirectoryFinder()
        self.setCentralWidget(directory_widget)


class DirectoryFinder(QWidget):
    def __init__(self):
        super().__init__()

        form_layout = QFormLayout()
        
        self.folder_line = QLineEdit("")
        self.folder_line.setEnabled(False)
        form_layout.addWidget(self.folder_line)

        folder_button = QPushButton("Video Directory")
        folder_button.clicked.connect(self.button_clicked)
        form_layout.addWidget(folder_button)

        self.setLayout(form_layout)


        

    def button_clicked(self):
        file_directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.folder_line.setText('{}'.format(file_directory))







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
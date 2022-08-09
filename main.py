from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# For the stylesheet templates
# Copyright (c) 2020, GCPDS
# All rights reserved.
# https://github.com/UN-GCPDS/qt-material
from qt_material import apply_stylesheet

from ui.MainWindow import MainWindow

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.show()
    app.exec()
from PyQt6.QtWidgets import *
from publish import *

def on_button_clicked():
    main()


if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()


    button = QPushButton('Click')
    button.clicked.connect(on_button_clicked)

    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    app.exec()



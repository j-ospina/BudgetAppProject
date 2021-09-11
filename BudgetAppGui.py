import os
import sys  
import random
from PySide6 import QtCore, QtWidgets, QtGui

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainWindow()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())


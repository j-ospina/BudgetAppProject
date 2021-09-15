import os
import sys  
import random
from PySide6 import QtCore, QtWidgets, QtGui

class monthlyTabLayout(QtWidgets.QHBoxLayout):
    def __init__(self) -> None:
        super().__init__()

        rightLayout = QtWidgets.QVBoxLayout()
        leftLayout = QtWidgets.QVBoxLayout()
        
        month = 'September'
        monthLabel = QtWidgets.QLabel(month)
        monthLabel.setTextFormat(QtCore.Qt.RichText)
        monthLabel.setText('<h1>'+month+'</h1>')

        leftLayout.addWidget(monthLabel)

        self.addLayout(leftLayout)
        self.addLayout(rightLayout)

class centralTabsWidget(QtWidgets.QTabWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setTabShape(QtWidgets.QTabWidget.Triangular)

        monthlyTab = QtWidgets.QWidget()
        monthlyTab.setLayout(monthlyTabLayout())
        self.addTab(monthlyTab,'Monthly Summary')

class menuWidget(QtWidgets.QMenuBar):
    def __init__(self) -> None:
        super().__init__()
        fileMenuWidget = QtWidgets.QMenu('File')
        self.addMenu(fileMenuWidget)

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        menuBar = menuWidget()
        centralTabs = centralTabsWidget()
        summaryDock = QtWidgets.QDockWidget()

        self.setMenuBar(menuBar)
        self.setCentralWidget(centralTabs)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, summaryDock)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainWindow()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())


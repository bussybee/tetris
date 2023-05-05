from PyQt5 import QtCore, QtGui, QtWidgets
from rool import Rool_MainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 586)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(44)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(211, 205, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rools = QtWidgets.QToolButton(self.centralwidget)
        self.rools.setEnabled(True)
        self.rools.setGeometry(QtCore.QRect(270, 330, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rools.setFont(font)
        self.rools.setStyleSheet("color: rgb(170, 0, 127);")
        self.rools.setObjectName("rools")
        self.start = QtWidgets.QToolButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(270, 230, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.start.setFont(font)
        self.start.setStyleSheet("color: rgb(170, 0, 127);")
        self.start.setAutoRepeat(True)
        self.start.setAutoRepeatDelay(300)
        self.start.setAutoRepeatInterval(101)
        self.start.setObjectName("start")
        self.tool = QtWidgets.QToolButton(self.centralwidget)
        self.tool.setGeometry(QtCore.QRect(270, 430, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tool.setFont(font)
        self.tool.setStyleSheet("color: rgb(170, 0, 127);")
        self.tool.setObjectName("tool")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(290, 80, 211, 111))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name.setStyleSheet("\n""color: rgb(85, 0, 127);")
        self.name.setFrame(True)
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tetris"))
        self.rools.setText(_translate("MainWindow", "Правила игры"))
        self.start.setText(_translate("MainWindow", "Начать"))
        self.tool.setText(_translate("MainWindow", "Настройки"))
        self.name.setText(_translate("MainWindow", "Tetris"))



    def show_rool(self):
        rool_window = QtWidgets.QMainWindow()
        ui = Rool_MainWindow()
        ui.setupUi(rool_window)
        rool_window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.rools.clicked.connect(ui.show_rool)
    MainWindow.show()
    sys.exit(app.exec_())

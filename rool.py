from PyQt5 import QtCore, QtGui, QtWidgets


class Rool_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(736, 600)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 222, 250);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text.setEnabled(False)
        self.text.setGeometry(QtCore.QRect(100, 220, 551, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text.setFont(font)
        self.text.setAcceptDrops(True)
        self.text.setStyleSheet("color: rgb(170, 85, 127);")
        self.text.setUndoRedoEnabled(True)
        self.text.setObjectName("text")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(310, 430, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.return_button.setFont(font)
        self.return_button.setStyleSheet("background-color: rgb(170, 170, 255);\n""color: rgb(85, 0, 127);")
        self.return_button.setObjectName("return_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 120, 201, 51))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Правила"))
        self.text.setPlainText(_translate("MainWindow", "Случайные фигурки тетрамино падают сверху в прямоугольный стакан шириной 10 и высотой 20 клеток. В полёте игрок может поворачивать фигурку на 90° и двигать её по горизонтали. Также можно «сбрасывать» фигурку, то есть ускорять её падение, когда уже решено, куда фигурка должна упасть"))
        self.return_button.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#aa557f;\">Правила игры</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Rool_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

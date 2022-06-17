import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from functools import partial


class Calculatrice(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Calculatrice LCD")
        self.setFixedSize(235, 235)
        self.disposition = QVBoxLayout()
        self._widget = QWidget(self)
        self.setCentralWidget(self._widget)
        self._widget.setLayout(self.disposition)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(15)
        self.lcd.setStyleSheet('background-color:black;')
        self.lcd.setFixedHeight(50)
        self.lcd.setContentsMargins(10, 10, 10, 10)
        self.lcd.display(9.87)
        self.disposition.addWidget(self.lcd, 1, Qt.AlignRight)



if __name__ == "__main__":
    pycalc = QApplication(sys.argv)
    vue = Calculatrice()
    vue.show()
    sys.exit(pycalc.exec_())

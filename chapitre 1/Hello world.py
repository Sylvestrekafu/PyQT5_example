import sys
from PyQt5.QtWidgets import QApplication, QWidget

application = QApplication(sys.argv)

widget = QWidget()

widget.resize(250, 250)
widget.setWindowTitle("Bonjour")
widget.show()

application.exec_()
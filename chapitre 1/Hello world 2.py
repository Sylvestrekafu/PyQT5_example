import sys
from PyQt5.QtWidgets import QApplication, QWidget

class FenetreSimple(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        self.resize(250, 300)
        self.move(50, 500)
        self.setWindowTitle("Bonjour ! " )
        self.show()

application = QApplication(sys.argv)

fenetre = FenetreSimple()

sys.exit(application.exec_())
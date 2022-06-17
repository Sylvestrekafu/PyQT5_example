import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap


class Fenetre(QWidget):

    def __init__(self):

        super().__init__()

        self.setGeometry(200, 100, 300, 100)
        self.setWindowTitle(" QPixmap2")
        self.disposition = QVBoxLayout()

        self.label = QLabel(self)
        self.image = QPixmap('pyqt.png')
        self.label.setPixmap(self.image)

        self.resize(self.image.width(), self.image.height())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = Fenetre()
    fenetre.show()
    sys.exit(app.exec_())
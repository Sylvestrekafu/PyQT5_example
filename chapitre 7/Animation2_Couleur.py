import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty

class LeLabel(QLabel):

    def __init__(self, texte):
        super().__init__(texte)

    def accesseurColorSet(self, couleur):
        palette = self.palette()
        palette.setColor(self.foregroundRole(), couleur)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=accesseurColorSet)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        self.bouton = QPushButton("Click animation", self)
        self.bouton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        hbox.addWidget(self.bouton)

        hbox.addSpacing(40)

        self.label = LeLabel("SYLVESTRE")
        font = self.label.font()
        font.setPointSize(40)
        self.label.setFont(font)
        hbox.addWidget(self.label)

        self.animation = QPropertyAnimation(self.label, b"color")
        self.animation.setDuration(2500)
        self.animation.setLoopCount(2)
        self.animation.setStartValue(QColor(255, 0, 0))
        self.animation.setEndValue(QColor(0, 0, 255))

        self.bouton.clicked.connect(self.animation.start)

        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Animation couleurs PyQt')
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()
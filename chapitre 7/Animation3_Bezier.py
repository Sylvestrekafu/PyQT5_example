import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QPixmap, QPainterPath
from PyQt5.QtCore import QObject, QPointF, QPropertyAnimation, pyqtProperty


class Italique(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        image = QPixmap("pyqt.png")
        self.h = image.height()
        self.w = image.width()
        self.setPixmap(image)

    def setPosition(self, pos):
        self.move(pos.x() - self.w / 2, pos.y() - self.h / 2)

    position = pyqtProperty(QPointF, fset=setPosition)


class Fenetre(QWidget):

    def __init__(self):
        super().__init__()

        self.vue()
        self.animation()

    def vue(self):
        self.path = QPainterPath()
        self.path.moveTo(15, 15)
        self.path.cubicTo(15, 15, 20, 325, 350, 190)

        self.italique = Italique(self)

        self.italique.pos = QPointF(30, 30)

        self.setWindowTitle("Animation d'une image le long d'une courbe de Bézier")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.drawPath(self.path)
        qp.end()

    def animation(self):
        self.animationBezier = QPropertyAnimation(self.italique, b'position')
        self.animationBezier.setDuration(8000)

        self.animationBezier.setStartValue(QPointF(30, 30))

        valeurs = [p / 100 for p in range(0, 101)]

        for i in valeurs:
            self.animationBezier.setKeyValueAt(i, self.path.pointAtPercent(i))

        self.animationBezier.setEndValue(QPointF(350, 30))
        self.animationBezier.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Fenetre()
    sys.exit(app.exec_())
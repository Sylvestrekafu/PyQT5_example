import sys
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsPixmapItem, QGraphicsScene)
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import (QObject, QPointF, QPropertyAnimation, pyqtProperty)


class Italique(QObject):

    def __init__(self):
        super().__init__()

        self.item = QGraphicsPixmapItem(QPixmap("pyqt.png"))

    def setPosition(self, pos):
        self.item.setPos(pos)

    pos = pyqtProperty(QPointF, fset=setPosition)


class Fenetre(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.vue()

    def vue(self):
        self.italique = Italique()

        self.animation = QPropertyAnimation(self.italique, b'pos')
        self.animation.setDuration(5000)
        self.animation.setStartValue(QPointF(30, 30))

        self.animation.setKeyValueAt(0.25, QPointF(100, 30))
        self.animation.setKeyValueAt(0.5, QPointF(30, 30))
        self.animation.setKeyValueAt(0.75, QPointF(275, 275))

        self.animation.setEndValue(QPointF(275, 30))

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.italique.item)
        self.setScene(self.scene)

        self.setWindowTitle("Chapitre 7 - scène graphique")
        self.setRenderHint(QPainter.Antialiasing)
        self.setGeometry(300, 300, 500, 400)

        self.animation.start()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Fenetre()
    sys.exit(app.exec_())
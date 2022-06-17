from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

app = QApplication([])

fenetre = QWidget()

fenetre.setGeometry(100, 100, 200, 100)
fenetre.setWindowTitle("QFormLayout")
disposition = QGridLayout()

disposition.addWidget(QPushButton("0"), 0, 0)
disposition.addWidget(QPushButton("1"), 0, 1)
disposition.addWidget(QPushButton("2"), 0, 2)
disposition.addWidget(QPushButton("3"), 1, 0)
disposition.addWidget(QPushButton("4"), 1, 1)
disposition.addWidget(QPushButton("5"), 1, 2)
disposition.addWidget(QPushButton("6"), 2, 0)
disposition.addWidget(QPushButton("7"), 2, 1)
disposition.addWidget(QPushButton("8"), 2, 2)
disposition.addWidget(QPushButton("9"), 3, 0)
disposition.addWidget(QPushButton("+"), 3, 1)
disposition.addWidget(QPushButton("="), 3, 2)

fenetre.setLayout(disposition)
fenetre.show()

app.exec_()
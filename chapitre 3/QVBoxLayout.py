from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

app = QApplication([])

fenetre = QWidget()

disposition = QHBoxLayout()
disposition.addWidget(QPushButton('Premier'))
disposition.addWidget(QPushButton('Second'))
disposition.addWidget(QPushButton('Troisième'))
disposition.addWidget(QPushButton('Quatrième'))
disposition.addWidget(QPushButton('Cinquième'))
fenetre.setLayout(disposition)

fenetre.show()
app.exec_()
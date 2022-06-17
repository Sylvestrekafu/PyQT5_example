from PyQt5.QtCore import *

maintenant = QDate.currentDate()

print(maintenant.toString(Qt.ISODate))
print(maintenant.toString(Qt.DefaultLocaleLongDate))

maintenant_datetime = QDateTime.currentDateTime()

print(maintenant_datetime.toString())

heure = QTime.currentTime()

print(heure.toString(Qt.DefaultLocaleLongDate))


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

def victory():
    victory_win = QMessageBox()
    victory_win.setText('Верно! Вы выиграли гироскутер')
    victory_win.exec_()
    main_win.close()
def los():
    lose = QMessageBox()
    lose.setText('Нет, в 2015 году. Вы выиграли фирменный плакат')
    lose.exec_()
    main_win.close()



app = QApplication([])
main_win = QWidget()
main_win.resize(800,500)
main_win.setWindowTitle('Конкурс от Crazy People')

question = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
rbtn = QRadioButton('2005')
rbtn1 = QRadioButton('2010')
rbtn2 = QRadioButton('2015')
rbtn3 = QRadioButton('2020')

HL1 = QHBoxLayout()
HL2 = QHBoxLayout()
HL3 = QHBoxLayout()
VL1 = QVBoxLayout()

HL1.addWidget(
    question, alignment = Qt.AlignCenter
    )
HL2.addWidget(
    rbtn, alignment = Qt.AlignCenter
    )
HL2.addWidget(
    rbtn1, alignment = Qt.AlignCenter
    )
HL3.addWidget(
    rbtn2, alignment = Qt.AlignCenter
    )
HL3.addWidget(
    rbtn3, alignment = Qt.AlignCenter
    )

VL1.addLayout(HL1)
VL1.addLayout(HL2)
VL1.addLayout(HL3)


rbtn2.clicked.connect(victory)
rbtn.clicked.connect(los)
rbtn1.clicked.connect(los)
rbtn3.clicked.connect(los)
main_win.setLayout(VL1)
main_win.show() 
app.exec_()
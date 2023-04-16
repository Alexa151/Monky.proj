from PyQt5.QtWidgets import*
app=QApplication([])
okno=QWidget()
okno.setWindowTitle('calculater')
okno.resize(650,600)

a=QLineEdit(okno)
b=QLineEdit(okno)
number1=QLineEdit
number2=QLineEdit

but1= QPushButton(okno)
but1.resize(60,40)
but1.move(500,200)

but2= QPushButton(okno)
but2.resize(30,20)
but2.move(250,250)
minus=QLabel(okno)
minus.setText('-')
minus.move(260,250)

a.move(100,200)
b.move(300,200)

plus=QLabel(okno)
plus.setText('+')
plus.move(255,200)

text2=QLabel(okno)#calculate!
text2.setText('Calculate!')
text2.move(510,210)
text3=QLabel(okno)
text3.setText('=')
text3.move(450,210)

result=()
def result1():
    global result
    a1 = a.text()
    b1 = b.text()
    text2.setText (str(int(a1)+int(b1)))
but1.clicked.connect(result1)
def minus():
    global result
    plus.setText('-')
but2.clicked.connect(minus)




okno.show()
app.exec_()
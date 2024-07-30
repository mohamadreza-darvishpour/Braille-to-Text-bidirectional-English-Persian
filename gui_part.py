https://pythonpyqt.com/pyqt-box-layout/








# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton)
# from PyQt5.QtGui import QFont

# class Example(QWidget):
  
#   def __init__(self):
#     super().__init__()
#     self.initUI()
  
#   def initUI(self):
#     QToolTip.setFont(QFont('Arial', 14))
#     self.setToolTip('Tooltip for <b>QWidget</b>')
#     btn = QPushButton('Button', self)
#     btn.setToolTip('Tooltip for <b>QPushButton</b>')
#     btn.resize(btn.sizeHint())
#     btn.move(50, 50)
#     self.setGeometry(300, 300, 300, 220)
#     self.setWindowTitle('PyQt Tooltip Demo')    
#     self.show()
  
# if __name__ == '__main__':
#   app = QApplication(sys.argv)
#   ex = Example()
#   sys.exit(app.exec_())





#custom signals.
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import pyqtSignal, QObject
 
# class Communicate(QObject):    #defines our custom signals here.
#     closeApp = pyqtSignal()
 
# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         self.c = Communicate()
#         self.c.closeApp.connect(self.close)
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Mouse events') 
#         self.show()
    
#     def mousePressEvent(self, event):   #mousepressevent is custom class in app
#         self.c.closeApp.emit()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())








# # how to get and enable changes . 
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# class Example(QMainWindow):

#     def __init__(self):
#          super().__init__()
#          self.initUI()

#     def initUI(self):
#         btn1 = QPushButton('One', self)
#         btn1.move(30, 50)
#         btn2 = QPushButton('Two', self)
#         btn2.move(150, 50)
#         btn1.clicked.connect(self.buttonClicked)   # when want to connect that to functions.
#         btn2.clicked.connect(self.buttonClicked)
#         self.statusBar()
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Window') 
#         self.show()

#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + ' changed')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# #set custom events. 
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtCore import Qt

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()
        
#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('PyQt events with keyboard') 
#         self.show()
        
#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Escape:
#             self.close()
    
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())










# #events is important to use .

# import sys

# from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLCDNumber, QVBoxLayout)
# from PyQt5.QtCore import Qt

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
        
#     def initUI(self):
#        lcd = QLCDNumber(self)
#        sld = QSlider(Qt.Horizontal, self)
#        vbox = QVBoxLayout()
#        vbox.addWidget(lcd)   #add lcd(widget ) to slider
#        vbox.addWidget(sld)  #add sld to slider too
#        self.setLayout(vbox)  #set layout . 
#        sld.valueChanged.connect(lcd.display) #when change the sld show on lcd. 
#        self.setGeometry(250, 250, 250, 150)
#        self.setWindowTitle('Events demo') 
#        self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())










# from PyQt5.QtWidgets import *
# import sys

# class QLabelBuddy(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('QLabel Buddy Demo')
#         self.setFixedWidth(250)

#         nameLabel = QLabel('&Name',self)
#         nameLineEdit = QLineEdit(self)
#         nameLabel.setBuddy(nameLineEdit)

#         passwordLabel = QLabel('&Password',self)
#         passwordLineEdit = QLineEdit(self)
#         passwordLabel.setBuddy(passwordLineEdit)

#         btnOK = QPushButton('&OK')
#         btnCancel = QPushButton('&Cancel')

#         mainLayout = QGridLayout(self)
#         mainLayout.addWidget(nameLabel,0,0)
#         mainLayout.addWidget(nameLineEdit,0,1,1,2)

#         mainLayout.addWidget(passwordLabel,1,0)
#         mainLayout.addWidget(passwordLineEdit,1,1,1,2)

#         mainLayout.addWidget(btnOK,2,1)
#         mainLayout.addWidget(btnCancel,2,2)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = QLabelBuddy()
#     main.show()
#     sys.exit(app.exec_())













# import sys
# from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget
# from PyQt5.QtGui import QPixmap, QPalette
# from PyQt5.QtCore import Qt

# class QLabelDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         label1 = QLabel(self)
#         label2 = QLabel(self)
#         label3 = QLabel(self)
#         label4 = QLabel(self)

#         label1.setText("<font color=yellow>PythonPyQt.com</font>")
#         label1.setAutoFillBackground(True)
#         palette = QPalette()
#         palette.setColor(QPalette.Window,Qt.blue)
#         label1.setPalette(palette)
#         label1.setAlignment(Qt.AlignCenter)

#         label2.setText("<a href='#'>QLabel2</a>")

#         label3.setAlignment(Qt.AlignCenter)
#         label3.setToolTip('Hint')
#         label3.setPixmap(QPixmap("python.png"))

#         label4.setOpenExternalLinks(True)
#         label4.setText("<a href='https://python.org'>Python.org</a>")
#         label4.setAlignment(Qt.AlignCenter)
#         label4.setToolTip('Python.org')

#         vbox = QVBoxLayout()

#         vbox.addWidget(label1)
#         vbox.addWidget(label2)
#         vbox.addWidget(label3)
#         vbox.addWidget(label4)

#         label2.linkHovered.connect(self.linkHovered)
#         label4.linkActivated.connect(self.linkClicked)

#         self.setLayout(vbox)
#         self.setWindowTitle('QLabel Demo')

#     def linkHovered(self):
#         print('Mouse hovered over the link')

#     def linkClicked(self):
#         print('Link was clicked')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = QLabelDemo()
#     main.show()
#     sys.exit(app.exec_())













# https://pythonpyqt.com/pyqt-label/


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle('Hello World')
#         self.show()

#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
#         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

















# from PyQt5.QtWidgets import QApplication, QWidget, QToolButton, QMainWindow
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt
# import sys

# class ToolButton(QMainWindow):

#     def __init__(self):
#         super(ToolButton,self).__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("ToolButton")
#         self.setGeometry(400,400,300,260)

#         self.toolbar = self.addToolBar("toolBar")
#         self.statusBar()
      
#         self._detailsbutton = QToolButton()                                     
#         self._detailsbutton.setCheckable(True)  # has 2 option on and off                                 
#         self._detailsbutton.setChecked(False)     # the button is not checked before when is false .                               
#         self._detailsbutton.setArrowType(Qt.RightArrow)
#         self._detailsbutton.setAutoRaise(True)
#         #self._detailsbutton.setIcon(QIcon("test.jpg"))
#         self._detailsbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
#         self._detailsbutton.clicked.connect(self.showDetail)
#         self.toolbar.addWidget(self._detailsbutton)

#     def showDetail(self):
#         if self._detailsbutton.isChecked():
#             self.statusBar().showMessage("Show Detail....")
#         else:
#             self.statusBar().showMessage("Close Detail....")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = ToolButton()
#     ex.show()
#     sys.exit(app.exec_()) 






# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import Qt
# import sys

# class PushButton(QWidget):
#     def __init__(self):
#         super(PushButton,self).__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("PushButton")
#         self.setGeometry(400,400,300,260)
#         self.closeButton = QPushButton(self)
#         self.closeButton.setText("Close")          #text
#         self.closeButton.setIcon(QIcon("close.png")) #icon
#         self.closeButton.setShortcut('Ctrl+D')  #shortcut key
#         self.closeButton.clicked.connect(self.close)
#         # when hover on option show set tooltip
#         self.closeButton.setToolTip("Close the widget") #Tool tip
#         self.closeButton.move(100,100)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = PushButton()
#     ex.show()
#     sys.exit(app.exec_()) 








# from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
# import sys

# class TextEditDemo(QWidget):
#         def __init__(self,parent=None):
#                 super().__init__(parent)

#                 self.setWindowTitle("QTextEdit")
#                 self.resize(300,270)

#                 self.textEdit = QTextEdit()
#                 self.btnPress1 = QPushButton("Button 1")
#                 self.btnPress2 = QPushButton("Button 2")

#                 layout = QVBoxLayout()
#                 layout.addWidget(self.textEdit)
#                 layout.addWidget(self.btnPress1)
#                 layout.addWidget(self.btnPress2)
#                 self.setLayout(layout)

#                 self.btnPress1.clicked.connect(self.btnPress1_Clicked)
#                 self.btnPress2.clicked.connect(self.btnPress2_Clicked)

#         def btnPress1_Clicked(self):
#                 self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

#         def btnPress2_Clicked(self):
#                 self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")

# if __name__ == '__main__':
#         app = QApplication(sys.argv)
#         win = TextEditDemo()
#         win.show()
#         sys.exit(app.exec_())


























# from PyQt5.QtWidgets import QApplication , QLineEdit , QWidget , QFormLayout
# from PyQt5.QtGui import QIntValidator , QDoubleValidator , QFont 
# from PyQt5.QtCore import Qt 
# import sys 


# class line_edit(QWidget):
#     def __init__(self, parent =None  ):
#         super().__init__(parent)
#         e1 = QLineEdit() 
#         e1.setValidator(QIntValidator())
#         e1.setMaxLength(9)
#         e1.setAlignment(Qt.AlignRight) 
#         e1.setFont(QFont("Arial" , 30)) 

#         e2 = QLineEdit() 
#         e2.setValidator(QDoubleValidator(0.99 , 99.99 , 2)) 
#         e3 = QLineEdit() 
#         e3.setInputMask("+99_9999_834")

#         e4 = QLineEdit() 
#         e4.textChanged.connect(self.textchanged) 
        
#         e5 = QLineEdit() 
#         e5.setEchoMode(QLineEdit.Password) 
        
#         flo = QFormLayout() 
#         flo.addRow("integer vali " , e1) 
#         flo.addRow('double vali' , e2) 
#         flo.addRow('input mask ',e3) 
#         flo.addRow('password' , e5) 
#         flo.addRow('text changed' , e4) 

#         self.setLayout(flo)
#         self.setWindowTitle('good mixture')
#     def textchanged(self, text): 
#         print('changed \n , ',text) 
#     def enterPress(self): 
#         print("enter pressed" ) 

# if __name__ == "__main__" : 
#     app = QApplication(sys.argv) 
#     win = line_edit() 
#     win.resize(500 , 500)
#     win.show() 
#     sys.exit(app.exec_())





# from PyQt5 import QtWidgets as qq 
# from PyQt5 import QtGui 
# import sys

# app = qq.QApplication(sys.argv)   #initiallizes new app . 
# win = qq.QWidget()     # qwidget as main window container. 

# win.resize(400 , 400 )  # window to width and height 
# win.move(300 , 300)     #position on screen. 

# win.setWindowTitle("braille")
# win.setWindowIcon(QtGui.QIcon('icon.png')  )   #icon 

# win.show() 
# sys.exit(app.exec_())


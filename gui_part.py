














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


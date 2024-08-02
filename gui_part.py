




print('\u280E')


h = open('test.txt' , 'w') 
h.write(chr(0x280F))
h.close()







# from PyQt5.Qt import *

# import sys

# app = QApplication(sys.argv)

# w = QWidget()
# w.setWindowTitle("QButtonGrounp")
# w.resize (300, 150)

# # Create 4 QRadioButton buttons
# cs1 = QRadioButton ("Super Cup", w)
# cs1.move(80, 20)

# cs2 = QRadioButton ("Big Cup", w)
# cs2.move(80, 40)

# cs3 = QRadioButton ("Medium Cup", w)
# cs3.move(80, 60)

# cs4 = QRadioButton ("small cup", w)
# cs4.move(80, 80)

# # Create a key group and add keys
# cs_group = QButtonGroup(w)
# cs_group.addButton(cs1,1)
# cs_group.addButton(cs2,2)
# cs_group.addButton(cs3,3)
# cs_group.addButton(cs4,4)

# # Define the slot function and print the received parameters
# def slot(object):
#     print("Key was pressed, id is:", cs_group.id(object))

# # connects the slot function and makes the argument of the band int type
# cs_group.buttonClicked.connect(slot)
# w.show()

# if __name__ == '__main__':
#     sys.exit(app.exec_())




# from PyQt5.Qt import *
# import sys

# app = QApplication(sys.argv)

# w = QWidget()
# w.setWindowTitle("QButtonGroup")
# w.resize (300, 150)

# #Create group 1 QRadioButton button
# cs1 = QRadioButton("1st",w)
# cs1.move(20, 20)

# #Setting the first radio box to be checked
# cs1.setChecked(True)
# cs2 = QRadioButton("2nd",w)
# cs2.move(20, 40)

# #Create a key group and add keys
# cs_group = QButtonGroup(w)
# cs_group.addButton(cs1, 1)
# cs_group.addButton(cs2, 2)

# #move cs2 key out of sc_group
# cs_group.removeButton(cs2)

# w.show()

# if __name__ == '__main__':
#     sys.exit(app.exec_())




# from PyQt5.Qt import *
# import sys

# app = QApplication(sys.argv)

# w = QWidget()
# w.setWindowTitle("QButtonGroup")
# w.resize (300, 150)

# #Create group 1 QRadioButton button
# cs1 = QRadioButton ("Super Cup", w)
# cs1.move(80, 20)

# cs2 = QRadioButton ("Big Cup", w)
# cs2.move(80, 40)

# cs3 = QRadioButton ("Medium Cup", w)
# cs3.move(80, 60)

# cs4 = QRadioButton ("small cup", w)
# cs4.move(80, 80)

# #Create a key group and add keys
# cs_group = QButtonGroup(w)
# cs_group.addButton(cs1)
# cs_group.addButton(cs2)
# cs_group.addButton(cs3)
# cs_group.addButton(cs4)

# # Set cs_group to not be mutually exclusive
# cs_group.setExclusive(False)

# w.show()

# if __name__ == '__main__':
#     sys.exit(app.exec_())








# from PyQt5.Qt import *
# import sys

# app = QApplication(sys.argv)

# w = QWidget()
# w.setWindowTitle("QButtonGrounp")
# w.resize(300, 150)

# cs1 = QRadioButton("Answer A",w)
# cs1.move(20, 20)
# cs1.setChecked(True)

# cs2 = QRadioButton("Answer B",w)
# cs2.move(20, 40)

# cs_group = QButtonGroup(w)
# cs_group.addButton(cs1, 1)      # ID 1
# cs_group.addButton(cs2, 2)      # ID 2

# print(cs_group.buttons())
# print(cs_group.button(2))       # ID=2
# print(cs_group.checkedButton())

# w.show()

# if __name__ == '__main__':
#     sys.exit(app.exec_())


# # *************** important radio buttons
# from PyQt5.Qt import *
# import sys    

# app = QApplication(sys.argv)

# w = QWidget()
# w.setWindowTitle("QButtonGrounp")
# w.resize(300, 150)

# cs1 = QRadioButton("Beginner",w)
# cs1.move(130, 20)

# cs2 = QRadioButton("Senior",w)
# cs2.move(130, 40)

# cs3 = QRadioButton("Expert",w)
# cs3.move(130, 60)

# cs4 = QRadioButton("Best",w)
# cs4.move(130, 80)

# cs_group = QButtonGroup(w)
# cs_group.addButton(cs1)
# cs_group.addButton(cs2)
# cs_group.addButton(cs3)
# cs_group.addButton(cs4)

# drs1 = QRadioButton("Python",w)
# drs1.move(20, 20)

# drs2 = QRadioButton("Golang",w)
# drs2.move(20, 40)

# drs3 = QRadioButton("Java",w)
# drs3.move(20, 60)

# drs_group = QButtonGroup(w)
# drs_group.addButton(drs1)
# drs_group.addButton(drs2)
# drs_group.addButton(drs3)

# w.show()

# if __name__ == '__main__':
#     sys.exit(app.exec_())










# import sys
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
# from PyQt5.QtCore import QTimer,QDateTime

# class WinForm(QWidget):
#     def __init__(self,parent=None):
#         super(WinForm, self).__init__(parent)
#         self.setWindowTitle('QTimer demonstration')

#         self.listFile=QListWidget()
#         self.label=QLabel('Label')
#         self.startBtn=QPushButton('Start')
#         self.endBtn=QPushButton('Stop')

#         layout=QGridLayout()

#         self.timer=QTimer()
#         self.timer.timeout.connect(self.showTime)

#         layout.addWidget(self.label,0,0,1,2)
#         layout.addWidget(self.startBtn,1,0)
#         layout.addWidget(self.endBtn,1,1)

#         self.startBtn.clicked.connect(self.startTimer)
#         self.endBtn.clicked.connect(self.endTimer)

#         self.setLayout(layout)

#     def showTime(self):
#         current_time=QDateTime.currentDateTime()
#         formatted_time=current_time.toString('yyyy-MM-dd hh:mm:ss dddd')
#         self.label.setText(formatted_time)

#     def startTimer(self):
#         self.timer.start(1000)
#         self.startBtn.setEnabled(False)
#         self.endBtn.setEnabled(True)

#     def endTimer(self):
#         self.timer.stop()
#         self.startBtn.setEnabled(True)
#         self.endBtn.setEnabled(False)

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     form=WinForm()
#     form.show()
#     sys.exit(app.exec_())






#***************  important   drag and drop
#*************** 2 main part is important.
# import sys
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *

# class CustomDropList(QListWidget):
#     def __init__(self):
#         super(CustomDropList, self).__init__()
#         self.setAcceptDrops(True)

#     def handleDropEvent(self, dropEvent):
#         sourceList = dropEvent.source()
#         selectedItems = sourceList.selectedItems()
#         for item in selectedItems:
#             sourceList.takeItem(sourceList.indexFromItem(item).row())
#             self.addItem(item)
#         print('Completed Drop Operation')

# class DragDropDemo(QWidget):
#     def __init__(self):
#         super(DragDropDemo, self).__init__()
#         self.setWindowTitle('Drag and Drop QListWidget Demo')
#         layout = QHBoxLayout()
#         self.leftList = CustomDropList()
#         self.rightList = QListWidget()
#         initialItems = ['Item A', 'Item B', 'Item C']
#         self.rightList.addItems(initialItems)
#         self.rightList.setDragEnabled(True)
#         self.rightList.setDragDropOverwriteMode(False)
#         self.rightList.setSelectionMode(QAbstractItemView.ExtendedSelection)
#         self.rightList.setDefaultDropAction(Qt.MoveAction)
#         layout.addWidget(self.leftList)
#         layout.addWidget(self.rightList)
#         self.setLayout(layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demoWidget = DragDropDemo()
#     demoWidget.show()
#     sys.exit(app.exec_())






# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# class ListWidgetDemo(QListWidget):
#     def onItemClicked(self, item):
#         QMessageBox.information(self, "QListWidget Interaction", "You selected: " + item.text())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demoListWidget = ListWidgetDemo()

#     demoListWidget.resize(300, 120)
#     demoListWidget.addItem("Option 1")
#     demoListWidget.addItem("Option 2")
#     demoListWidget.addItem("Option 3")
#     demoListWidget.addItem("Option 4")
#     demoListWidget.setWindowTitle('QListWidget Demonstration')
#     demoListWidget.itemClicked.connect(demoListWidget.onItemClicked)

#     demoListWidget.show()
#     sys.exit(app.exec_())





#********* important 
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# class DockDemo(QMainWindow):
#     def __init__(self,parent=None):
#         super(DockDemo, self).__init__(parent)
#         layout=QHBoxLayout()
#         bar=self.menuBar()
#         file=bar.addMenu('File')
#         file.addAction('New')
#         file.addAction('Save')
#         file.addAction('quit')

#         self.items=QDockWidget('Dockable',self)

#         self.listWidget=QListWidget()
#         self.listWidget.addItem('Item1')
#         self.listWidget.addItem('Item2')
#         self.listWidget.addItem('Item3')
#         self.listWidget.addItem('Item4')

#         self.items.setWidget(self.listWidget)
#         self.items.setFloating(False)
#         self.setCentralWidget(QTextEdit())
#         self.addDockWidget(Qt.RightDockWidgetArea,self.items)

#         self.setLayout(layout)
#         self.setWindowTitle('Dock Demo with PyQt')

# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     demo=DockDemo()
#     demo.show()
#     sys.exit(app.exec_())


#     Finally, the QWidget is set up within the
#  window area, and list control is added through:
# self.items.setWidget(self.listWidget)

# #input dialog 
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.btn = QPushButton('Show Dialog', self)
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog)

#         self.le = QLineEdit(self)
#         self.le.move(130, 22)

#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Input Dialog')        
#         self.show()

#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, 'input dialog', 'Is this ok?')
#         if ok:
#             self.le.setText(str(text))

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())









# #progress bar 
# from random import randint
# import sys
# from PyQt5.QtCore import QTimer
# from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QProgressBar
 
# StyleSheet = '''
# #RedProgressBar {
#     text-align: center;
# }
# #RedProgressBar::chunk {
#     background-color: #F44336;
# }
# #GreenProgressBar {
#     min-height: 12px;
#     max-height: 12px;
#     border-radius: 6px;
# }
# #GreenProgressBar::chunk {
#     border-radius: 6px;
#     background-color: #009688;
# }
# #BlueProgressBar {
#     border: 2px solid #2196F3;
#     border-radius: 5px;
#     background-color: #E0E0E0;
# }
# #BlueProgressBar::chunk {
#     background-color: #2196F3;
#     width: 10px; 
#     margin: 0.5px;
# }
# '''
 
 
# class ProgressBar(QProgressBar):
 
#     def __init__(self, *args, **kwargs):
#         super(ProgressBar, self).__init__(*args, **kwargs)
#         self.setValue(0)
#         if self.minimum() != self.maximum():
#             self.timer = QTimer(self, timeout=self.onTimeout)
#             self.timer.start(randint(1, 3) * 1000)
 
#     def onTimeout(self):
#         if self.value() >= 100:
#             self.timer.stop()
#             self.timer.deleteLater()
#             del self.timer
#             return
#         self.setValue(self.value() + 1)
 
 
# class Window(QWidget):
 
#     def __init__(self, *args, **kwargs):
#         super(Window, self).__init__(*args, **kwargs)
#         self.resize(800, 600)
#         layout = QVBoxLayout(self)
#         layout.addWidget(  
#             ProgressBar(self, minimum=0, maximum=100, objectName="RedProgressBar"))
 
#         layout.addWidget(  
#             ProgressBar(self, minimum=0, maximum=0, objectName="RedProgressBar"))
 
#         layout.addWidget(  
#             ProgressBar(self, minimum=0, maximum=100, textVisible=False,
#                         objectName="GreenProgressBar"))
#         layout.addWidget(  
#             ProgressBar(self, minimum=0, maximum=0, textVisible=False,
#                         objectName="GreenProgressBar"))
 
#         layout.addWidget(  
#             ProgressBar(self, minimum=0, maximum=100, textVisible=False,
#                         objectName="BlueProgressBar"))
#         layout.addWidget(  
#             ProgressBar(self, minimum=0, maximum=0, textVisible=False,
#                         objectName="BlueProgressBar"))
 
 
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyleSheet(StyleSheet)
#     w = Window()
#     w.show()
#     sys.exit(app.exec_())
# import sys
# import time
# from PyQt5.QtCore import QThread, pyqtSignal
# from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar, QVBoxLayout, QApplication

# class Thread(QThread):
#     _signal = pyqtSignal(int)
#     def __init__(self):
#         super(Thread, self).__init__()

#     def __del__(self):
#         self.wait()

#     def run(self):
#         for i in range(100):
#             time.sleep(0.1)
#             self._signal.emit(i)
 
# class Example(QWidget):
#     def __init__(self):
#         super(Example, self).__init__()
#         self.setWindowTitle('QProgressBar')
#         self.btn = QPushButton('Click me')
#         self.btn.clicked.connect(self.btnFunc)
#         self.pbar = QProgressBar(self)
#         self.pbar.setValue(0)
#         self.resize(300, 100)
#         self.vbox = QVBoxLayout()
#         self.vbox.addWidget(self.pbar)
#         self.vbox.addWidget(self.btn)
#         self.setLayout(self.vbox)
#         self.show()
        
#     def btnFunc(self):
#         self.thread = Thread()
#         self.thread._signal.connect(self.signal_accept)
#         self.thread.start()
#         self.btn.setEnabled(False)

#     def signal_accept(self, msg):
#         self.pbar.setValue(int(msg))
#         if self.pbar.value() == 99:
#             self.pbar.setValue(0)
#             self.btn.setEnabled(True)
 
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec_())









#PyQt grid layout (QGridLayout example)
# The most frequently used layout class is grid layout, 
# this layout divides the space into rows and columns.

# It is an alternative to the box layout and default widget 
# positining.

# To create a grid layout, we use the class QGridLayout.
#  A grid layout is an evenly divided area to which you can
#  add widgets to each cell.

# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget,
# QPushButton, QGridLayout)
 
# class Example(QWidget):
 
#     def __init__(self):
#         super().__init__()
#         self.initUI()
     
#     def initUI(self):   
#         grid = QGridLayout()  
#         self.setLayout(grid)
      
#         names = ['Cls', 'Bck', '', 'Close', 
#         '7', '8', '9', '/',
#         '4', '5', '6', '*',
#         '1', '2', '3', '-',
#         '0', '.', '=', '+',]
      
#         positions = [(i, j) for i in range(5) for j in range(4)] # This is the button label to be used later.
      
#         for position, name in zip(positions, names):
#          if name == '':
#           continue
#          button = QPushButton(name)
#          grid.addWidget(button, *position)
      
#         self.move(300, 150)
#         self.setWindowTitle('PyQt window')  
#         self.show()
    
# if __name__ == '__main__':
#      app = QApplication(sys.argv)
#      ex = Example()
#      sys.exit(app.exec_()) 










#**************************  very important to spaceing 

# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout)

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         okButton = QPushButton('OK')
#         cancelButton = QPushButton('Cancel')
#         #  QHBoxLayout and QVBoxLayout . for vertical and horizental box layout
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)    # get flexible space to elements. 
#         #widget in layouts . 
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#         vbox = QVBoxLayout()   # This line creates an instance of QVBoxLayout, a layout manager that arranges widgets vertically in a single column.
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#         self.setLayout(vbox)
#         self.setGeometry(300, 300, 350, 150)
#         self.setWindowTitle('Utilizing PyQt Box Layouts: QHBoxLayout and QVBoxLayout')  
#         self.show()

# if __name__ == '__main__':
#  app = QApplication(sys.argv)
#  ex = Example()
#  sys.exit(app.exec_())
######################### description of code by gpt 
# Certainly! Let's break down the code snippet line by line to understand its functionality in PyQt5:

# python
# Copy code
# hbox = QHBoxLayout()
# This line creates an instance of QHBoxLayout, which is a layout manager that arranges widgets horizontally in a single row.
# python
# Copy code
# hbox.addStretch(1)
# This line adds a stretchable space to the hbox layout. The parameter 1 indicates the stretch factor, which determines how much space this stretchable element will take relative to other stretchable elements. In this case, it allows for flexible space to be distributed.
# python
# Copy code
# hbox.addWidget(okButton)
# This line adds the okButton widget to the hbox layout. This widget will be placed next to the stretchable space created earlier.
# python
# Copy code
# hbox.addWidget(cancelButton)
# This line adds the cancelButton widget to the hbox layout, positioned next to the okButton.
# python
# Copy code
# vbox = QVBoxLayout()
# This line creates an instance of QVBoxLayout, a layout manager that arranges widgets vertically in a single column.
# python
# Copy code
# vbox.addStretch(1)
# This line adds a stretchable space to the vbox layout, allowing for flexible vertical space distribution, similar to the horizontal stretchable space in hbox.
# python
# Copy code
# vbox.addLayout(hbox)
# This line adds the hbox layout to the vbox layout. This effectively nests the horizontal layout within the vertical layout, arranging the okButton and cancelButton widgets horizontally within the vertical layout.
# In summary, this code sets up a layout with a vertical box layout (vbox) that contains a horizontal box layout (hbox). The hbox layout includes two buttons (okButton and cancelButton) and some stretchable space to control the spacing between the buttons. The vbox layout includes the hbox, along with a stretchable space at the top. This configuration is useful for creating a layout with buttons at the bottom of a window or dialog.







# https://pythonpyqt.com/pyqt-box-layout/








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


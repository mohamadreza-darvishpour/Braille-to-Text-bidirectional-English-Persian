





import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Window 1"))
        self.setLayout(layout)

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Window 2"))
        self.setLayout(layout)

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Window 3"))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Multiple Windows Example")
        self.setGeometry(100, 100, 600, 400)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.window1 = Window1()
        self.window2 = Window2()
        self.window3 = Window3()

        self.stacked_widget.addWidget(self.window1)
        self.stacked_widget.addWidget(self.window2)
        self.stacked_widget.addWidget(self.window3)

        self.create_taskbar()

    def create_taskbar(self):
        self.taskbar = self.menuBar().addMenu("Windows")
        self.add_taskbar_action("Window 1", 0)
        self.add_taskbar_action("Window 2", 1)
        self.add_taskbar_action("Window 3", 2)

    def add_taskbar_action(self, name, index):
        action = self.taskbar.addAction(name)
        action.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(index))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())





















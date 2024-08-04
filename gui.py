import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QTextEdit, QPushButton, QLineEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('layer with grid test')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        grid_layout = QGridLayout()

        form_label = QLabel('form section')
        grid_layout.addWidget(form_label, 0, 0)

        #input text
        input_label = QLabel('input text test')
        grid_layout.addWidget(input_label, 0, 1)

        input_text = QLineEdit()
        grid_layout.addWidget(input_text, 1, 1)

        #show text
        show_label = QLabel('show text test')
        grid_layout.addWidget(show_label, 0, 2)

        show_text = QTextEdit()
        grid_layout.addWidget(show_text, 1, 2)        
        show_text2 = QTextEdit()
        grid_layout.addWidget(show_text2, 2, 1)

        #buttons
        buttons_label = QLabel('button section')
        grid_layout.addWidget(buttons_label, 0, 3)

        button_layout = QVBoxLayout()

        for i in range(1, 8):
            button = QPushButton(f'button {i}')
            button_layout.addWidget(button)

        grid_layout.addLayout(button_layout, 1, 3)

        layout.addLayout(grid_layout)

        self.setGeometry(100, 100, 800, 600) 
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

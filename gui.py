import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtWidgets import  QTextEdit , QGridLayout
class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
    
        main_layout = QVBoxLayout(central_widget)

        #screen text edit area
        self.screen = QTextEdit(self)
        self.screen.setReadOnly(False)
        main_layout.addWidget(self.screen)

        #keyboard(grid buttons)
        braille_keyboard = QWidget()
        keyboard_layout = QGridLayout()

        braille_buttons = [
            ('⠁', 0, 0), ('⠃', 0, 1), ('⠉', 0, 2),
            ('⠙', 1, 0), ('⠑', 1, 1), ('⠋', 1, 2),
            ('⠛', 2, 0), ('⠓', 2, 1), ('⠊', 2, 2),
            ('⠚', 3, 0), ('⠞', 3, 1), ('⠟', 3, 2),
            ('⠎', 4, 0), ('⠏', 4, 1), ('⠓', 4, 2)
        ]

        for text, row, col in braille_buttons:
            button = QPushButton(text, self)
            button.clicked.connect(self.type_in_screen)
            keyboard_layout.addWidget(button, row, col)

        braille_keyboard.setLayout(keyboard_layout)
        main_layout.addWidget(braille_keyboard)

        self.setWindowTitle('Braille Keyboard App')
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def type_in_screen(self):
        # button was clicked
        button = self.sender()
        if button:
            #button to text 
            self.screen.insertPlainText(button.text())

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('common language')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        label = QLabel('common lang label')
        layout.addWidget(label)

        button = QPushButton('Close Window 2')
        button.clicked.connect(self.close)
        layout.addWidget(button)

        self.setGeometry(500, 100, 400, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window1 = Window1()
    window2 = Window2()

    sys.exit(app.exec_())

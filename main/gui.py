import sys
from PyQt5.QtWidgets import *  # QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout
from PyQt5.QtCore import pyqtSignal
from translator import translator 

# Assume translate.braille_to_lang is your actual translation method
translate = translator()

def custom_translator(lang, braille_text):
    print('\n\n\n****', lang, '****')
    text = translate.braille_to_lang(lang, braille_text)
    return "Translated text for: " + text

braille_chars = [chr(code) for code in range(0x2800, 0x28FF + 1)]

class BrailleTranslator(QWidget):
    def __init__(self, input_area):
        super().__init__()
        self.input_area = input_area

        self.language_input = QLineEdit()
        self.language_input.setPlaceholderText("Enter language for translation")

        self.translated_text = QLineEdit()
        self.translated_text.setReadOnly(True)
        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.translate_text)

        layout = QVBoxLayout()
        layout.addWidget(self.language_input)
        layout.addWidget(self.translated_text)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.translate_button)
        self.setLayout(layout)

    def set_translated_text(self, text):
        self.translated_text.setText(text)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.translated_text.text())

    def translate_text(self):
        # Get the text from the input area
        braille_text = self.input_area.get_text()
        language = self.language_input.text()  # Get the language from the QLineEdit
        translated_text = custom_translator(language, braille_text)
        self.set_translated_text(translated_text)
        print(f"Translating Braille: {braille_text} to {language} -> {translated_text}")

class BrailleKeyboard(QWidget):
    def __init__(self, input_area):
        super().__init__()
        self.input_area = input_area

        layout = QGridLayout()
        positions = [(i, j) for i in range(10) for j in range(8)]

        for position, char in zip(positions, braille_chars):
            button = QPushButton(char)
            button.setFixedSize(30, 30)
            button.clicked.connect(lambda _, ch=char: self.insert_braille_char(ch))
            layout.addWidget(button, *position)

        self.setLayout(layout)

    def insert_braille_char(self, char):
        self.input_area.input_text.insertPlainText(char)
        self.input_area.textChanged.emit()  # Emit textChanged signal

class BrailleInputArea(QWidget):
    textChanged = pyqtSignal()  # Custom signal to handle text change

    def __init__(self):
        super().__init__()

        self.input_text = QTextEdit()
        self.input_text.setAcceptRichText(False)

        layout = QVBoxLayout()
        layout.addWidget(self.input_text)
        self.setLayout(layout)

    def get_text(self):
        return self.input_text.toPlainText()

    def set_text(self, text):
        self.input_text.setPlainText(text)

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Window 1"))
        self.setLayout(layout)

class Window2(QWidget):
    '''braille to lang'''
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_area = BrailleInputArea()
        self.translator = BrailleTranslator(self.input_area)  # Pass the input area to the translator
        self.keyboard = BrailleKeyboard(self.input_area)
        layout.addWidget(self.translator)
        layout.addWidget(QLabel("Braille Keyboard"))
        layout.addWidget(self.keyboard)
        layout.addWidget(QLabel("Braille Input Area"))
        layout.addWidget(self.input_area)

        self.setLayout(layout)

        # Connect textChanged signal to update translation
        self.input_area.textChanged.connect(self.translator.translate_text)

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

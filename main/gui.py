import sys
from PyQt5.QtWidgets import *  # QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout
from PyQt5.QtCore import pyqtSignal
from translator import translator 

translate = translator()
braille_chars = [chr(code) for code in range(0x2800, 0x28FF + 1)]

def custom_translator(lang, braille_text):
    text = translate.braille_to_lang(lang, braille_text)
    return "Translated text for: " + text


def to_braille_custom_translator(lang, braille_text):
    text = translate.lang_to_braille(lang, braille_text)
    return "Translated text for: " + text






class toBrailleTranslator(QWidget):
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
        translated_text = to_braille_custom_translator(language, braille_text)
        self.set_translated_text(translated_text)


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
    '''lang to braille'''
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.input_area = BrailleInputArea()
        self.translator = toBrailleTranslator(self.input_area)  # Pass the input area to the translator
        #self.keyboard = BrailleKeyboard(self.input_area)
        layout.addWidget(self.translator)
        # layout.addWidget(QLabel("Braille Keyboard"))
        # layout.addWidget(self.keyboard)
        layout.addWidget(QLabel("Braille Input Area"))
        layout.addWidget(self.input_area)

        self.setLayout(layout)

        # Connect textChanged signal to update translation
        self.input_area.textChanged.connect(self.translator.translate_text)




class Window4(QWidget):
    '''add new language in braille'''
    def __init__(self):
        super().__init__()

        self.default_text = translate.alphabet_string_exam
        

        layout = QVBoxLayout()

        # Label
        layout.addWidget(QLabel("This is Window 4"))

        # Input field for method name
        self.method_name_input = QLineEdit()
        self.method_name_input.setPlaceholderText("Enter name of new language or language to edit.")
        layout.addWidget(self.method_name_input)
        self.method_name_input.textChanged.connect(self.new_lang_name)

        # Input text field with default text
        self.text_input = QTextEdit(self.default_text)
        self.text_input.setFixedHeight(200)  # Set the preferred height to make it bigger
        layout.addWidget(self.text_input)

        # Button to reset text
        self.reset_button = QPushButton("Reset Text")
        self.reset_button.clicked.connect(self.reset_text)
        layout.addWidget(self.reset_button)

        # Button to send text to custom function
        self.send_button = QPushButton("Send Text")
        self.send_button.clicked.connect(self.send_text)
        layout.addWidget(self.send_button)

        # Options label and combo box
        options_layout = QVBoxLayout()
        options_label = QLabel("Options")
        options_layout.addWidget(options_label)
        self.option_combo = QComboBox()
        lang_list = list(translate.langs.keys())
        lang_list.insert(0 , 'languages')
        self.option_combo.addItems(lang_list)
        self.option_combo.currentIndexChanged.connect(self.option_changed)
        options_layout.addWidget(self.option_combo)
        layout.addLayout(options_layout)

        self.setLayout(layout)
    

    def new_lang_name(self  , text ):
        self.new_lang = text 
        

    def reset_text(self):
        self.text_input.setText(self.default_text)
        self.method_name_input.clear()
        self.option_combo.setCurrentIndex(0)

    def send_text(self):
        method_name = self.method_name_input.text()
        self.new_lang_name = method_name
        text = self.text_input.toPlainText()
        self.add_text(self.new_lang_name, text)
        self.update_options(method_name)
        self.reset_text()

    def add_text(self ,  method_name , text):
        # Custom function to handle the method name and text
        print(f'\n\n3223   methodname ={method_name} , text = {text} 3223\n\n')
        self.alarm = translate.add_lang(method_name , text)
        self.show_popup()

    def show_popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(self.alarm)
        msg.setWindowTitle("Information")
        msg.exec_()

    def option_changed(self, index):
        option_text = self.option_custom_func(self.option_combo.itemText(index))
        self.text_input.setText(option_text)

    def option_custom_func(self, option_index):
        # Custom function to return a text based on the option
        option_texts = {  'languages' : translate.alphabet_string_exam}
        for lang_key in translate.langs.keys() :
            string = ''
            for key,value in translate.langs[lang_key].items() :
                if key == '⠀': key = 'space'
                string +='  ' + key + '  =  {' + value +'},\n'
            option_texts[lang_key] = string
        # option_texts[self.new_lang_name] = option

        return option_texts.get(option_index, self.default_text)

    def update_options(self, new_item):
        self.option_combo.addItem(new_item)



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
        self.window4 = Window4()

        self.stacked_widget.addWidget(self.window1)
        self.stacked_widget.addWidget(self.window2)
        self.stacked_widget.addWidget(self.window3)
        self.stacked_widget.addWidget(self.window4)

        self.create_taskbar()

    def create_taskbar(self):
        self.taskbar = self.menuBar().addMenu("Windows")
        self.add_taskbar_action("Window 1", 0)
        self.add_taskbar_action("Window 2", 1)
        self.add_taskbar_action("Window 3", 2)
        self.add_taskbar_action("Window 4", 3)

    def add_taskbar_action(self, name, index):
        action = self.taskbar.addAction(name)
        action.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(index))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())









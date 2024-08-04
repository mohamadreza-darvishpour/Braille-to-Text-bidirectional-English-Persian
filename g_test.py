










import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

class DragDropWidget(QFrame):
    def __init__(self, label_text):
        super().__init__()
        self.initUI(label_text)

    def initUI(self, label_text):
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self.setAcceptDrops(True)
        
        layout = QVBoxLayout()
        self.label = QLabel(label_text)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if file_path.endswith('.pdf'):
                    self.label.setText(f"File Dropped: {file_path}")
                else:
                    self.label.setText("Please drop a PDF file")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF Drag and Drop Interface')

        # Create a central widget and set the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a grid layout to divide into four parts
        grid_layout = QGridLayout()

        # Part 1: Drag PDF File Section
        drag_pdf_section = DragDropWidget('Drag PDF File Here')
        grid_layout.addWidget(drag_pdf_section, 0, 0)

        # Part 2: Drop PDF File Section
        drop_pdf_section = DragDropWidget('Drop PDF File Here')
        grid_layout.addWidget(drop_pdf_section, 0, 1)

        # Part 3: Buttons Section
        button_section = QWidget()
        button_layout = QVBoxLayout()

        # Adding 3 buttons
        for i in range(1, 4):
            button = QPushButton(f'Button {i}')
            button_layout.addWidget(button)
        
        button_section.setLayout(button_layout)
        grid_layout.addWidget(button_section, 1, 0)

        # Part 4: Exit and Start Section
        exit_start_section = QWidget()
        exit_start_layout = QVBoxLayout()

        start_button = QPushButton('Start')
        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)

        exit_start_layout.addWidget(start_button)
        exit_start_layout.addWidget(exit_button)
        exit_start_section.setLayout(exit_start_layout)
        grid_layout.addWidget(exit_start_section, 1, 1)

        # Add the grid layout to the main layout
        layout.addLayout(grid_layout)

        self.setGeometry(100, 100, 800, 600)  # Set window size
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())












# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QTextEdit, QPushButton, QLineEdit, QLabel

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('layer with grid test')

#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         layout = QVBoxLayout()
#         central_widget.setLayout(layout)

#         grid_layout = QGridLayout()

#         form_label = QLabel('form section')
#         grid_layout.addWidget(form_label, 0, 0)

#         #input text
#         input_label = QLabel('input text test')
#         grid_layout.addWidget(input_label, 0, 1)

#         input_text = QLineEdit()
#         grid_layout.addWidget(input_text, 1, 1)

#         #show text
#         show_label = QLabel('show text test')
#         grid_layout.addWidget(show_label, 0, 2)

#         show_text = QTextEdit()
#         grid_layout.addWidget(show_text, 1, 2)        
#         show_text2 = QTextEdit()
#         grid_layout.addWidget(show_text2, 2, 1)

#         #buttons
#         buttons_label = QLabel('button section')
#         grid_layout.addWidget(buttons_label, 0, 3)

#         button_layout = QVBoxLayout()

#         for i in range(1, 8):
#             button = QPushButton(f'button {i}')
#             button_layout.addWidget(button)

#         grid_layout.addLayout(button_layout, 1, 3)

#         layout.addLayout(grid_layout)

#         self.setGeometry(100, 100, 800, 600) 
#         self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     sys.exit(app.exec_())

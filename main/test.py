from translator import translator


import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt, QMimeData, QUrl
from PyPDF2 import PdfReader, PdfWriter
from PyQt5.QtGui import QDrag

# Translator instance
translate = translator()
braille_chars = [chr(code) for code in range(0x2800, 0x28FF + 1)]




class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Drag and Drop")

        # Main layout
        layout = QVBoxLayout()

        # Dragging part label
        self.drag_label = QLabel("Drag a PDF file here")
        self.drag_label.setStyleSheet(self.default_style())
        self.drag_label.setFixedHeight(100)
        self.drag_label.setAlignment(Qt.AlignCenter)
        self.drag_label.setAcceptDrops(True)
        self.drag_label.dragEnterEvent = self.dragEnterEvent
        self.drag_label.dropEvent = self.dropEvent

        layout.addWidget(self.drag_label)

        # Language selection options
        self.language_combo = QComboBox()
        self.language_combo.addItems(["English", "French", "Spanish", "German"])
        layout.addWidget(self.language_combo)

        # Dropping part label
        self.drop_label = QLabel("PDF File ready for drag and drop")
        self.drop_label.setStyleSheet(self.default_style())
        self.drop_label.setFixedHeight(50)
        self.drop_label.setAlignment(Qt.AlignCenter)
        self.drop_label.setAcceptDrops(False)

        layout.addWidget(self.drop_label)

        # Reset and Capitalize buttons
        button_layout = QVBoxLayout()

        self.reset_button = QPushButton("Reset")
        button_layout.addWidget(self.reset_button)
        self.reset_button.clicked.connect(self.resetFields)

        self.capitalize_button = QPushButton("Capitalize")
        button_layout.addWidget(self.capitalize_button)
        self.capitalize_button.clicked.connect(self.capitalizePDF)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Internal variables
        self.pdf_file_path = None
        self.output_pdf_path = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            self.pdf_file_path = url.toLocalFile()
            if self.pdf_file_path.lower().endswith(".pdf"):
                self.drag_label.setText(f"Loaded PDF: {os.path.basename(self.pdf_file_path)}")
                self.drag_label.setStyleSheet(self.aqua_style())
            else:
                QMessageBox.warning(self, "Invalid File", "Please drop a valid PDF file.")
                self.pdf_file_path = None
                self.drag_label.setText("Drag a PDF file here")
                self.drag_label.setStyleSheet(self.default_style())

    def resetFields(self):
        self.pdf_file_path = None
        self.output_pdf_path = None
        self.drag_label.setText("Drag a PDF file here")
        self.drag_label.setStyleSheet(self.default_style())
        self.drop_label.setText("PDF File ready for drag and drop")
        self.drop_label.setStyleSheet(self.default_style())
        self.language_combo.setCurrentIndex(0)

    def capitalizePDF(self):
        if not self.pdf_file_path:
            QMessageBox.warning(self, "Missing Information", "Please ensure a PDF file is dragged.")
            return

        # Create a default save path in the current directory
        default_save_dir = os.path.join(os.getcwd(), "output_pdfs")
        os.makedirs(default_save_dir, exist_ok=True)
        self.output_pdf_path = os.path.join(default_save_dir, f"CAPITALIZED_{os.path.basename(self.pdf_file_path)}")

        # Read PDF and capitalize text
        with open(self.pdf_file_path, "rb") as file:
            reader = PdfReader(file)
            writer = PdfWriter()

            for i in range(len(reader.pages)):
                page = reader.pages[i]
                page_text = page.extract_text().upper()
                writer.add_page(page)

                with open(self.output_pdf_path, "wb") as output_file:
                    writer.write(output_file)

        self.enable_drag_and_drop()

    def enable_drag_and_drop(self):
        # Set up the drop label to allow drag-and-drop of the generated PDF
        def drag_start(event):
            mime_data = QMimeData()
            mime_data.setUrls([QUrl.fromLocalFile(self.output_pdf_path)])
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            drag.exec_(Qt.CopyAction | Qt.MoveAction)

        self.drop_label.setText(f"PDF ready: {os.path.basename(self.output_pdf_path)}")
        self.drop_label.setStyleSheet(self.aqua_style())
        self.drop_label.mouseMoveEvent = drag_start

    def default_style(self):
        return """
            QLabel {
                border: 2px dashed #aaa;
                background-color: #f9f9f9;
                color: #333;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
        """

    def aqua_style(self):
        return """
            QLabel {
                border: 2px dashed aqua;
                background-color: #e0ffff;
                color: #007777;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
        """




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Multiple Windows Example")
        self.setGeometry(100, 100, 600, 400)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.window1 = Window1()

        self.stacked_widget.addWidget(self.window1)

        self.create_taskbar()

    def create_taskbar(self):
        self.taskbar = self.menuBar().addMenu("Windows")
        self.add_taskbar_action("Window 1", 0)

    def add_taskbar_action(self, name, index):
        action = self.taskbar.addAction(name)
        action.triggered.connect(lambda: self.stacked_widget.setCurrentIndex(index))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())





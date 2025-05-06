import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QInputDialog,
    QGridLayout
)
from PyQt5.QtCore import Qt

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog Demo - F1D021099")

        # Tombol-tombol
        self.btn_list = QPushButton("Choose from list")
        self.btn_text = QPushButton("get name")
        self.btn_int = QPushButton("Enter an integer")

        # Input field
        self.input_list = QLineEdit()
        self.input_text = QLineEdit()
        self.input_int = QLineEdit()

        # Atur layout grid supaya tombol di kiri dan input di kanan
        layout = QGridLayout()
        layout.addWidget(self.btn_list, 0, 0)
        layout.addWidget(self.input_list, 0, 1)

        layout.addWidget(self.btn_text, 1, 0)
        layout.addWidget(self.input_text, 1, 1)

        layout.addWidget(self.btn_int, 2, 0)
        layout.addWidget(self.input_int, 2, 1)

        # Hubungkan tombol ke fungsi masing-masing
        self.btn_list.clicked.connect(self.get_item)
        self.btn_text.clicked.connect(self.get_text)
        self.btn_int.clicked.connect(self.get_int)

        self.setLayout(layout)

    def get_item(self):
        items = ["C", "C++", "Java", "Python", "Ruby"]
        item, ok = QInputDialog.getItem(self, "select input dialog", "list of languages", items, 0, False)
        if ok and item:
            self.input_list.setText(item)

    def get_text(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.input_text.setText(text)

    def get_int(self):
        number, ok = QInputDialog.getInt(self, "integer input dualog", "enter a number")
        if ok:
            self.input_int.setText(str(number))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InputDialogDemo()
    window.resize(400, 120)
    window.show()
    sys.exit(app.exec_())

import sys
import ctypes
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *
from qt_material import QtStyleTools

class Widget(QWidget, QtStyleTools):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.setWindowIcon(QIcon('icon.png'))

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        self.text_widget = QLineEdit()
        self.text_widget.returnPressed.connect(self.searchEvent)
        button = QPushButton("検索")
        button.clicked.connect(self.searchEvent)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.text_widget)
        search_layout.addWidget(button)
        search_widget = QWidget()
        search_widget.setLayout(search_layout)

        content_layout = QVBoxLayout()
        content_layout.addWidget(search_widget)
        content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)

        self.apply_stylesheet(self, 'dark_teal.xml')
    
    def searchEvent(self):
        value = self.text_widget.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + value, QMessageBox.Ok, QMessageBox.Ok)

if __name__ == "__main__":

    #Explicitly tell Windows the correct AppUserModelID for this process by using a Windows call.
    #This causes the window icon to appear on the taskbar.
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app = QApplication()

    w = Widget()
    w.show()

    sys.exit(app.exec())
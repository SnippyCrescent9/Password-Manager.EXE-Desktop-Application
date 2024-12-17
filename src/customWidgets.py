from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMainWindow, QWidget, QStackedLayout)

class Searched_password_obj(QWidget):
    def __init__(self, website, username, password, hyperlink):
        super().__init__()

        #data information stored inside of Password Object
        self.website = website
        self.username = username
        self.password = password
        self.hyperlink = hyperlink

        self.label1= QLabel(self.website)
        self.label2 = QLabel(self.username)

        self.search_password = QVBoxLayout
        self.search_password.addWidget(self.label1)
        self.search_password.addWidget(self.label2)

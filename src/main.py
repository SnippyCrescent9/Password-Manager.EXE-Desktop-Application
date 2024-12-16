from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMainWindow, QWidget)

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        #Username Field
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")

        #Password Field (masked input)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter Password")

        #Login Button
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.check_login)

        #Error Message Label
        self.message_label = QLabel("", self)

        #Layout
        layout = QVBoxLayout()
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.message_label)
        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        #Validates the credentials
        if username == "admin" and password == "password":
            self.message_label.setText("Login successful!")
            self.accept() #Closes dialogue with an accepted state
        else:
            self.message_label.setText("Invalid username or password")
        

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")

        #Placeholder task request for password manager
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("What would you like to do today?")
        
        layout = QVBoxLayout()
        layout.addWidget(self.task_input)
        self.setLayout(layout)

        self.setGeometry(100,100,600,400)

app = QApplication([])

#Show the login dialog
login_dialog = LoginDialog()
if login_dialog.exec() == QDialog.Accepted:
    main_window = MainAppWindow()
    main_window.show()

app.exec()


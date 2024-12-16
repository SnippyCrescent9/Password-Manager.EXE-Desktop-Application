from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton, QLabel, QVBoxLayout, QMainWindow, QWidget)

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        # self.master_username = ""
        # self.master_password = ""

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
        
# class CreateMasterUser(QDialog):



class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Turtle Key Password Manager")

        #Buttoms for task requests for password manager
        all_button = QPushButton("All Passwords", self)
        all_button.clicked.connect(self.show_all_passwords)
        
        wifi_button = QPushButton("Wifi Passwords", self)
        wifi_button.clicked.connect(self.show_wifi_passwords)
        
        deleted_button = QPushButton("Deleted Passwords", self)
        deleted_button.clicked.connect(self.show_deleted_passwords)

        new_entry = QPushButton("New Password Entry", self)
        new_entry.clicked.connect(self.password_creator)

        #layout for main window when opened
        layout = QVBoxLayout()
        layout.addWidget(all_button)
        layout.addWidget(wifi_button)
        layout.addWidget(deleted_button)
        layout.addWidget(new_entry)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
        self.setGeometry(100,100,600,400)

    #changes layout to allow you to view all passwords in alpha order
    def show_all_passwords(self):
        self.clear_layout(self.layout)
        label = QLabel("Your passwords will be shown here!")
        self.layout.addWidget(label)

    def show_wifi_passwords(self):
        self.clear_layout(self.layout)
        label = QLabel("Your passwords will be shown here!")
        self.layout.addWidget(label)

    def show_deleted_passwords(self):
        self.clear_layout(self.layout)
        label = QLabel("Your passwords will be shown here!")
        self.layout.addWidget(label)
    
    def password_creator(self):
        self.clear_layout(self.layout)
        label = QLabel("Your passwords will be shown here!")
        self.layout.addWidget(label)
    

app = QApplication([])

#Show the login dialog
login_dialog = LoginDialog()
if login_dialog.exec() == QDialog.Accepted:
    main_window = MainAppWindow()
    main_window.show()

app.exec()


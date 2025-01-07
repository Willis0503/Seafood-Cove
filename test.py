from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import sys

def on_login():
    print("Login button clicked!")

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My PyQt GUI")

layout = QVBoxLayout()

label = QLabel("Login")
username = QLineEdit()
username.setPlaceholderText("Username")
password = QLineEdit()
password.setPlaceholderText("Password")
password.setEchoMode(QLineEdit.Password)
login_button = QPushButton("Login")
login_button.clicked.connect(on_login)

layout.addWidget(label)
layout.addWidget(username)
layout.addWidget(password)
layout.addWidget(login_button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())

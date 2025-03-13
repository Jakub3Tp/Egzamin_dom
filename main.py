import sys
from random import randint

from PyQt6.QtSql import password
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.generate.clicked.connect(self.generate_password)
        self.ui.save.clicked.connect(self.message)
        self.show()

    def generate_password(self):
        password = int(self.ui.numberOf.text())
        pass_word = ''

        set_of_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        set_of_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','G','R','S','T','U','V','W','X','Y','Z']
        set_of_digits = ['0','1','2','3','4','5','6','7','8','9']
        set_of_special = ['!','@','#','$','%','^','&','*','()','_','+','-','=']

        for i in range(password):
            randomLower = randint(0, len(set_of_lowercase)-1)
            pass_word += set_of_lowercase[randomLower]

        if self.ui.bigSmall.isChecked():
            randomUpper = randint(0, len(set_of_uppercase) - 1)
            pass_word = set_of_uppercase[randomUpper] + pass_word

        if self.ui.numbers.isChecked():
            randomNumber = randint(0, len(set_of_digits) - 1)
            pass_word = set_of_digits[randomNumber] + pass_word

        if self.ui.special.isChecked():
            randomSpecial = randint(0, len(set_of_special) - 1)
            pass_word = set_of_special[randomSpecial] + pass_word

        print(pass_word)

    def message(self):
        name = self.ui.name.text()
        surname = self.ui.surname.text()
        status = str(self.ui.status.currentText())
        password = password()

        message = QMessageBox()
        message.setText(f'{name}, {surname}, {status}, {pas}')
        message.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
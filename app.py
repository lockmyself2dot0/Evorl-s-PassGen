from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from ui.ui_main import Ui_MainWindow

import sys

import ui.rsc
import buttons
import password


class PassGen(QMainWindow):
    """Объект главного рбочего окна
    """
    def __init__(self) -> None:
        super(PassGen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.slider_spinbox_set_pass()
        self.set_pass()

        for btn in buttons.GENERATE_PASSWORD:
            getattr(self.ui, btn).clicked.connect(self.set_pass)
        
        self.ui.btn_visi.clicked.connect(self.change_pass_visi)
        self.ui.line_pass.textChanged.connect(self.set_entro)
        self.ui.line_pass.textChanged.connect(self.set_strenght)
        self.ui.btn_copy.clicked.connect(self.copy)



    def slider_spinbox_set_pass(self) -> None:
        """Связывает значения между слайдером, спибоксом паролем
        """
        self.ui.slider_lenght.valueChanged.connect(self.ui.spinbox_lenght.setValue)
        self.ui.spinbox_lenght.valueChanged.connect(self.ui.slider_lenght.setValue)
        self.ui.spinbox_lenght.valueChanged.connect(self.set_pass)

    def get_list_chars(self) -> list: 
        """Создает список, состоящий из словарей, которые должны использоваться при генерации пароля

        Returns:
            list: список словарей
        """
        chars = []
        for btn in buttons.Chars:
            if getattr(self.ui, btn.name).isChecked():
                chars.append(btn.value)

        return chars
    
    def set_pass(self) -> None:
        """Вызывает функцию создания пароля и вписывает получившееся значение в строку ввода 
        """
        try:
            self.ui.line_pass.setText(password.create(length=self.ui.slider_lenght.value(), char_list=self.get_list_chars()))
        except IndexError:
            self.ui.line_pass.clear()

        self.set_entro()
        self.set_strenght()

    def get_count_chars(self) -> int:
        """Высчитывает сумарное количество символов в использованных словарях 

        Returns:
            int: количество букв
        """
        num = 0

        for btn in buttons.CHARACTER_NUMBER.items():
            if getattr(self.ui, btn[0]).isChecked():
                num += btn[1]

        return num

    def set_entro(self) -> None:
        """Высчитывает энтропию, 
        """
        pword = len(self.ui.line_pass.text())
        chars_num = self.get_count_chars()

        self.ui.text_entropy.setText(f'Entropy: {password.get_entro(pword, chars_num)} bit')

    def set_strenght(self) -> None:
        """Дает оценку сложности пароля
        """
        lenght =len(self.ui.line_pass.text())
        chars_num = self.get_count_chars()

        for strenght in password.StrengthToEntropy:
            if password.get_entro(lenght, chars_num) >= strenght.value:
                self.ui.text_strengt.setText(f'Strenght: {strenght.name}')

    def change_pass_visi(self) -> None:
        """Изменяет видимость пароля
        """
        if self.ui.btn_visi.isChecked():
            self.ui.line_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.line_pass.setEchoMode(QLineEdit.Password)

    def copy(self) -> None:
        """Копирует пароль в буфер обмена
        """
        QApplication.clipboard().setText(self.ui.line_pass.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PassGen()
    window.show()

    sys.exit(app.exec())
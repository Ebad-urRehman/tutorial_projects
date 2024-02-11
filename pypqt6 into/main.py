from PyQt6.QtWidgets import QApplication,QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton
import sys
from datetime import datetime

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        # creating a grid layout
        grid = QGridLayout()

        name_label = QLabel("Name : ")
        self.input_name = QLineEdit()

        birth_label = QLabel("Enter Birth date : ")
        self.input_birth = QLineEdit()

        calc_button = QPushButton("Calculate Age")
        calc_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # adding above widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(birth_label, 1, 0)
        grid.addWidget(self.input_name, 0, 1)
        grid.addWidget(self.input_birth, 1, 1)
        grid.addWidget(calc_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        self.setLayout(grid)
    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.input_birth.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.input_name.text()} is {age} years old")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_calc = AgeCalculator()
    my_calc.show()
    sys.exit(app.exec())

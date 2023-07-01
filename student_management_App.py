

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit,QPushButton
import sys
from datetime import datetime
class agecalculator(QWidget):
    # inheriting qwidget class
    def __init__(self):
         # caliing init of parent/super class
           super().__init__()
           self.setWindowTitle("Age Calculator")
         # creating a grid
           grid=QGridLayout()
           name_label=QLabel("Name:")
           # for adding a new widget
           self.name_line_edit = QLineEdit()

           date_birth_label=QLabel("Date of Birth MM/DD/YY")
           self.date_birth_label_edit=QLineEdit()

           calculate_button=QPushButton("CalculateAge")
           calculate_button.clicked.connect(self.calculate_age)
           self.output_label=QLabel("")


           grid.addWidget(name_label, 0, 0)
           grid.addWidget(self.name_line_edit, 0, 1)
           grid.addWidget(date_birth_label, 1, 0)
           grid.addWidget(self.date_birth_label_edit, 1, 1)
           grid.addWidget(calculate_button, 2, 0, 1, 2)
           grid.addWidget(self.output_label, 3, 0, 1, 2)

    #        adding grid into widget class
           self.setLayout(grid)
    def calculate_age(self):
        current_year=datetime.now().year
        date_of_birth=self.date_birth_label_edit.text()
        year_of_birth=datetime.strptime(date_of_birth,"%m/%d/%Y").date().year
        age=current_year-year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old")
 # calling application first
app=QApplication(sys.argv)
age_calculator = agecalculator()
age_calculator.show()
sys.exit(app.exec())

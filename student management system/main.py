import sqlite3
from PyQt6.QtWidgets import QApplication, QTreeWidget, QLabel, QLayout,\
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem,\
    QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students Management System")
        self.setMinimumSize(400, 450)

        file_menu_bar = self.menuBar().addMenu("&File")
        edit_menu_bar = self.menuBar().addMenu("&Edit")
        help_menu_bar = self.menuBar().addMenu("&Help")

        add_student_action = QAction(QIcon("add.png"),"Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_bar.addAction(add_student_action)
        about_action = QAction("About", self)
        help_menu_bar.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        search_action = QAction(QIcon("search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_bar.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        self.load_data()

        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Status bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        # detect a cell click
        self.table.cellClicked.connect(self.cell_clicked)


    def cell_clicked(self):
        edit_button = QPushButton("Edit Selected")
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete)

        # finding button options created from previous cell clicked and delete them
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        # print(list(result))
        self.table.setRowCount(0)
        # outerloop is creating rows
        # innerloop is inserting items column wise in that row
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()
class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Student data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # adding student name widget to layout
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # adding combo box for sbujects
        self.course_select = QComboBox()
        courses = ["Data Structure", "Data Base", "Data Science", "AI", "ML"]
        self.course_select.addItems(courses)
        layout.addWidget(self.course_select)

        # adding Roll number widget to layout
        self.roll_no = QLineEdit()
        self.roll_no.setPlaceholderText("Roll no")
        layout.addWidget(self.roll_no)

        # add button
        button = QPushButton("Submit")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_select.itemText(self.course_select.currentIndex())
        r_no = self.roll_no.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, r_no))
        connection.commit()
        cursor.close()
        connection.close()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search")
        self.setFixedWidth(200)
        self.setFixedHeight(200)

        layout = QVBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Type anything")
        layout.addWidget(self.search_bar)

        button = QPushButton("Search")
        button.clicked.connect(self.search)
        layout.addWidget(button)

        self.setLayout(layout)

    def search(self):
        name = self.search_bar.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = connection.execute("SELECT * FROM students WHERE name = ?", (name,))
        print(cursor)
        print(list(cursor))
        print(result)
        print(list(result))
        items = main_win.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            # highlight selected items using row(item.row) and column 1(name column)
            main_win.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


class DeleteDialog():
    pass


class EditDialog():
    pass


if __name__ == '__main__':
    # creating an app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
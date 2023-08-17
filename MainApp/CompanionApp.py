import sys
from datetime import datetime, time
import pandas as pd
from PyQt5.QtGui import QFont# QIcon, QPixmap,
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

import Database_handlers
from Database_handlers.sql_handlers_companion import *


### Constants ###
date = datetime.now()
today = datetime.today().strftime("%d.%m.%Y")
day_of_week = datetime.today().isoweekday()
header_labels = ['Найменування', 'од. виміру', 'кількість']
kg = 'кг'
columns_for_rozclad = ('День тижня', 'Прийом їжі', 'Страва')
columns_bread = ['Дата', 'Витрачено \nборошна', 'Отримано \nхліба', 'Вихід \nплановий \n(%)', 'Вихід \nфактичний \n(%)', 'Олія\nза нормою\nв кг', 'Олія\nза нормою\nв %', 'Олія\nфактично\nв кг', 'Олія\nфактично\nв %', 'Сіль\nза нормою\nв кг', 'Сіль\nза нормою\nв %', 'Сіль\nфактично\nв кг', 'Сіль\nфактично\nв %', 'Дріжджі\nза нормою\nв кг', 'Дріжджі\nза нормою\nв %', 'Дріжджі\nфактично\nв кг', 'Дріжджі\nфактично\nв %']
columns_bread_act = ['Найменування \nматеріальних \nзасобів', 'Одиниця \nвиімру', 'Витрачено \nсировини', 'ціна \nза од.', 'Отримано \nпродукції', 'ціна \nза од.']
rows_bread_act = ['Борошно пшеничне \nІ гат', 'Дріжджі сухі', 'Олія', 'Сіль', 'Хліб пшеничний \nз борошна І гат.', 'ВСЬОГО:']
val_default = Database_handlers.sql_handlers.val_zag






class Storage(QWidget):
    def __init__(self, parent=None):
        super(Storage, self).__init__()
        self.parent = parent
        # parse database
        self.name_lables = parse_column_db()
        # create table widget
        self.detachment = detachment
        self.tableWidget = QTableWidget() # rows, columns
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        # create buttons
        self.form_table = QPushButton('   Сформувати таблицю')
        self.form_table.setIcon(QtGui.QIcon('icons/computer.png'))
        self.form_table.clicked.connect(self.show_table_func)
        self.form_excel = QPushButton('   Формувати у Excel')
        self.form_excel.setIcon(QtGui.QIcon('icons/excel.png'))
        self.form_excel.clicked.connect(self.export_to_excel)
        self.start_new_zvit = QPushButton('   Почати новий звіт')
        self.start_new_zvit.setIcon(QtGui.QIcon('icons/add_zvit.png'))
        self.start_new_zvit.clicked.connect(self.start_new_zv)
        # create dialog-window for save file
        self.dialog = QFileDialog(self)
        #self.question = QDialog(self)
        # layout box
        vBox = QVBoxLayout(self)

        vBox.addWidget(self.tableWidget)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_table)
        button_layout.addWidget(self.form_excel)
        vBox.addLayout(button_layout)
        vBox.addWidget(self.start_new_zvit)
        # add dialog-window for save file
        vBox.addWidget(self.dialog)
        #vBox.addWidget(self.question)


    def show_table_func(self):
        """
        function for create and show data from 'main_file' table
        """
        # table settings
        date = datetime.today().strftime("%d.%m.%Y")
        loss_header = 'Видаток'
        profit_header = 'Прибуток'
        self.names = self.name_lables[0]
        row_count = len(self.names) - 2
        dtch = (self.detachment[0],)
        self.detachment_start = parse_db_detach_start(dtch)
        date_start = (self.detachment_start[0][2],)
        data = dtch + date_start + (date,)
        self.detachment_loses = parse_db_detach_loss(data)
        self.detachment_profits = parse_db_detach_profit(data)
        self.detachment_actual = parse_db_detach_actual(dtch)

        leftovers_header = 'Залишок на ' + date
        header_labels = ['Найменування', 'од. виміру', 'Зал. на початок періоду']
        for i in range(len(self.detachment_loses)):
            header_labels.append(loss_header)
        for i in range(len(self.detachment_profits)):
            header_labels.append(profit_header)
        header_labels.append(leftovers_header)

        rows = []
        rows.append(self.detachment_start[0])
        for i in self.detachment_loses:
            rows.append(i)
        for i in self.detachment_profits:
            rows.append(i)
        rows.append(self.detachment_actual[0])

        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(len(header_labels))
        self.tableWidget.setHorizontalHeaderLabels(header_labels)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.setColumnWidth(0, 300)

        names_numb = 2
        for row in range(row_count): # for column 1
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.names[names_numb])))
            names_numb = names_numb+1
        for row in range(row_count): # for column 2
            self.tableWidget.setItem(row+1, 1, QTableWidgetItem(kg))

        column = 1
        for i in rows:
            temp = i[1:]
            column = column + 1
            row = -1
            for j in temp:
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(j)))
                row = row+1

    def export_to_excel(self):
        columnHeaders = []
        row_count = len(self.name_lables[0]) - 2
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
        for row in range(row_count):
            for col in range(self.tableWidget.columnCount()):
                try:
                    temp = self.tableWidget.item(row, col).text()
                except:
                    temp = 0
                df.at[row, columnHeaders[col]] = temp

        # activate dialog-window for save file
        result = self.dialog.getSaveFileName(self.tableWidget, 'Зберегти файл', 'C:/', 'Excel files (*.xlsx)')
        # try-except block for saving file
        try:
            df.to_excel(result[0])
        except:
            pass

    def start_new_zv(self):
        dtch = (self.detachment[0],)
        # dialog window !!!
        self.question = QMessageBox(self.tableWidget)
        self.question.setWindowTitle("Новий звіт")
        self.question.setInformativeText("Почати новий звіт?")
        self.question.addButton("Так", QMessageBox.AcceptRole)
        self.question.addButton("Ні", QMessageBox.AcceptRole)
        self.question.setIcon(QMessageBox.Information) # QtGui.QIcon('icons/question.png')
        self.question.show()
        bttn = self.question.exec()
        if self.question.clickedButton().text() == "Так":
            start_new_db(dtch)
        else:
            pass


class Two(QWidget):
    def __init__(self, parent=None):
        super(Two, self).__init__()
        self.parent = parent
        self.detachment = detachment






















class MainWindow(QMainWindow):
    """
    MAIN window Class
    """
    def __init__(self):
        super().__init__() # initialization widgets and properties Parent class "QDialog"
        # in here we set widgets and set properties
        self.setWindowTitle('eBookComp')
        self.setWindowIcon(QtGui.QIcon('icons/main.png'))
        #self.setWindowTitle("My App") # title of app
        self.resize(1150, 1000) # set size window
        font = QFont("Times New Roman", 14, 75, True) # set font window

        # add widgets
        self.main_widget = QTabWidget()
        self.detachment = QInputDialog.getText(self.main_widget, 'Введіть підрозділ', 'Введіть індекс підрозділу',
                                  text='test')
        global detachment
        detachment = self.detachment
        self.setCentralWidget(self.main_widget)


        self.main_widget.addTab(Storage(), "Залишки (Склад)")
        self.main_widget.addTab(Two(), "Two")




### Final App Block ###
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create app
    # app.setStyle('Oxygen') # 'Breeze'
    dlgMain = MainWindow() # build object of class "DlgMain" and set here in variable "dlgMain"

    dlgMain.show() # show function
    sys.exit(app.exec_())  # loop app in "sys.exit" func for check logs

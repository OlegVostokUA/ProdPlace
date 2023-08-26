import sys
from datetime import datetime, time
import pandas as pd
from PyQt5.QtGui import QFont# QIcon, QPixmap,
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui

import Database_handlers
from Database_handlers.sql_handlers_companion import *

# pip install pyinstaller
# pyinstaller -F -w -i "C:\Users\User\PycharmProjects\ProdPlace\MainApp\detach.ico" CompanionApp.py


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

    def show_table_func(self):
        """
        function for create and show data from 'main_file' table
        """
        # table settings
        date = datetime.today().strftime("%d.%m.%Y")
        loss_header = 'Видаток'
        profit_header = 'Прибуток'
        self.names = self.name_lables[0]
        row_count = len(self.names) - 3
        dtch = (self.detachment[0],)
        self.detachment_start = parse_db_detach_start(dtch)
        date_start = (self.detachment_start[0][3],)
        data = dtch + ('хліб',) + date_start + (date,)
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
        names_numb = 3
        for row in range(row_count): # for column 1
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.names[names_numb])))
            names_numb = names_numb+1
        for row in range(row_count): # for column 2
            self.tableWidget.setItem(row+1, 1, QTableWidgetItem(kg))
        column = 1
        for i in rows:
            temp = i[2:]
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


class Rozkladka(QWidget):
    def __init__(self, parent=None):
        super(Rozkladka, self).__init__()
        self.parent = parent

        self.lables_main = columns_for_rozclad
        self.name_lables_one = parse_column_db()
        self.name_lables = self.name_lables_one[0]
        self.name_lables = self.name_lables[4:]
        self.names_columns = self.lables_main + self.name_lables
        column_count = len(self.names_columns)
        self.tableWidget = QTableWidget(0, column_count)
        self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.setColumnWidth(2, 300)
        # create buttons
        self.form_table = QPushButton('   Сформувати таблицю')
        self.form_table.setIcon(QtGui.QIcon('icons/computer.png'))
        self.form_table.clicked.connect(self.show_table_func)

        main_v_box = QVBoxLayout(self)
        button_v_box = QHBoxLayout(self)
        button_v_box.addWidget(self.form_table)
        main_v_box.addWidget(self.tableWidget)
        main_v_box.addLayout(button_v_box)

    def show_table_func(self):
        self.rows = parse_db_rozklad()
        self.tableWidget.setRowCount(65)
        row = -1
        for i in self.rows:
            temp = i
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1


class Menu(QWidget):
    def __init__(self, parent=None):
        super(Menu, self).__init__()
        self.parent = parent
        # constants class
        zero_people = '0'
        self.detachment = detachment
        self.rows = parse_db_rozklad()
        self.lables_main = columns_for_rozclad
        self.name_lables_one = parse_column_db()
        self.name_lables = self.name_lables_one[0]
        self.name_lables = self.name_lables[4:]
        self.names_columns = self.lables_main + self.name_lables
        column_count = len(self.names_columns)
        # create input fields
        self.label_date = QLabel(self)
        self.label_date.setText('Введіть дату операції:')
        self.input_date = QDateEdit(self)
        self.input_date.setCalendarPopup(True)
        self.input_date.setDate(datetime.today())
        self.label_ppl = QLabel(self)
        self.label_ppl.setText('Введіть кількість людей:')
        self.input_ppl = QLineEdit(zero_people)
        self.label_ppl_d = QLabel(self)
        self.label_ppl_d.setText('Введіть кількість людей на обід:')
        self.input_ppl_d = QLineEdit(zero_people)
        self.label_day = QLabel(self)
        self.label_day.setText('Введіть день тижня:')
        self.input_day = QComboBox(self)
        self.input_day.addItems(['---', 'Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П’ятниця', 'Субота', 'Неділя'])
        self.input_day.currentTextChanged.connect(self.show_table_func)
        # create tables
        self.tableWidget = QTableWidget(0, column_count)
        self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget_2 = QTableWidget(0, column_count)
        self.tableWidget_2.setHorizontalHeaderLabels(self.names_columns)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.setColumnWidth(2, 300)
        self.calculate = QPushButton('   Розрахувати')
        self.calculate.setIcon(QtGui.QIcon('icons/calculate.png'))
        self.calculate.clicked.connect(self.calculate_result)
        self.save_to_db = QPushButton('   Зберегти у Базу Даних')
        self.save_to_db.setIcon(QtGui.QIcon('icons/database.png'))
        self.save_to_db.clicked.connect(self.push_to_database)
        self.to_excell = QPushButton('   Формувати у Excel')
        self.to_excell.setIcon(QtGui.QIcon('icons/excel.png'))
        self.to_excell.clicked.connect(self.export_to_excel)
        # create dialog-window for save file
        self.dialog = QFileDialog(self)

        main_v_box = QVBoxLayout(self)
        input_form_layout = QFormLayout(self)
        input_form_layout.addRow(self.label_date, self.input_date)
        input_form_layout.addRow(self.label_ppl, self.input_ppl)
        input_form_layout.addRow(self.label_ppl_d, self.input_ppl_d)
        input_form_layout.addRow(self.label_day, self.input_day)
        button_layout = QHBoxLayout(self)
        # button_layout.addWidget(self.form_table)
        button_layout.addWidget(self.calculate)
        button_layout.addWidget(self.save_to_db)
        button_layout.addWidget(self.to_excell)
        main_v_box.addLayout(input_form_layout)
        main_v_box.addWidget(self.tableWidget)
        main_v_box.addWidget(self.tableWidget_2)
        main_v_box.addLayout(button_layout)
        # add dialog-window for save file
        main_v_box.addWidget(self.dialog)

    def show_table_func(self, day):
        self.tableWidget.setRowCount(11)
        self.tableWidget_2.setRowCount(6)
        day = (day,)
        self.rows = parse_day_rozklad(day)
        self.rows_dinner = parse_day_dinner_rozklad(day)
        row = -1
        for i in self.rows:
            temp = i
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1
        row = -1
        for i in self.rows_dinner:
            temp = i
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget_2.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1

    def calculate_result(self):
        count_ppl = self.input_ppl.text()
        count_ppl = int(count_ppl)
        sum_colls = []
        total_colls = []
        for coll in range(3, self.tableWidget.columnCount()):
            data = []
            for row in range(0, 9):
                if self.tableWidget.item(row, coll) is not None:
                    item = self.tableWidget.item(row, coll).text()
                    item = float(item)
                else:
                    item = 0
                item = round(item / 1000, 3)
                data.append(item)
            sum_collumn = sum(data)
            sum_colls.append(sum_collumn)
        for i in sum_colls:
            total = round(i * count_ppl, 3)
            total_colls.append(total)
        coll = 2
        for i in sum_colls:
            temp = i
            coll = coll + 1
            self.tableWidget.setItem(9, coll, QTableWidgetItem(str(temp)))
        coll = 2
        for i in total_colls:
            temp = i
            coll = coll + 1
            self.tableWidget.setItem(10, coll, QTableWidgetItem(str(temp)))
        count_ppl_d = self.input_ppl_d.text()
        count_ppl_d = int(count_ppl_d)
        sum_colls_d = []
        total_colls_d = []
        for coll in range(3, self.tableWidget_2.columnCount()):
            data_d = []
            for row in range(0, 3):
                if self.tableWidget_2.item(row, coll) is not None:
                    item = self.tableWidget_2.item(row, coll).text()
                    item = float(item)
                else:
                    item = 0
                item = round(item / 1000, 3)
                data_d.append(item)
            sum_collumn_d = sum(data_d)
            sum_colls_d.append(sum_collumn_d)
        for i in sum_colls_d:
            total = round(i * count_ppl_d, 3)
            total_colls_d.append(total)
        coll = 2
        for i in sum_colls_d:
            temp = i
            coll = coll + 1
            self.tableWidget_2.setItem(4, coll, QTableWidgetItem(str(temp)))
        coll = 2
        for i in total_colls_d:
            temp = i
            coll = coll + 1
            self.tableWidget_2.setItem(5, coll, QTableWidgetItem(str(temp)))

    def push_to_database(self):
        signal = 3
        index_ch = (self.detachment[0],)
        date = (self.input_date.text(),)
        ppl = (self.input_ppl.text(),)
        ppl_d = (self.input_ppl_d.text(),)
        day_of_week = (self.input_day.currentText(),)
        row = 10
        data = []
        for coll in range(3, self.tableWidget.columnCount()):  # (3, self...)
            if self.tableWidget.item(row, coll) is not None:
                item = self.tableWidget.item(row, coll).text()
                item = float(item)
            else:
                item = 0
            data.append(item)
            val_ch = tuple(data)
        # add_n_to_db(signal, day_of_week, ppl, date, val_ch)
        add_n_to_db(signal, day_of_week, index_ch, ppl, date, val_ch)
        row_d = 4
        data_d = []
        for coll in range(3, self.tableWidget_2.columnCount()):  # (3, self...)
            if self.tableWidget_2.item(row_d, coll) is not None:
                item = self.tableWidget_2.item(row_d, coll).text()
                item = float(item)
            else:
                item = 0
            data_d.append(item)
            val_ch_d = tuple(data_d)
        # add_n_to_db(signal, day_of_week, ppl_d, date, val_ch_d)
        add_n_to_db(signal, day_of_week, index_ch, ppl_d, date, val_ch_d)

    def export_to_excel(self):
        columnHeaders = []
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                try:
                    temp = self.tableWidget.item(row, col).text()
                except:
                    temp = 0
                df.at[row, columnHeaders[col]] = temp
        # activate dialog-window for save file
        result1 = self.dialog.getSaveFileName(self.tableWidget, 'Зберегти файл', 'C:/', 'Excel files (*.xlsx)')
                # try-except block for saving file
        try:
            df.to_excel(result1[0])
        except:
            pass

        for j in range(self.tableWidget_2.model().columnCount()):
            columnHeaders.append(self.tableWidget_2.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
        for row in range(self.tableWidget_2.rowCount()):
            for col in range(self.tableWidget_2.columnCount()):
                try:
                    temp = self.tableWidget_2.item(row, col).text()
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


class MenuZvit(QWidget):
    def __init__(self, parent=None):
        super(MenuZvit, self).__init__()
        self.parent = parent
        self.names_columns = parse_column_db()[0]
        self.detachment = detachment
        self.names_columns = self.names_columns[2::]
        self.label_date1 = QLabel(self)
        self.label_date1.setText('Введіть початкову дату операції:')
        self.input_date1 = QDateEdit(self)
        self.input_date1.setCalendarPopup(True)
        self.input_date1.setDate(datetime.today())
        self.label_date2 = QLabel(self)
        self.label_date2.setText('Введіть кіневу дату операції:')
        self.input_date2 = QDateEdit(self)
        self.input_date2.setCalendarPopup(True)
        self.input_date2.setDate(datetime.today())
        # create table widget
        column_count = len(self.names_columns)
        self.tableWidget = QTableWidget(0, column_count)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
        # create button box
        self.form_button = QPushButton('   Сформувати таблицю')
        self.form_button.setIcon(QtGui.QIcon('icons/computer.png'))
        self.form_button.clicked.connect(self.show_table_func)
        self.excel_button = QPushButton('   Формувати у Excel')
        self.excel_button.setIcon(QtGui.QIcon('icons/excel.png'))
        self.excel_button.clicked.connect(self.export_to_excel)
        # create dialog-window for save file
        self.dialog = QFileDialog(self)

        main_box_layout = QVBoxLayout(self)
        input_form_layout = QFormLayout(self)
        input_form_layout.addRow(self.label_date1, self.input_date1)
        input_form_layout.addRow(self.label_date2, self.input_date2)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_button)
        button_layout.addWidget(self.excel_button)
        main_box_layout.addLayout(input_form_layout)
        main_box_layout.addWidget(self.tableWidget)
        main_box_layout.addLayout(button_layout)
        # add dialog-window for save file
        main_box_layout.addWidget(self.dialog)

    def show_table_func(self):
        index_ch = (self.detachment[0],)
        day1 = (self.input_date1.text(),)
        day2 = (self.input_date2.text(),)
        self.rows = parse_menu_loss_db(index_ch, day1, day2)
        self.tableWidget.setRowCount(len(self.rows)+1)
        row = -1
        for i in self.rows:
            temp = i[2::]
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1
        sum_colls = []

        for coll in range(2, self.tableWidget.columnCount()):
            data = []
            for row in range(0, len(self.rows)):
                if self.tableWidget.item(row, coll) is not None:
                    item = self.tableWidget.item(row, coll).text()
                    item = float(item)
                else:
                    item = 0
                item = item
                data.append(item)
            sum_collumn = sum(data)
            sum_colls.append(sum_collumn)
        coll = 2
        for i in sum_colls:
            temp = i
            temp = round(temp, 3)
            self.tableWidget.setItem(len(self.rows), coll, QTableWidgetItem(str(temp)))
            coll = coll + 1

    def export_to_excel(self):
        columnHeaders = []
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
        for row in range(self.tableWidget.rowCount()):
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


class Bread(QWidget):
    def __init__(self, parent=None):
        super(Bread, self).__init__()
        self.parent = parent
        self.detachment = detachment
        self.name_lables_one = columns_bread
        self.name_lables_two = columns_bread_act
        self.rows = rows_bread_act
        # create input fields
        self.label_date = QLabel(self)
        self.label_date.setText('Введіть дату операції:')
        self.input_date = QDateEdit(self)
        self.input_date.setCalendarPopup(True)
        self.input_date.setDate(datetime.today())
        self.label_bread = QLabel(self)
        self.label_bread.setText('Введіть кількість хліба:')
        self.input_bread = QLineEdit('0')
        # create tables
        self.tableWidget = QTableWidget(0, 17)  # +1
        self.tableWidget.setHorizontalHeaderLabels(self.name_lables_one)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_2 = QTableWidget(0, 6)  # +1
        self.tableWidget_2.setHorizontalHeaderLabels(self.name_lables_two)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_2.setColumnWidth(0, 300)
        # create buttons
        self.form_table_button = QPushButton('   Сформувати таблицю')
        self.form_table_button.setIcon(QtGui.QIcon('icons/computer.png'))
        self.form_table_button.clicked.connect(self.show_table_func)
        self.calculate_button = QPushButton('   Провести розрахунок')
        self.calculate_button.setIcon(QtGui.QIcon('icons/calculate.png'))
        self.calculate_button.clicked.connect(self.calculate_result)
        self.save_to_db_button = QPushButton('   Зберегти у Базу Даних')
        self.save_to_db_button.setIcon(QtGui.QIcon('icons/database.png'))
        self.save_to_db_button.clicked.connect(self.push_to_database)
        self.excel_button = QPushButton('   Формувати у Excel')
        self.excel_button.setIcon(QtGui.QIcon('icons/excel.png'))
        self.excel_button.clicked.connect(self.export_to_excel)
        # create dialog-window for save file
        self.dialog = QFileDialog(self)

        main_layout = QVBoxLayout(self)
        input_form_layout = QFormLayout(self)
        input_form_layout.addRow(self.label_date, self.input_date)
        input_form_layout.addRow(self.label_bread, self.input_bread)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_table_button)
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.save_to_db_button)
        button_layout.addWidget(self.excel_button)
        main_layout.addLayout(input_form_layout)
        main_layout.addWidget(self.tableWidget)
        main_layout.addWidget(self.tableWidget_2)
        main_layout.addLayout(button_layout)
        # add dialog-window for save file
        main_layout.addWidget(self.dialog)

    def show_table_func(self):
        self.tableWidget.setRowCount(1)
        self.tableWidget_2.setRowCount(6)
        date = self.input_date.text()
        bread = float(self.input_bread.text())
        out_p = 136.1
        oil_p = 0.141
        salt_p = 1.8
        yeast_p = 0.4
        bread_in_wheat = 0.73475
        wheat = round(bread * bread_in_wheat, 3)
        oil = round((wheat * oil_p) / 100, 3)
        salt = round((wheat * salt_p) / 100, 3)
        yeast = round((wheat * yeast_p) / 100, 3)

        values_list = [date, wheat, bread, out_p, out_p, oil, oil_p, oil, oil_p, salt, salt_p, salt, salt_p, yeast, yeast_p, yeast, yeast_p]
        names_numb = 0
        for column in range(17): # for column 1
            self.tableWidget.setItem(0, column, QTableWidgetItem(str(values_list[names_numb])))
            names_numb = names_numb+1
        rows = 0
        for row in range(6):
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(self.rows[rows])))
            rows = rows+1
        for row in range(5):
            self.tableWidget_2.setItem(row, 1, QTableWidgetItem(kg))

        self.tableWidget_2.setItem(0, 2, QTableWidgetItem(str(wheat)))
        self.tableWidget_2.setItem(1, 2, QTableWidgetItem(str(yeast)))
        self.tableWidget_2.setItem(2, 2, QTableWidgetItem(str(oil)))
        self.tableWidget_2.setItem(3, 2, QTableWidgetItem(str(salt)))
        self.tableWidget_2.setItem(4, 4, QTableWidgetItem(str(bread)))

    def calculate_result(self):
        try:
            wheat = self.tableWidget_2.item(0, 2).text()
            wheat = round(float(wheat), 3)
        except:
            wheat = 0
        try:
            wheat_price = self.tableWidget_2.item(0, 3).text()
            wheat_price = float(wheat_price)
        except:
            wheat_price = 0
        wheat_sum = round(wheat * wheat_price, 3)
        yeast = self.tableWidget_2.item(1, 2).text()
        yeast = round(float(yeast), 3)
        try:
            yeast_price = self.tableWidget_2.item(1, 3).text()
            yeast_price = float(yeast_price)
        except:
            yeast_price = 0
        yeast_sum = round(yeast * yeast_price, 3)

        oil = self.tableWidget_2.item(2, 2).text()
        oil = round(float(oil), 3)
        try:
            oil_price = self.tableWidget_2.item(2, 3).text()
            oil_price = float(oil_price)
        except:
            oil_price = 0
        oil_sum = round(oil * oil_price, 3)
        salt = self.tableWidget_2.item(3, 2).text()
        salt = round(float(salt), 3)
        try:
            salt_price = self.tableWidget_2.item(3, 3).text()
            salt_price = float(salt_price)
        except:
            salt_price = 0
        salt_sum = round(salt * salt_price, 3)
        sum_ingr = round(wheat + yeast + oil + salt, 3)
        self.tableWidget_2.setItem(5, 2, QTableWidgetItem(str(sum_ingr)))
        sum_ingredients = round(wheat_sum + yeast_sum + oil_sum + salt_sum, 3)
        self.tableWidget_2.setItem(5, 3, QTableWidgetItem(str(sum_ingredients)))
        self.tableWidget_2.setItem(5, 5, QTableWidgetItem(str(sum_ingredients)))
        try:
            bread = self.tableWidget_2.item(4, 4).text()
            bread = round(float(bread), 3)
            bread_price = round(sum_ingredients / bread, 3)
        except:
            bread_price = 0
        self.tableWidget_2.setItem(4, 5, QTableWidgetItem(str(bread_price)))

    def push_to_database(self):
        signal_b = 2
        index = (self.detachment[0],)
        date = (self.input_date.text(),)
        row = 0
        data = []
        for coll in range(1, self.tableWidget.columnCount()):  # (3, self...)
            if self.tableWidget.item(row, coll) is not None:
                item = self.tableWidget.item(row, coll).text()
                item = float(item)
            else:
                item = 0
            data.append(item)
            val_chs = tuple(data)
        add_bread_baking(index, date, val_chs) # +index

        data_baker = parse_bread_baking_db(signal_b, index, (0,), (0,))
        data_baker = data_baker[0]
        bread = (data_baker[3],)
        zero = (
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        val_ch = bread + zero
        number_ch = ('хліб',)
        signal = 1
        #add_n_to_db(signal, number_ch, number_ch, date_op, val_ch)
        add_n_to_db(signal, number_ch, index, number_ch, date, val_ch)

        signal = 2
        wheat = (data_baker[2],)
        oil = (data_baker[8],)
        salt = (data_baker[12],)
        yeast = (data_baker[16],)
        zero1 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        zero2 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        zero3 = (0,)
        zero4 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        zero5 = (0, 0, 0, 0, 0, 0, 0, 0)
        val_ch = zero1 + oil + zero2 + wheat + zero3 + salt + zero4 + yeast + zero5
        # add_n_to_db(signal, number_ch, number_ch, date_op, val_ch)
        add_n_to_db(signal, number_ch, index, number_ch, date, val_ch)

    def export_to_excel(self):
        column_headers = []
        for j in range(self.tableWidget_2.model().columnCount()):
            column_headers.append(self.tableWidget_2.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=column_headers)
        for row in range(self.tableWidget_2.rowCount()):
            for col in range(self.tableWidget_2.columnCount()):
                try:
                    temp = self.tableWidget_2.item(row, col).text()
                except:
                    temp = 0
                df.at[row, column_headers[col]] = temp
        # activate dialog-window for save file
        result = self.dialog.getSaveFileName(self.tableWidget, 'Зберегти файл', 'C:/', 'Excel files (*.xlsx)')
        # try-except block for saving file
        try:
            df.to_excel(result[0])
        except:
            pass


class BreadZvit(QWidget):
    def __init__(self, parent=None):
        super(BreadZvit, self).__init__()
        self.parent = parent
        self.detachment = detachment
        self.name_lables_one = columns_bread
        self.name_lables_two = columns_bread_act
        # create table
        self.tableWidget = QTableWidget(0, 17)  # +1
        self.tableWidget.setHorizontalHeaderLabels(self.name_lables_one)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        # create input date labels
        self.label_date1 = QLabel(self)
        self.label_date1.setText('Введіть початкову дату операції:')
        self.input_date1 = QDateEdit(self)
        self.input_date1.setCalendarPopup(True)
        self.input_date1.setDate(datetime.today())
        self.label_date2 = QLabel(self)
        self.label_date2.setText('Введіть кіневу дату операції:')
        self.input_date2 = QDateEdit(self)
        self.input_date2.setCalendarPopup(True)
        self.input_date2.setDate(datetime.today())
        # create buttons
        self.form_table_button = QPushButton('   Сформувати таблицю')
        self.form_table_button.setIcon(QtGui.QIcon('icons/computer.png'))
        self.form_table_button.clicked.connect(self.show_table_func)
        self.excel_button = QPushButton('   Формувати у Excel')
        self.excel_button.setIcon(QtGui.QIcon('icons/excel.png'))
        self.excel_button.clicked.connect(self.export_to_excel)
        # create dialog-window for save file
        self.dialog = QFileDialog(self)

        main_layout = QVBoxLayout(self)
        input_form_layout = QFormLayout(self)
        input_form_layout.addRow(self.label_date1, self.input_date1)
        input_form_layout.addRow(self.label_date2, self.input_date2)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_table_button)
        button_layout.addWidget(self.excel_button)
        main_layout.addLayout(input_form_layout)
        main_layout.addWidget(self.tableWidget)
        main_layout.addLayout(button_layout)
        # add dialog-window for save file
        main_layout.addWidget(self.dialog)

    def show_table_func(self):
        signal_b = 1
        index = (self.detachment[0],)
        day1 = (self.input_date1.text(),)
        day2 = (self.input_date2.text(),)
        self.rows = parse_bread_baking_db(signal_b, index, day1, day2)
        self.tableWidget.setRowCount(len(self.rows)+1)
        row = -1
        for i in self.rows:
            temp = i[1::]
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1
        sum_colls = []
        for coll in range(3, self.tableWidget.columnCount()):
            data = []
            for row in range(0, len(self.rows)):
                if self.tableWidget.item(row, coll) is not None:
                    item = self.tableWidget.item(row, coll).text()
                    item = float(item)
                else:
                    item = 0
                item = item
                data.append(item)
            sum_collumn = sum(data)
            sum_colls.append(sum_collumn)
        coll = 3
        for i in sum_colls:
            temp = i
            temp = round(temp, 3)
            self.tableWidget.setItem(len(self.rows), coll, QTableWidgetItem(str(temp)))
            coll = coll + 1

    def export_to_excel(self):
        columnHeaders = []
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)
        for row in range(self.tableWidget.rowCount()):
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


class MainStorage(QWidget):
    def __init__(self, parent=None):
        super(MainStorage, self).__init__()
        self.parent = parent
        # parse database
        self.name_lables = parse_column_db()
        # create table widget
        self.tableWidget = QTableWidget(0, 3) # rows, columns
        self.tableWidget.setHorizontalHeaderLabels(header_labels) # headers of columns on table
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.setColumnWidth(0, 350)
        # create button
        self.pushButton = QPushButton('   Сформувати таблицю')
        self.pushButton.setIcon(QtGui.QIcon('icons/computer.png'))
        self.pushButton.clicked.connect(self.show_table_func)
        # layout box
        vBox = QVBoxLayout(self)
        vBox.addWidget(self.tableWidget)
        vBox.addWidget(self.pushButton)

    def show_table_func(self):
        '''
        function for create and show data from 'main_file' table
        '''
        # table settings
        self.rows = parse_db()
        row_count = len(self.name_lables[0]) - 4
        self.tableWidget.setRowCount(row_count)
        # save tuples of values
        self.names = self.name_lables[0] #
        self.values = self.rows[0]

        names_numb = 4
        for row in range(row_count): # for column 1
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.names[names_numb])))
            names_numb = names_numb+1
        for row in range(row_count): # for column 2
            self.tableWidget.setItem(row, 1, QTableWidgetItem(kg))
        values_numb = 4
        for row in range(row_count):  # for column 3
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(self.values[values_numb])))
            values_numb = values_numb + 1


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
                                  text='enter index . . . ')
        global detachment
        detachment = self.detachment
        self.setCentralWidget(self.main_widget)

        self.main_widget.addTab(Storage(), "Залишки (Підрозділ)")
        self.main_widget.addTab(Rozkladka(), "Розкладка")
        self.main_widget.addTab(Menu(), "Меню-вимога")
        self.main_widget.addTab(MenuZvit(), "Меню-вимога звіт")
        self.main_widget.addTab(Bread(), "Хлібопечення")
        self.main_widget.addTab(BreadZvit(), "Хлібопечення звіт")
        self.main_widget.addTab(MainStorage(), "Залишки (Головний склад)")


### Final App Block ###
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create app
    # app.setStyle('Oxygen') # 'Breeze'
    dlgMain = MainWindow() # build object of class "DlgMain" and set here in variable "dlgMain"

    dlgMain.show() # show function
    sys.exit(app.exec_())  # loop app in "sys.exit" func for check logs

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
        row_count = len(self.names) - 3
        dtch = (self.detachment[0],)
        self.detachment_start = parse_db_detach_start(dtch)
        date_start = (self.detachment_start[0][3],)
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
        self.rows = parse_db_rozklad()
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
        self.save_to_db = QPushButton('   Зберегти у Базу Даних')
        self.save_to_db.setIcon(QtGui.QIcon('icons/database.png'))
        self.save_to_db.clicked.connect(self.delete_from_rozclad)
        self.save_to_db.clicked.connect(self.push_to_database)

        main_v_box = QVBoxLayout(self)
        button_v_box = QHBoxLayout(self)
        button_v_box.addWidget(self.form_table)
        button_v_box.addWidget(self.save_to_db)
        main_v_box.addWidget(self.tableWidget)
        main_v_box.addLayout(button_v_box)


    def show_table_func(self):
        self.tableWidget.setRowCount(65)
        row = -1
        for i in self.rows:
            temp = i
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1

    def push_to_database(self):
        for row in range(self.tableWidget.rowCount()):
            data = []
            for coll in range(self.tableWidget.columnCount()):
                if self.tableWidget.item(row, coll) is not None:
                    item = self.tableWidget.item(row, coll).text()
                else:
                    item = 0
                    item = str(item)
                data.append(item)
            val_roz = tuple(data)
            add_values_to_rozclad_db(val_roz)

    def delete_from_rozclad(self):
        clear_rozclad_db()


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
        # 2
        self.tableWidget_2 = QTableWidget(0, column_count)
        self.tableWidget_2.setHorizontalHeaderLabels(self.names_columns)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.setColumnWidth(2, 300)
        # create buttons
        # self.form_table = QPushButton('Сформувати таблицю')
        # self.form_table.clicked.connect(self.show_table_func)
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
        self.tableWidget_2.setRowCount(5)
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
            self.tableWidget_2.setItem(3, coll, QTableWidgetItem(str(temp)))
        coll = 2
        for i in total_colls_d:
            temp = i
            coll = coll + 1
            self.tableWidget_2.setItem(4, coll, QTableWidgetItem(str(temp)))



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
        self.main_widget.addTab(Rozkladka(), "Розкладка")
        self.main_widget.addTab(Menu(), "Меню-вимога")




### Final App Block ###
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create app
    # app.setStyle('Oxygen') # 'Breeze'
    dlgMain = MainWindow() # build object of class "DlgMain" and set here in variable "dlgMain"

    dlgMain.show() # show function
    sys.exit(app.exec_())  # loop app in "sys.exit" func for check logs

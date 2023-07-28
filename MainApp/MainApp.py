import sys
from datetime import datetime, time
import pandas as pd
from PyQt5.QtGui import QFont# QIcon, QPixmap,
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from Database.sql_handlers import *


### Constants ###
today = datetime.today().strftime("%d.%m.%Y")
day_of_week = datetime.today().isoweekday()
header_labels = ['Найменування', 'од. виміру', 'кількість']
kg = 'кг'
columns_for_rozclad = ('День тижня', 'Прийом їжі', 'Страва')
columns_bread = ['Дата', 'Витрачено \nборошна', 'Отримано \nхліба', 'Вихід \nплановий \n(%)', 'Вихід \nфактичний \n(%)', 'Олія\nза нормою\nв кг', 'Олія\nза нормою\nв %', 'Олія\nфактично\nв кг', 'Олія\nфактично\nв %', 'Сіль\nза нормою\nв кг', 'Сіль\nза нормою\nв %', 'Сіль\nфактично\nв кг', 'Сіль\nфактично\nв %', 'Дріжджі\nза нормою\nв кг', 'Дріжджі\nза нормою\nв %', 'Дріжджі\nфактично\nв кг', 'Дріжджі\nфактично\nв %']
columns_bread_act = ['Найменування \nматеріальних \nзасобів', 'Одиниця \nвиімру', 'Витрачено \nсировини', 'ціна \nза од.', 'Отримано \nпродукції', 'ціна \nза од.']
rows_bread_act = ['Борошно пшеничне \nІ гат', 'Дріжджі сухі', 'Олія', 'Сіль', 'Хліб пшеничний \nз борошна І гат.', 'ВСЬОГО:']


class Storage(QWidget):

    def __init__(self, parent=None):
        super(Storage, self).__init__()
        self.parent = parent
        # parse database
        self.name_lables = parse_column_db()
        self.rows = parse_db()
        # create table widget
        self.tableWidget = QTableWidget(0, 3) # rows, columns
        self.tableWidget.setHorizontalHeaderLabels(header_labels) # headers of columns on table
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        # create button
        self.pushButton = QPushButton('Show table')
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
        row_count = len(self.name_lables[0]) - 3
        self.tableWidget.setRowCount(row_count)
        # save tuples of values
        self.names = self.name_lables[0] #
        self.values = self.rows[0]

        names_numb = 3
        for row in range(row_count): # for column 1
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.names[names_numb])))
            names_numb = names_numb+1
        for row in range(row_count): # for column 2
            self.tableWidget.setItem(row, 1, QTableWidgetItem(kg))
        values_numb = 3
        for row in range(row_count):  # for column 3
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(self.values[values_numb])))
            values_numb = values_numb + 1


class LossProfitTab(QWidget):
    def __init__(self, parent=None):
        self.parent = parent
        super(LossProfitTab, self).__init__()
        self.parent = parent
        # parse database
        self.name_lables = parse_column_db()
        # create input fields
        self.label_date = QLabel(self)
        self.label_date.setText('Введіть дату операції:')
        self.input_date = QLineEdit(today)
        unk = '1111'#'UNKNOWN'
        self.label_pidr = QLabel(self)
        self.label_pidr.setText('Введіть номер військової частини:') #
        self.input_pidr = QLineEdit(unk)
        self.label_pidr_name = QLabel(self)
        self.label_pidr_name.setText('Введіть назву військової частини:') #
        self.input_pidr_name = QLineEdit(unk)
        self.label_detach_list = QLabel(self)
        self.label_detach_list.setText('Оберіть підрозділ:') #
        self.input_detach_list = QComboBox(self)
        self.input_detach_list.addItems(['---', 'first', 'second'])
        # self.input_detach_list = QLineEdit(unk)
        self.label_name = QLabel(self)
        self.label_name.setText('Введіть прізвище, ім’я того, через кого здійснюєтся операція:')
        self.input_name = QLineEdit(unk)
        self.label_operation = QLabel(self)
        self.label_operation.setText("Оберіть тип операції")
        self.button_group = QButtonGroup()
        self.check_op_prof = QRadioButton('Profit')
        self.check_op_prof_p = QRadioButton('Profit of PODK')
        self.check_op_loss = QRadioButton('Loss')
        self.check_op_loss_p = QRadioButton('Loss of PODK')
        self.button_group.addButton(self.check_op_prof, 1)
        self.button_group.addButton(self.check_op_prof_p, 2)
        self.button_group.addButton(self.check_op_loss, 4)
        self.button_group.addButton(self.check_op_loss_p, 5)
        # create table widget
        self.tableWidget = QTableWidget(0, 3) # rows, columns
        self.tableWidget.setHorizontalHeaderLabels(header_labels) # headers of columns on table
        self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        # create buttons
        self.form_table = QPushButton('Сформувати таблицю')
        self.form_table.clicked.connect(self.show_table_func)
        self.save_to_db = QPushButton('Зберегти у Базу Даних')
        self.save_to_db.clicked.connect(self.push_to_database)
        self.form_excel = QPushButton('Формувати у Excel')
        self.form_excel.clicked.connect(self.export_to_excel)

        # self.connect(self.check_op_loss, QtCore.SIGNAL('clicked()'), self.input_detach_list, QtCore.SLOT('setDisabled()'))



        # layout box
        mainLayout = QVBoxLayout(self)
        in_date_layout = QHBoxLayout(self)
        in_date_layout.addWidget(self.label_date)
        in_date_layout.addWidget(self.input_date)
        in_pidr_layout = QHBoxLayout(self)
        in_pidr_layout.addWidget(self.label_pidr)
        in_pidr_layout.addWidget(self.input_pidr)
        in_pidr_name_layout = QHBoxLayout(self)
        in_pidr_name_layout.addWidget(self.label_pidr_name)
        in_pidr_name_layout.addWidget(self.input_pidr_name)
        in_detach_list_layout = QHBoxLayout(self)
        in_detach_list_layout.addWidget(self.label_detach_list)
        in_detach_list_layout.addWidget(self.input_detach_list)
        in_name_layout = QHBoxLayout(self)
        in_name_layout.addWidget(self.label_name)
        in_name_layout.addWidget(self.input_name)
        in_opper_type_layout = QHBoxLayout(self)
        in_opper_type_layout.addWidget(self.label_operation)
        in_opper_type_layout.addWidget(self.check_op_prof)
        in_opper_type_layout.addWidget(self.check_op_prof_p)
        in_opper_type_layout.addWidget(self.check_op_loss)
        in_opper_type_layout.addWidget(self.check_op_loss_p)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_table)
        button_layout.addWidget(self.save_to_db)
        button_layout.addWidget(self.form_excel)

        mainLayout.addLayout(in_date_layout)
        mainLayout.addLayout(in_opper_type_layout)
        mainLayout.addLayout(in_pidr_layout)
        mainLayout.addLayout(in_pidr_name_layout)
        mainLayout.addLayout(in_detach_list_layout)
        mainLayout.addLayout(in_name_layout)
        mainLayout.addWidget(self.tableWidget)
        mainLayout.addLayout(button_layout)

    def show_table_func(self):
        """
        function for create and show data from 'main_file' table
        """
        # table settings
        row_count = len(self.name_lables[0]) - 3
        self.tableWidget.setRowCount(row_count)
        # save tuples of values
        self.names = self.name_lables[0]  #
        # self.values = self.rows[0]
        names_numb = 3
        for row in range(row_count):  # for column 1
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(self.names[names_numb])))
            names_numb = names_numb + 1
        for row in range(row_count):  # for column 2
            self.tableWidget.setItem(row, 1, QTableWidgetItem(kg))

    def enabled(self):
        pass

    def push_to_database(self):
        signal = 1
        checket_btn = self.button_group.checkedButton()
        checket_btn_txt = self.button_group.checkedId()
        print(checket_btn_txt)
        if checket_btn_txt == 2:
            #self.input_detach_list.setDisabled(False)
            signal = 2
        # print(signal)
        date = self.input_date.text()

        item = self.input_pidr.text()
        item = int(item)
        date_op = (date,)
        number_ch = (item,)
        column = 2
        data = []
        row_count = len(self.name_lables[0]) - 3

        for row in range(row_count):
            if self.tableWidget.item(row, column) is not None:
                item = self.tableWidget.item(row, column).text()
                item = int(item)
            else:
                item = 0
            data.append(item)
            val_ch = tuple(data)
        add_n_to_db(signal, number_ch, date_op, val_ch)


    def export_to_excel(self):
        time_date = time.ctime()
        name = self.input_pidr.text()
        time_file = time_date[4:10]
        format_file = '.xlsx'
        file = name + '.' + time_file + format_file
        columnHeaders = []
        row_count = len(self.name_lables[0]) - 2
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())
            df = pd.DataFrame(columns=columnHeaders)#pd.DataFrame(columns=columnHeaders)
        for row in range(row_count):
            for col in range(self.tableWidget.columnCount()):
                try:
                    temp = self.tableWidget.item(row, col).text()
                except:
                    temp = 0
                print(temp)

                df.at[row, columnHeaders[col]] = temp
                df.to_excel(file)


class Rozkladka(QWidget):

    def __init__(self, parent=None):
        super(Rozkladka, self).__init__()
        self.parent = parent

        self.rows = parse_db_rozklad()
        self.lables_main = columns_for_rozclad
        self.name_lables_one = parse_column_db()
        self.name_lables = self.name_lables_one[0]
        self.name_lables = self.name_lables[2:]
        self.names_columns = self.lables_main + self.name_lables
        column_count = len(self.names_columns)
        self.tableWidget = QTableWidget(0, column_count)
        self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        # create buttons
        self.form_table = QPushButton('Сформувати таблицю')
        self.form_table.clicked.connect(self.show_table_func)
        self.save_to_db = QPushButton('Зберегти у Базу Даних')
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
        default_day = 'Понеділок'

        self.rows = parse_db_rozklad()
        self.lables_main = columns_for_rozclad
        self.name_lables_one = parse_column_db()
        self.name_lables = self.name_lables_one[0]
        self.name_lables = self.name_lables[2:]
        self.names_columns = self.lables_main + self.name_lables
        column_count = len(self.names_columns)
        # create input fields
        self.label_date = QLabel(self)
        self.label_date.setText('Введіть дату операції:')
        self.input_date = QLineEdit(today)
        self.label_ppl = QLabel(self)
        self.label_ppl.setText('Введіть кількість людей:')
        self.input_ppl = QLineEdit(zero_people)
        self.label_ppl_d = QLabel(self)
        self.label_ppl_d.setText('Введіть кількість людей на обід:')
        self.input_ppl_d = QLineEdit(zero_people)
        default_day = 'Понеділок'
        self.label_day = QLabel(self)
        self.label_day.setText('Введіть день тижня:')
        # self.input_day = QLineEdit(default_day) # fix on list-down widget
        self.input_day = QComboBox(self)
        self.input_day.addItems(['---', 'Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П’ятниця', 'Субота', 'Неділя'])
        self.input_day.currentTextChanged.connect(self.show_table_func)
        # create tables
        self.tableWidget = QTableWidget(0, column_count)
        self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        # 2
        self.tableWidget_2 = QTableWidget(0, column_count)
        self.tableWidget_2.setHorizontalHeaderLabels(self.names_columns)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(120)
        # create buttons
        # self.form_table = QPushButton('Сформувати таблицю')
        # self.form_table.clicked.connect(self.show_table_func)
        self.calculate = QPushButton('Розрахувати')
        self.calculate.clicked.connect(self.calculate_result)
        self.save_to_db = QPushButton('Зберегти у Базу Даних')
        self.save_to_db.clicked.connect(self.push_to_database)
        self.to_excell = QPushButton('Формувати у Excel')
        self.to_excell.clicked.connect(self.export_to_excel)

        main_v_box = QVBoxLayout(self)
        in_date_layout = QHBoxLayout(self) #1
        in_date_layout.addWidget(self.label_date)
        in_date_layout.addWidget(self.input_date)
        in_ppl_all_layout = QHBoxLayout(self)#2
        in_ppl_all_layout.addWidget(self.label_ppl)
        in_ppl_all_layout.addWidget(self.input_ppl)
        in_ppl_d_layout = QHBoxLayout(self)#3
        in_ppl_d_layout.addWidget(self.label_ppl_d)
        in_ppl_d_layout.addWidget(self.input_ppl_d)
        in_day_layout = QHBoxLayout(self)#4
        in_day_layout.addWidget(self.label_day)
        in_day_layout.addWidget(self.input_day)
        button_layout = QHBoxLayout(self)#6
        # button_layout.addWidget(self.form_table)
        button_layout.addWidget(self.calculate)
        button_layout.addWidget(self.save_to_db)
        button_layout.addWidget(self.to_excell)
        main_v_box.addLayout(in_date_layout)
        main_v_box.addLayout(in_ppl_all_layout)
        main_v_box.addLayout(in_ppl_d_layout)
        main_v_box.addLayout(in_day_layout)
        main_v_box.addWidget(self.tableWidget)
        main_v_box.addWidget(self.tableWidget_2)
        main_v_box.addLayout(button_layout)

    def show_table_func(self, day):
        self.tableWidget.setRowCount(11)
        self.tableWidget_2.setRowCount(5)
        day = day
        day = (day,)
        # print(day, type(day))
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
        date = self.input_date.text()
        item = self.input_ppl.text()
        item_d = self.input_ppl_d.text()
        date_op = (date,)
        item = int(item)
        item_d = int(item_d)
        ppl = (item,)
        ppl_d = (item_d,)
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
        add_n_to_db(signal, ppl, date_op, val_ch)

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
        add_n_to_db(signal, ppl_d, date_op, val_ch_d)

    def export_to_excel(self):
        timedate = time.ctime()
        ppl = self.input_ppl.text()
        ppl_d = self.input_ppl_d.text()
        timefile = timedate[4:10]
        dinner = ' Обід'
        formatfile = '.xlsx'
        file = ppl + ' чол.' + timefile + formatfile
        file_d = ppl_d + ' чол.' + timefile + dinner + formatfile
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
                df.to_excel(file)

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
                df.to_excel(file_d)


class MenuZvit(QWidget):

    def __init__(self, parent=None):
        super(MenuZvit, self).__init__()
        self.parent = parent
        self.names_columns = parse_column_db()[0]
        ppl_col_name = ('Кількість людей',)
        self.names_columns = self.names_columns[1::]
        self.names_columns = ppl_col_name+self.names_columns
        #print(self.names_columns)
        # create input date labels
        self.label_date1 = QLabel(self)
        self.label_date1.setText('Введіть початкову дату операції:')
        self.input_date1 = QLineEdit(today)
        self.label_date2 = QLabel(self)
        self.label_date2.setText('Введіть кіневу дату операції:')
        self.input_date2 = QLineEdit(today)
        # create table widget
        column_count = len(self.names_columns)
        self.tableWidget = QTableWidget(0, column_count)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.setHorizontalHeaderLabels(self.names_columns)
        # create button box
        self.form_button = QPushButton('Сформувати таблицю')
        self.form_button.clicked.connect(self.show_table_func)
        self.excel_button = QPushButton('Формувати у Excel')
        self.excel_button.clicked.connect(self.export_to_excel)

        main_box_layout = QVBoxLayout(self)
        in_data_1layout = QHBoxLayout(self)
        in_data_1layout.addWidget(self.label_date1)
        in_data_1layout.addWidget(self.input_date1)
        in_data_2layout = QHBoxLayout(self)
        in_data_2layout.addWidget(self.label_date2)
        in_data_2layout.addWidget(self.input_date2)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_button)
        button_layout.addWidget(self.excel_button)
        main_box_layout.addLayout(in_data_1layout)
        main_box_layout.addLayout(in_data_2layout)
        main_box_layout.addWidget(self.tableWidget)
        main_box_layout.addLayout(button_layout)

    def show_table_func(self):
        day1 = self.input_date1.text()
        day1 = (day1,)
        day2 = self.input_date2.text()
        day2 = (day2,)
        self.rows = parse_menu_loss_db(day1, day2)
        self.tableWidget.setRowCount(len(self.rows)+1)
        row = -1
        for i in self.rows:
            temp = i
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1
        sum_colls = []
        total_colls = []
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
        day1 = self.input_date1.text()
        day2 = self.input_date2.text()
        name = 'Зведена відомість за період '
        formatfile = '.xlsx'
        file = name + day1 + ' - ' + day2 + formatfile
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
                df.to_excel(file)


class Bread(QWidget):

    def __init__(self, parent=None):
        super(Bread, self).__init__()
        self.parent = parent
        self.name_lables_one = columns_bread
        self.name_lables_two = columns_bread_act
        self.rows = rows_bread_act
        # create input fields
        self.label_date = QLabel(self)
        self.label_date.setText('Введіть дату операції:')
        self.input_date = QLineEdit(today)
        nulll = '0'
        self.label_bread = QLabel(self)
        self.label_bread.setText('Введіть кількість хліба:')
        self.input_bread = QLineEdit(nulll)
        # create tables
        self.tableWidget = QTableWidget(0, 17)  # +1
        self.tableWidget.setHorizontalHeaderLabels(self.name_lables_one)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)

        self.tableWidget_2 = QTableWidget(0, 6)  # +1
        self.tableWidget_2.setHorizontalHeaderLabels(self.name_lables_two)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(160)
        # create buttons
        self.form_table_button = QPushButton('Сформувати таблицю')
        self.form_table_button.clicked.connect(self.show_table_func)
        self.calculate_button = QPushButton('Провести розрахунок')
        self.calculate_button.clicked.connect(self.calculate_result)
        self.save_to_db_button = QPushButton('Зберегти у Базу Даних')
        self.save_to_db_button.clicked.connect(self.push_to_database)
        self.excel_button = QPushButton('Формувати у Excel')
        self.excel_button.clicked.connect(self.export_to_excel)

        main_layout = QVBoxLayout(self)
        input_date_layout = QHBoxLayout(self)
        input_date_layout.addWidget(self.label_date)
        input_date_layout.addWidget(self.input_date)
        input_bread_layout = QHBoxLayout(self)
        input_bread_layout.addWidget(self.label_bread)
        input_bread_layout.addWidget(self.input_bread)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_table_button)
        button_layout.addWidget(self.calculate_button)
        button_layout.addWidget(self.save_to_db_button)
        button_layout.addWidget(self.excel_button)

        main_layout.addLayout(input_date_layout)
        main_layout.addLayout(input_bread_layout)
        main_layout.addWidget(self.tableWidget)
        main_layout.addWidget(self.tableWidget_2)
        main_layout.addLayout(button_layout)

    def show_table_func(self):
        self.tableWidget.setRowCount(1)
        self.tableWidget_2.setRowCount(6)
        date = self.input_date.text()
        bread = self.input_bread.text()
        bread = float(bread)
        date_t = (date,)
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
        wheat = self.tableWidget_2.item(0, 2).text()
        wheat = float(wheat)
        if self.tableWidget_2.item(0, 3) is not None:
            wheat_price = self.tableWidget_2.item(0, 3).text()
            wheat_price = float(wheat_price)
        else:
            wheat_price = 0
        wheat_sum = round(wheat * wheat_price, 3)
        yeast = self.tableWidget_2.item(1, 2).text()
        yeast = float(yeast)
        if self.tableWidget_2.item(1, 3) is not None:
            yeast_price = self.tableWidget_2.item(1, 3).text()
            yeast_price = float(yeast_price)
        else:
            yeast_price = 0
        yeast_sum = round(yeast * yeast_price, 3)

        oil = self.tableWidget_2.item(2, 2).text()
        oil = float(oil)
        if self.tableWidget_2.item(2, 3) is not None:
            oil_price = self.tableWidget_2.item(2, 3).text()
            oil_price = float(oil_price)
        else:
            oil_price = 0
        oil_sum = round(oil * oil_price, 3)
        salt = self.tableWidget_2.item(3, 2).text()
        salt = float(salt)
        if self.tableWidget_2.item(3, 3) is not None:
            salt_price = self.tableWidget_2.item(3, 3).text()
            salt_price = float(salt_price)
        else:
            salt_price = 0
        salt_sum = round(salt * salt_price, 3)
        sum_ingr = round(wheat + yeast + oil + salt, 3)
        self.tableWidget_2.setItem(5, 2, QTableWidgetItem(str(sum_ingr)))
        sum_ingredients = wheat_sum + yeast_sum + oil_sum + salt_sum
        self.tableWidget_2.setItem(5, 3, QTableWidgetItem(str(sum_ingredients)))
        self.tableWidget_2.setItem(5, 5, QTableWidgetItem(str(sum_ingredients)))
        bread = self.tableWidget_2.item(4, 4).text()
        bread = float(bread)
        bread_price = round(sum_ingredients / bread, 3)
        self.tableWidget_2.setItem(4, 5, QTableWidgetItem(str(bread_price)))

    def push_to_database(self):
        signal_b = 2
        index = ('bread',)
        date = self.tableWidget.item(0, 0).text()
        date_op = (date,)
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
        add_bread_baking(date_op, val_chs)
        data_baker = parse_bread_baking_db(signal_b)
        data_baker = data_baker[0]
        bread = (data_baker[2],)
        zero = (
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        val_ch = bread + zero
        number_ch = index
        signal = 1
        add_n_to_db(signal, number_ch, date_op, val_ch)
        signal = 2
        wheat = (data_baker[1],)
        oil = (data_baker[8],)
        salt = (data_baker[11],)
        yeast = (data_baker[15],)
        zero1 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        zero2 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        zero3 = (0,)
        zero4 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        zero5 = (0, 0, 0, 0, 0, 0, 0, 0)
        val_ch = zero1 + oil + zero2 + wheat + zero3 + salt + zero4 + yeast + zero5
        add_n_to_db(signal, number_ch, date_op, val_ch)

    def export_to_excel(self):
        time_date = time.ctime()
        time_file = time_date[4:10]
        bread = 'Хліб '
        format_file = '.xlsx'
        file = bread + time_file + format_file
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
                df.to_excel(file)


class BreadZvit(QWidget):

    def __init__(self, parent=None):
        super(BreadZvit, self).__init__()
        self.parent = parent
        self.name_lables_one = columns_bread
        self.name_lables_two = columns_bread_act
        signal = 1
        self.rows = parse_bread_baking_db(signal)
        # create table
        self.tableWidget = QTableWidget(0, 17)  # +1
        self.tableWidget.setHorizontalHeaderLabels(self.name_lables_one)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        # create buttons
        self.form_table_button = QPushButton('Сформувати таблицю')
        self.form_table_button.clicked.connect(self.show_table_func)
        self.excel_button = QPushButton('Формувати у Excel')
        self.excel_button.clicked.connect(self.export_to_excel)

        main_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_table_button)
        button_layout.addWidget(self.excel_button)
        main_layout.addWidget(self.tableWidget)
        main_layout.addLayout(button_layout)

    def show_table_func(self):
        pass
        # table settings
        row_count = len(self.rows)
        self.tableWidget.setRowCount(row_count)
        # # save tuples of values
        # self.names = self.name_lables[0] #
        self.values = self.rows[0]

        row = -1
        for i in self.rows:
            temp = i
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1

    def export_to_excel(self):
        time_date = time.ctime()
        time_file = time_date[4:7]
        bread = 'Звіт хлібопечення '
        format_file = '.xlsx'
        file = bread + time_file + format_file
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
                df.to_excel(file)


class ProfitLossZvit(QWidget):

    def __init__(self, parent=None):
        super(ProfitLossZvit, self).__init__()
        self.parent = parent
        self.names_columns = parse_column_db()[0]
        self.names_columns = self.names_columns[1::]
        # self.names_columns = ppl_col_name+self.names_columns
        #print(self.names_columns)
        # create input date labels
        self.label_date1 = QLabel(self)
        self.label_date1.setText('Введіть початкову дату операції:')
        self.input_date1 = QLineEdit(today)
        self.label_date2 = QLabel(self)
        self.label_date2.setText('Введіть кіневу дату операції:')
        self.input_date2 = QLineEdit(today)
        self.label_op = QLabel(self)
        self.label_op.setText('Введіть назву операції:')
        self.input_op = QComboBox(self)
        self.input_op.addItems(['Надходження', 'Видатки'])
        # create table widget
        column_count = len(self.names_columns)
        self.tableWidget = QTableWidget(0, column_count)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.setHorizontalHeaderLabels(self.names_columns)

        # create button box
        self.form_button = QPushButton('Сформувати таблицю')
        self.form_button.clicked.connect(self.show_table_func)
        self.excel_button = QPushButton('Формувати у Excel')
        self.excel_button.clicked.connect(self.export_to_excel)

        main_box_layout = QVBoxLayout(self)
        in_data_1layout = QHBoxLayout(self)
        in_data_1layout.addWidget(self.label_date1)
        in_data_1layout.addWidget(self.input_date1)
        in_data_1layout.addWidget(self.label_op)
        in_data_1layout.addWidget(self.input_op)
        in_data_2layout = QHBoxLayout(self)
        in_data_2layout.addWidget(self.label_date2)
        in_data_2layout.addWidget(self.input_date2)
        button_layout = QHBoxLayout(self)
        button_layout.addWidget(self.form_button)
        button_layout.addWidget(self.excel_button)
        main_box_layout.addLayout(in_data_1layout)
        main_box_layout.addLayout(in_data_2layout)
        main_box_layout.addWidget(self.tableWidget)
        main_box_layout.addLayout(button_layout)

    def show_table_func(self):
        signal = 0
        text = self.input_op.currentText()
        if text == 'Надходження':
            signal = 1
        elif text == 'Видатки':
            signal = 2

        day1 = self.input_date1.text()
        day1 = (day1,)
        day2 = self.input_date2.text()
        day2 = (day2,)
        self.rows = parse_loss_profit_db(signal, day1, day2)
        self.tableWidget.setRowCount(len(self.rows))
        row = -1
        for i in self.rows:
            temp = i
            row = row + 1
            count = 0
            for j in temp:
                self.tableWidget.setItem(row, count, QTableWidgetItem(str(temp[count])))
                count = count+1

    def export_to_excel(self):
        day1 = self.input_date1.text()
        day2 = self.input_date2.text()
        name = self.input_op.currentText()
        format_file = '.xlsx'
        file = name + ' за період ' + day1 + '-' + day2 + format_file
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
                df.to_excel(file)


class CreateDetachment(QWidget):
    def __init__(self, parent=None):
        super(CreateDetachment, self).__init__()
        self.parent = parent

        self.label_main = QLabel(self)
        self.label_main.setText('Введіть дані підрозділів:')
        self.label_main.setFont(QFont("Times New Roman", 16, 50))
        self.label_main2 = QLabel(self)

        self.label_detach_name1 = QLabel(self)
        self.label_detach_name1.setText('Введіть назву підрозділу:')
        self.input_detach_name1 = QLineEdit(self)
        self.label_detach_index1 = QLabel(self)
        self.label_detach_index1.setText('Введіть індекс підрозділу:')
        self.input_detach_index1 = QLineEdit(self)

        self.label_detach_name2 = QLabel(self)
        self.label_detach_name2.setText('Введіть назву підрозділу:')
        self.input_detach_name2 = QLineEdit(self)
        self.label_detach_index2 = QLabel(self)
        self.label_detach_index2.setText('Введіть індекс підрозділу:')
        self.input_detach_index2 = QLineEdit(self)

        self.label_detach_name3 = QLabel(self)
        self.label_detach_name3.setText('Введіть назву підрозділу:')
        self.input_detach_name3 = QLineEdit(self)
        self.label_detach_index3 = QLabel(self)
        self.label_detach_index3.setText('Введіть індекс підрозділу:')
        self.input_detach_index3 = QLineEdit(self)

        self.label_detach_name4 = QLabel(self)
        self.label_detach_name4.setText('Введіть назву підрозділу:')
        self.input_detach_name4 = QLineEdit(self)
        self.label_detach_index4 = QLabel(self)
        self.label_detach_index4.setText('Введіть індекс підрозділу:')
        self.input_detach_index4 = QLineEdit(self)

        self.label_detach_name5 = QLabel(self)
        self.label_detach_name5.setText('Введіть назву підрозділу:')
        self.input_detach_name5 = QLineEdit(self)
        self.label_detach_index5 = QLabel(self)
        self.label_detach_index5.setText('Введіть індекс підрозділу:')
        self.input_detach_index5 = QLineEdit(self)

        self.save_btn = QPushButton('Зберегти у базу даних')


        main_box_layout = QVBoxLayout(self)

        in_data_1_layout = QHBoxLayout(self)
        in_data_1_layout.addWidget(self.label_detach_name1)
        in_data_1_layout.addWidget(self.input_detach_name1)
        in_data_1_layout.addWidget(self.label_detach_index1)
        in_data_1_layout.addWidget(self.input_detach_index1)

        in_data_2_layout = QHBoxLayout(self)
        in_data_2_layout.addWidget(self.label_detach_name2)
        in_data_2_layout.addWidget(self.input_detach_name2)
        in_data_2_layout.addWidget(self.label_detach_index2)
        in_data_2_layout.addWidget(self.input_detach_index2)

        in_data_3_layout = QHBoxLayout(self)
        in_data_3_layout.addWidget(self.label_detach_name3)
        in_data_3_layout.addWidget(self.input_detach_name3)
        in_data_3_layout.addWidget(self.label_detach_index3)
        in_data_3_layout.addWidget(self.input_detach_index3)

        in_data_4_layout = QHBoxLayout(self)
        in_data_4_layout.addWidget(self.label_detach_name4)
        in_data_4_layout.addWidget(self.input_detach_name4)
        in_data_4_layout.addWidget(self.label_detach_index4)
        in_data_4_layout.addWidget(self.input_detach_index4)

        in_data_5_layout = QHBoxLayout(self)
        in_data_5_layout.addWidget(self.label_detach_name5)
        in_data_5_layout.addWidget(self.input_detach_name5)
        in_data_5_layout.addWidget(self.label_detach_index5)
        in_data_5_layout.addWidget(self.input_detach_index5)

        main_box_layout.addWidget(self.label_main)
        main_box_layout.addWidget(self.label_main2)
        main_box_layout.addLayout(in_data_1_layout)
        main_box_layout.addLayout(in_data_2_layout)
        main_box_layout.addLayout(in_data_3_layout)
        main_box_layout.addLayout(in_data_4_layout)
        main_box_layout.addLayout(in_data_5_layout)
        main_box_layout.addStretch()
        main_box_layout.addWidget(self.save_btn)


class MainWindow(QMainWindow):#, QDialog):
    """
    MAIN window Class
    """
    def __init__(self):
        # "__init__" func for initialization widgets and properties
        super().__init__() # initialization widgets and properties Parent class "QDialog"
        # in here we set widgets and set properties
        self.setWindowTitle("My App") # title of app
        self.resize(950, 1000) # set size window
        font = QFont("Times New Roman", 14, 75, True) # set font window
        # add widgets
        self.main_widget = QTabWidget()
        self.setCentralWidget(self.main_widget)
        self.main_widget.addTab(Storage(), "Storage")
        self.main_widget.addTab(LossProfitTab(), "Loss Profit Tab")
        self.main_widget.addTab(Rozkladka(), "Rozcladka")
        self.main_widget.addTab(Menu(), "Menu")
        self.main_widget.addTab(MenuZvit(), "Menu Zvit")
        self.main_widget.addTab(Bread(), "Bread")
        self.main_widget.addTab(BreadZvit(), "BreadZvit")
        self.main_widget.addTab(ProfitLossZvit(), "ProfitLossZvit")
        self.main_widget.addTab(CreateDetachment(), "CreateDetachments")


### Final App Block ###
if __name__ == '__main__':
    app = QApplication(sys.argv)  # create app
    dlgMain = MainWindow() # build object of class "DlgMain" and set here in variable "dlgMain"
    dlgMain.setWindowTitle('eBook')
    # dlgMain.setWindowIcon(QtGui.QIcon('icon.png'))
    dlgMain.show() # show function
    sys.exit(app.exec_())  # loop app in "sys.exit" func for check logs



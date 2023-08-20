import sqlite3
from datetime import datetime

date = datetime.today().strftime("%d.%m.%Y")

# functions of parsing databases
def parse_column_db():
    '''
    function for parsing product names
    '''
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    data = ('''SELECT * FROM names_prod''')
    cursor.execute(data)
    records = cursor.fetchall()
    return records


def parse_db_detach_start(detachment):
    # функция для извлечения данных из бд отделов
    conn = sqlite3.connect('Database/prod_database.db') # Database/prod_database.db
    cursor = conn.cursor()

    data = ('''SELECT * FROM detach_start_zvit WHERE index_db = ?''')


    cursor.execute(data, (detachment))
    records = cursor.fetchall()

    return records


def parse_db_detach_loss(data_d): # fix it with dates

    # функция для извлечения данных из бд отделов
    conn = sqlite3.connect('Database/prod_database.db') # Database/prod_database.db
    cursor = conn.cursor()

    data = ('''SELECT * FROM detach_loss WHERE index_db = ? AND дата BETWEEN ? AND ?''')

    cursor.execute(data, (data_d))
    records = cursor.fetchall()

    return records


def parse_db_detach_profit(data_d): # fix it with dates
    # функция для извлечения данных из бд отделов
    conn = sqlite3.connect('Database/prod_database.db') # Database/prod_database.db
    cursor = conn.cursor()


    data = ('''SELECT * FROM detach_profit WHERE index_db = ? AND дата BETWEEN ? AND ?''')
    cursor.execute(data, (data_d))
    records = cursor.fetchall()

    return records


def parse_db_detach_actual(detachment):
    # функция для извлечения данных из бд отделов
    conn = sqlite3.connect('Database/prod_database.db') # Database/prod_database.db
    cursor = conn.cursor()

    data = ('''SELECT * FROM detach WHERE index_db = ?''')

    cursor.execute(data, (detachment))
    records = cursor.fetchall()

    return records


def start_new_db(detachment):
    # функция для извлечения данных из бд отделов
    dd = (date,) + detachment
    conn = sqlite3.connect('Database/prod_database.db') # Database/prod_database.db
    cursor = conn.cursor()

    data = ('''SELECT * FROM detach WHERE index_db = ?''')
    cursor.execute(data, (detachment))
    records = cursor.fetchall()

    # удаляем старое значение
    delete_row = ("""DELETE FROM detach_start_zvit WHERE index_db = ?""")
    cursor.execute(delete_row, (detachment))

    cursor.executemany('''INSERT INTO detach_start_zvit VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', records)

    update_row = ("""UPDATE detach_start_zvit SET дата = ? WHERE index_db = ?""")
    cursor.execute(update_row, (dd))

    conn.commit()


def parse_db_rozklad():
    '''
    parsing rozclad db
    '''
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    data = ('''SELECT * FROM rozklad_db''')
    cursor.execute(data)
    records = cursor.fetchall()
    return records


def clear_rozclad_db():
    '''
    func for clear old values of rozclad_db
    '''
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rozklad_db ;")
    conn.commit()


def parse_day_rozklad(day):
    day = day
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    data = ('''SELECT * FROM rozklad_db WHERE день_тижн = ?''')
    cursor.execute(data, (day))
    records = cursor.fetchall()
    return records

def parse_day_dinner_rozklad(day):
    day = day
    dinner = ('Обід',)
    dd = day+dinner
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    data = ('''SELECT * FROM rozklad_db WHERE день_тижн = ? AND прийом = ?''')
    cursor.execute(data, (dd))
    records = cursor.fetchall()
    return records



def add_n_to_db(signal, number_ch, index_ch, person, date_op, val_ch):
    '''
    func for insert loss, menu-loss or profit(signal flag) values
    calcuating sum old and new values
    insert new (sum) values
    delete old values
    '''
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()

    signal = signal
    number_ch = number_ch
    index_ch = index_ch
    val_ch = val_ch
    person = person
    date_op = date_op

    almount = number_ch + index_ch + person + date_op + val_ch

    val = []
    val.append(almount)

    temp_tuple = ()
    for i in val_ch:
        n = i - (i * 2)
        n = (n,)
        temp_tuple = temp_tuple + n
    almount_scnd = number_ch + index_ch + person + date_op + temp_tuple

    val_scnd = []
    val_scnd.append(almount_scnd)

    cursor.executemany(
        "INSERT INTO detach_menu_loss VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                val)

    old_data_dtch = ('''SELECT * FROM detach WHERE index_db = ?''')
    cursor.execute(old_data_dtch, (index_ch))
    records_dtch = cursor.fetchall()

    cursor.executemany(
        "INSERT INTO detach_temp VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                records_dtch)

    cursor.executemany(
        "INSERT INTO detach_temp VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                val_scnd)

    number = ('''SELECT name_db FROM detach_temp''')
    cursor.execute(number)
    number = cursor.fetchall()
    number = number[0]

    index = ('''SELECT index_db FROM detach_temp''')
    cursor.execute(index)
    index = cursor.fetchall()
    index = index[0]

    person = ('''SELECT person FROM detach_temp''')
    cursor.execute(person)
    person = cursor.fetchall()
    person = person[0]

    date_opn = ('''SELECT дата FROM detach_temp''')
    cursor.execute(date_opn)
    date_opn = cursor.fetchall()
    date_opn = date_opn[0]

    amount_sum = number + index + person + date_opn  #

    data_db = ('''pragma table_info(detach_temp); ''')
    cursor.execute(data_db)
    names_column_db = cursor.fetchall()

    for i in names_column_db[4::]:
        name_column = i[1]
        sum_var = ('''SELECT sum(''' + name_column + ''') FROM detach_temp''')
        cursor.execute(sum_var)
        final_var = cursor.fetchall()
        final_var = final_var[0]
        amount_sum = amount_sum + final_var

    val_sum_dtch = []
    val_sum_dtch.append(amount_sum)

    # удаляем старое значение
    delete_row = ("""DELETE FROM detach WHERE index_db = ?""")
    cursor.execute(delete_row, (index_ch))
    conn.commit()

    cursor.executemany(
        "INSERT INTO detach VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val_sum_dtch)

    cursor.execute('DELETE FROM detach_temp ;')
    conn.commit()


################################


def parse_db():
    '''
    parsing main file
    '''
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    data = ('''SELECT * FROM main_file''')
    cursor.execute(data)
    records = cursor.fetchall()
    cursor.close()
    return records




def parse_menu_loss_db(day1, day2):
    day1 = day1
    day2 = day2
    dd = day1+day2
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    data = ('''SELECT * FROM menu_loss WHERE дата BETWEEN ? AND ?''')
    cursor.execute(data, (dd))
    records = cursor.fetchall()
    return records

def parse_bread_baking_db(signal_b, day1, day2):
    signal_b = signal_b
    day1 = day1
    day2 = day2
    dd = day1+day2
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    if signal_b == 1:
        data = ('''SELECT * FROM bread_baking WHERE дата BETWEEN ? AND ?''')
        cursor.execute(data, (dd))

    elif signal_b == 2:
        data = ('''SELECT * FROM bread_baking WHERE rowid>0 ORDER BY rowid DESC LIMIT 1''')
        cursor.execute(data)
    records = cursor.fetchall()
    cursor.close()
    return records

def parse_loss_profit_db(signal, day1, day2):
    signal = signal
    day1 = day1
    day2 = day2
    dd = day1+day2
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    if signal == 1:
        data = ('''SELECT * FROM profit WHERE дата BETWEEN ? AND ?''')
        cursor.execute(data, (dd))
    elif signal == 2:
        data = ('''SELECT * FROM loss WHERE дата BETWEEN ? AND ?''')
        cursor.execute(data, (dd))
    records = cursor.fetchall()
    return records


def parse_db_detach():
    # функция для извлечения данных из бд отделов
    conn = sqlite3.connect('Database/prod_database.db') # Database/prod_database.db
    cursor = conn.cursor()

    data = ('''SELECT * FROM detach''')

    cursor.execute(data)
    records = cursor.fetchall()

    #print(records)
    return records


def parse_db_names_detach():
    # функция для извлечения данных из бд отделов и формирования словаря где ключ - имя, значения - индекс отд
    conn = sqlite3.connect('Database/prod_database.db')
    cursor = conn.cursor()

    data = ('''SELECT * FROM detach''')

    cursor.execute(data)
    records = cursor.fetchall()
    names_index = {}

    for i in records:
        name = i[0]
        index = i[1]
        pair = (name,) + (index,)
        names_index.update([pair])

    return names_index

# functions for record in database
def add_detachments(data):
    # функция добавления записей в бд
    conn = sqlite3.connect('Database/prod_database.db')
    cursor = conn.cursor()

    cursor.executemany('''INSERT INTO detach VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)

    conn.commit()




def add_values_to_rozclad_db(val_roz):
    val_roz = val_roz
    val = []
    val.append(val_roz)
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO rozklad_db VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        val)
    conn.commit()


def add_bread_baking(date_op, val_chs):
    date_op = date_op
    val_chs = val_chs
    almount1 = date_op+val_chs
    val = []
    val.append(almount1)
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO bread_baking VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", val)

    conn.commit()

# functions for delete from databases



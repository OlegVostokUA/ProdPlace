import sqlite3
import pandas as pd
import time


names_production = ('Назва підрозділу', 'Дата', 'Хліб', 'М’ясо яловичина, свинина(тущі, напівтущі, чверть)',
                    'М’ясні блоки яловичина, свинина', 'М’ясо птиці', 'Сосиски, сардельки', 'Печінка',
                   'Консерви м’ясні', 'Консерви м’ясорослинні', 'Риба заморожена (Хек)', 'Риба заморожена (Сайда)',
                    'Риба заморожена (Минтай)', 'Оселедець', 'Риба копчена, вялена', 'Консерви рибні', 'Сало зі спеціями',
                    'Сало-шпик солене', 'Мед', 'Джем', 'Масло вершкове', 'Олія', 'Маргарин', 'Сир', 'Цукор', 'Яйце',
                   'Рис', 'Гречана', 'Пшоно', 'Горох', 'Ячнева', 'Перлова', 'Пшенична', 'Кукурудзяна', 'Булгур',
                   'Макаронні вироби', 'Борошно пшен І гат.', 'Чай', 'Сіль', 'Перець', 'Лавр. лист', 'Гірч. порошок',
                   'Оцет', 'Томат паста', 'Сухофрукти', 'Соки плодово-ягідні', 'Фрукти свіжі', 'Картопля', 'Капуста свіжа',
                   'Капуста маринована', 'Капуста конс.', 'Морква свіжа', 'Морква конс.', 'Буряк свіжий', 'Буряк конс.',
                   'Цибуля ріпчаста', 'Цибуля (перо)', 'Огірки свіжі', 'Огірки марин.', 'Огірки конс.',
                   'Консервований горошок', 'Консервована кукурудза', 'Консервована квасоля', 'Салати овочеві', 'Дріжджі',
                    'Вода питна бутильована', 'Гексавіт', 'Молоко сухе', 'Печиво',
                   'ПНСП (норма 10)', 'ПНСП (норма 15)', 'Корм для сл. собак', 'Миючий засіб')
number_zag = (1111,)
date = ('11.11.22',)
val_zag = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def conn_db():
    """
    func for connection to database and create tables
    """
    sqlite_connection = sqlite3.connect('prod_database.db')
    print("База данных подключена к SQLite")

    sqlite_create_table_query1 = '''CREATE TABLE IF NOT EXISTS names_prod (index_db TEXT, дата TEXT, хліб TEXT, ялов_свин_туші TEXT, ялов_свин_блоки TEXT, мясо_птиці TEXT, сардельки TEXT, печінка TEXT, конс_мясні TEXT, конс_мясорослинні TEXT, риба_замор_Хек TEXT, риба_замор_Сайда TEXT, риба_замор_Минтай TEXT, оселедець TEXT, риба_копчена TEXT, конс_рибні TEXT, сало_зі_спец TEXT, сало_солене TEXT, мед TEXT, джем TEXT, масло TEXT, олія TEXT, маргарин TEXT, сир_тв TEXT, цукор TEXT, яйце TEXT, рис TEXT, гречана TEXT, пшоно TEXT, горох TEXT, ячмінна TEXT, перлова TEXT, пшенична TEXT, кукурудзяна TEXT, булгур TEXT, макаронні_вироби TEXT, борошно TEXT, чай TEXT, сіль TEXT, перець TEXT, лавр_лист TEXT, гірч_порошок TEXT, оцет TEXT, томат_паста TEXT, фрукти_сушені TEXT, соки_фруктові TEXT, фрукти_свіжі TEXT, картопля TEXT, капуста_св TEXT, капуста_кв TEXT, капуста_конс TEXT, морква_св TEXT, морква_конс TEXT, буряк_св TEXT, буряк_конс TEXT, цибуля_ріпчаста TEXT, цибуля_перо TEXT, огірки_св TEXT, огірки_мар TEXT, огірки_конс TEXT, горошок TEXT, кукурудза_конс TEXT, квасоля_конс TEXT, салати_овочеві TEXT, дріжджі TEXT, вода_питн_бут TEXT, гексавіт TEXT, молоко_сухе TEXT, печиво TEXT, ПНСП TEXT, ДПНП TEXT, сухий_корм TEXT, миючий_засіб_рідкий TEXT)'''
    print("Таблица names_prod создана")
    sqlite_create_table_query2 = '''CREATE TABLE IF NOT EXISTS main_file (index_db INT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица main_file создана")
    sqlite_create_table_query3 = '''CREATE TABLE IF NOT EXISTS profit (index_db INT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица profit создана")
    sqlite_create_table_query4 = '''CREATE TABLE IF NOT EXISTS loss (index_db INT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица loss создана")
    sqlite_create_table_query5 = '''CREATE TABLE IF NOT EXISTS menu_loss (index_db INT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица menu_loss создана")
    sqlite_create_table_query6 = '''CREATE TABLE IF NOT EXISTS rozklad_db (день_тижн TEXT, прийом TEXT, страва TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица rozklad_db создана")
    sqlite_create_table_query7 = '''CREATE TABLE IF NOT EXISTS bread_baking (дата TEXT, витр_бор DECIMAL, хліб DECIMAL, вих_план DECIMAL, вих_факт DECIMAL, олія_н_кг DECIMAL, олія_н_п DECIMAL, олія_ф_кг DECIMAL, олія_ф_п DECIMAL, сіль_н_кг DECIMAL, сіль_н_п DECIMAL, сіль_ф_кг DECIMAL, сіль_ф_п DECIMAL, држ_н_кг DECIMAL, држ_н_п DECIMAL, држ_ф_кг DECIMAL, држ_ф_п DECIMAL)'''
    print("Таблица bread_baking создана")

    cursor = sqlite_connection.cursor()

    cursor.execute(sqlite_create_table_query1)
    cursor.execute(sqlite_create_table_query2)
    cursor.execute(sqlite_create_table_query3)
    cursor.execute(sqlite_create_table_query4)
    cursor.execute(sqlite_create_table_query5)
    cursor.execute(sqlite_create_table_query6)
    cursor.execute(sqlite_create_table_query7)
    # cursor.execute(sqlite_create_table_query8)

    sqlite_connection.commit()

    cursor.close()


# functions for felling database default values
def add_names_to_db_names(names_production):
    '''
    table for save  human-readable names products
    '''
    names_production = names_production
    val = []
    val.append(names_production)
    conn = sqlite3.connect("prod_database.db")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO names_prod VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        val)
    conn.commit()


def add_n_to_db_main(number_zag, date, val_zag):
    number_zag = number_zag
    date = date
    val_zag = val_zag
    almount1 = number_zag + date + val_zag
    val = []
    val.append(almount1)
    conn = sqlite3.connect("prod_database.db")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        val)
    conn.commit()

# conn_db()
# add_names_to_db_names(names_production)
# add_n_to_db_main(number_zag, date, val_zag)

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

def parse_menu_loss_db(day1, day2):
    day1 = day1
    day2 = day2
    dd = day1+day2
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    data = ('''SELECT * FROM menu_loss WHERE дата BETWEEN ? AND ?''') #BETWEEN LIKE = ? AND LIKE = ? ORDER BY dateRec
    cursor.execute(data, (dd))
    records = cursor.fetchall()
    return records

def parse_bread_baking_db(signal_b):
    signal_b = signal_b
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    if signal_b == 1:
        data = ('''SELECT * FROM bread_baking''')
        cursor.execute(data)
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
        data = ('''SELECT * FROM profit WHERE дата BETWEEN ? AND ?''') #BETWEEN LIKE = ? AND LIKE = ? ORDER BY dateRec
        cursor.execute(data, (dd))
    elif signal == 2:
        data = ('''SELECT * FROM loss WHERE дата BETWEEN ? AND ?''') #BETWEEN LIKE = ? AND LIKE = ? ORDER BY dateRec
        cursor.execute(data, (dd))
    records = cursor.fetchall()
    return records

# functions for record in database
def add_n_to_db(signal, number_ch, date_op, val_ch):
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
    val_ch = val_ch
    date_op = date_op
    almount = number_ch + date_op + val_ch
    val = []
    val.append(almount)

    if signal == 1:
        cursor.executemany(
            "INSERT INTO profit VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val)
        cursor.executemany(
            "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val)
    elif signal == 2 or 3:
        temp_tuple = ()
        for i in val_ch:
            n = i - (i * 2)
            n = (n,)
            temp_tuple = temp_tuple + n
        almount_scnd = number_ch + date_op + temp_tuple
        val_scnd = []
        val_scnd.append(almount_scnd)
        cursor.executemany(
            "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val_scnd)

    conn.commit()

    number = ('''SELECT index_db FROM main_file''')
    cursor.execute(number)
    number = cursor.fetchall()
    number = number[0]

    date_opn = ('''SELECT дата FROM main_file''')
    cursor.execute(date_opn)
    date_opn = cursor.fetchall()
    date_opn = date_opn[0]

    bread = ('''SELECT sum(хліб) FROM main_file''')
    cursor.execute(bread)
    bread = cursor.fetchall()
    bread = bread[0]

    meet_carc = ('''SELECT sum(ялов_свин_туші) FROM main_file''')
    cursor.execute(meet_carc)
    meet_carc = cursor.fetchall()
    meet_carc = meet_carc[0]

    meat_blocks = ('''SELECT sum(ялов_свин_блоки) FROM main_file''')
    cursor.execute(meat_blocks)
    meat_blocks = cursor.fetchall()
    meat_blocks = meat_blocks[0]

    meat_chicken = ('''SELECT sum(мясо_птиці) FROM main_file''')
    cursor.execute(meat_chicken)
    meat_chicken = cursor.fetchall()
    meat_chicken = meat_chicken[0]

    sausage = ('''SELECT sum(сардельки) FROM main_file''')
    cursor.execute(sausage)
    sausage = cursor.fetchall()
    sausage = sausage[0]

    liver = ('''SELECT sum(печінка) FROM main_file''')
    cursor.execute(liver)
    liver = cursor.fetchall()
    liver = liver[0]

    cons_meat = ('''SELECT sum(конс_мясні) FROM main_file''')
    cursor.execute(cons_meat)
    cons_meat = cursor.fetchall()
    cons_meat = cons_meat[0]

    cons_meat_veg = ('''SELECT sum(конс_мясорослинні) FROM main_file''')
    cursor.execute(cons_meat_veg)
    cons_meat_veg = cursor.fetchall()
    cons_meat_veg = cons_meat_veg[0]

    fish_hake = ('''SELECT sum(риба_замор_Хек) FROM main_file''')
    cursor.execute(fish_hake)
    fish_hake = cursor.fetchall()
    fish_hake = fish_hake[0]

    fish_pike = ('''SELECT sum(риба_замор_Сайда) FROM main_file''')
    cursor.execute(fish_pike)
    fish_pike = cursor.fetchall()
    fish_pike = fish_pike[0]

    fish_pollock = ('''SELECT sum(риба_замор_Минтай) FROM main_file''')
    cursor.execute(fish_pollock)
    fish_pollock = cursor.fetchall()
    fish_pollock = fish_pollock[0]

    herring = ('''SELECT sum(оселедець) FROM main_file''')
    cursor.execute(herring)
    herring = cursor.fetchall()
    herring = herring[0]

    fish_smoked = ('''SELECT sum(риба_копчена) FROM main_file''')
    cursor.execute(fish_smoked)
    fish_smoked = cursor.fetchall()
    fish_smoked = fish_smoked[0]

    cons_fish = ('''SELECT sum(конс_рибні) FROM main_file''')
    cursor.execute(cons_fish)
    cons_fish = cursor.fetchall()
    cons_fish = cons_fish[0]

    fat_pepper = ('''SELECT sum(сало_зі_спец) FROM main_file''')
    cursor.execute(fat_pepper)
    fat_pepper = cursor.fetchall()
    fat_pepper = fat_pepper[0]

    fat_salt = ('''SELECT sum(сало_солене) FROM main_file''')
    cursor.execute(fat_salt)
    fat_salt = cursor.fetchall()
    fat_salt = fat_salt[0]

    honey = ('''SELECT sum(мед) FROM main_file''')
    cursor.execute(honey)
    honey = cursor.fetchall()
    honey = honey[0]

    jam = ('''SELECT sum(джем) FROM main_file''')
    cursor.execute(jam)
    jam = cursor.fetchall()
    jam = jam[0]

    butter = ('''SELECT sum(масло) FROM main_file''')
    cursor.execute(butter)
    butter = cursor.fetchall()
    butter = butter[0]

    oil = ('''SELECT sum(олія) FROM main_file''')
    cursor.execute(oil)
    oil = cursor.fetchall()
    oil = oil[0]

    marg_fat = ('''SELECT sum(маргарин) FROM main_file''')
    cursor.execute(marg_fat)
    marg_fat = cursor.fetchall()
    marg_fat = marg_fat[0]

    cheese = ('''SELECT sum(сир_тв) FROM main_file''')
    cursor.execute(cheese)
    cheese = cursor.fetchall()
    cheese = cheese[0]

    sugar = ('''SELECT sum(цукор) FROM main_file''')
    cursor.execute(sugar)
    sugar = cursor.fetchall()
    sugar = sugar[0]

    egg = ('''SELECT sum(яйце) FROM main_file''')
    cursor.execute(egg)
    egg = cursor.fetchall()
    egg = egg[0]

    rice = ('''SELECT sum(рис) FROM main_file''')
    cursor.execute(rice)
    rice = cursor.fetchall()
    rice = rice[0]

    buckwheat = ('''SELECT sum(гречана) FROM main_file''')
    cursor.execute(buckwheat)
    buckwheat = cursor.fetchall()
    buckwheat = buckwheat[0]

    millet = ('''SELECT sum(пшоно) FROM main_file''')
    cursor.execute(millet)
    millet = cursor.fetchall()
    millet = millet[0]

    pears = ('''SELECT sum(горох) FROM main_file''')
    cursor.execute(pears)
    pears = cursor.fetchall()
    pears = pears[0]

    barley = ('''SELECT sum(ячмінна) FROM main_file''')
    cursor.execute(barley)
    barley = cursor.fetchall()
    barley = barley[0]

    pearl = ('''SELECT sum(перлова) FROM main_file''')
    cursor.execute(pearl)
    pearl = cursor.fetchall()
    pearl = pearl[0]

    wheat = ('''SELECT sum(пшенична) FROM main_file''')
    cursor.execute(wheat)
    wheat = cursor.fetchall()
    wheat = wheat[0]

    corn = ('''SELECT sum(кукурудзяна) FROM main_file''')
    cursor.execute(corn)
    corn = cursor.fetchall()
    corn = corn[0]

    bulgur = ('''SELECT sum(булгур) FROM main_file''')
    cursor.execute(bulgur)
    bulgur = cursor.fetchall()
    bulgur = bulgur[0]

    pasta = ('''SELECT sum(макаронні_вироби) FROM main_file''')
    cursor.execute(pasta)
    pasta = cursor.fetchall()
    pasta = pasta[0]

    wheat_fl_first = ('''SELECT sum(борошно) FROM main_file''')
    cursor.execute(wheat_fl_first)
    wheat_fl_first = cursor.fetchall()
    wheat_fl_first = wheat_fl_first[0]

    tea = ('''SELECT sum(чай) FROM main_file''')
    cursor.execute(tea)
    tea = cursor.fetchall()
    tea = tea[0]

    salt = ('''SELECT sum(сіль) FROM main_file''')
    cursor.execute(salt)
    salt = cursor.fetchall()
    salt = salt[0]

    pepper = ('''SELECT sum(перець) FROM main_file''')
    cursor.execute(pepper)
    pepper = cursor.fetchall()
    pepper = pepper[0]

    l_list = ('''SELECT sum(лавр_лист) FROM main_file''')
    cursor.execute(l_list)
    l_list = cursor.fetchall()
    l_list = l_list[0]

    g_porokh = ('''SELECT sum(гірч_порошок) FROM main_file''')
    cursor.execute(g_porokh)
    g_porokh = cursor.fetchall()
    g_porokh = g_porokh[0]

    vinegar = ('''SELECT sum(оцет) FROM main_file''')
    cursor.execute(vinegar)
    vinegar = cursor.fetchall()
    vinegar = vinegar[0]

    tomat_pasta = ('''SELECT sum(томат_паста) FROM main_file''')
    cursor.execute(tomat_pasta)
    tomat_pasta = cursor.fetchall()
    tomat_pasta = tomat_pasta[0]

    dried_fruits = ('''SELECT sum(фрукти_сушені) FROM main_file''')
    cursor.execute(dried_fruits)
    dried_fruits = cursor.fetchall()
    dried_fruits = dried_fruits[0]

    juice = ('''SELECT sum(соки_фруктові) FROM main_file''')
    cursor.execute(juice)
    juice = cursor.fetchall()
    juice = juice[0]

    fresh_fruits = ('''SELECT sum(фрукти_свіжі) FROM main_file''')
    cursor.execute(fresh_fruits)
    fresh_fruits = cursor.fetchall()
    fresh_fruits = fresh_fruits[0]

    potato = ('''SELECT sum(картопля) FROM main_file''')
    cursor.execute(potato)
    potato = cursor.fetchall()
    potato = potato[0]

    cabbage_fr = ('''SELECT sum(капуста_св) FROM main_file''')
    cursor.execute(cabbage_fr)
    cabbage_fr = cursor.fetchall()
    cabbage_fr = cabbage_fr[0]

    cabbage_ferm = ('''SELECT sum(капуста_кв) FROM main_file''')
    cursor.execute(cabbage_ferm)
    cabbage_ferm = cursor.fetchall()
    cabbage_ferm = cabbage_ferm[0]

    cabbage_cons = ('''SELECT sum(капуста_конс) FROM main_file''')
    cursor.execute(cabbage_cons)
    cabbage_cons = cursor.fetchall()
    cabbage_cons = cabbage_cons[0]

    carrot_fr = ('''SELECT sum(морква_св) FROM main_file''')
    cursor.execute(carrot_fr)
    carrot_fr = cursor.fetchall()
    carrot_fr = carrot_fr[0]

    carrot_cons = ('''SELECT sum(морква_конс) FROM main_file''')
    cursor.execute(carrot_cons)
    carrot_cons = cursor.fetchall()
    carrot_cons = carrot_cons[0]

    beet_fr = ('''SELECT sum(буряк_св) FROM main_file''')
    cursor.execute(beet_fr)
    beet_fr = cursor.fetchall()
    beet_fr = beet_fr[0]

    beet_cons = ('''SELECT sum(буряк_конс) FROM main_file''')
    cursor.execute(beet_cons)
    beet_cons = cursor.fetchall()
    beet_cons = beet_cons[0]

    onion_on = ('''SELECT sum(цибуля_ріпчаста) FROM main_file''')
    cursor.execute(onion_on)
    onion_on = cursor.fetchall()
    onion_on = onion_on[0]

    onion_fr = ('''SELECT sum(цибуля_перо) FROM main_file''')
    cursor.execute(onion_fr)
    onion_fr = cursor.fetchall()
    onion_fr = onion_fr[0]

    cucumbers_fr = ('''SELECT sum(огірки_св) FROM main_file''')
    cursor.execute(cucumbers_fr)
    cucumbers_fr = cursor.fetchall()
    cucumbers_fr = cucumbers_fr[0]

    cucumbers_ferm = ('''SELECT sum(огірки_мар) FROM main_file''')
    cursor.execute(cucumbers_ferm)
    cucumbers_ferm = cursor.fetchall()
    cucumbers_ferm = cucumbers_ferm[0]

    cucumbers_cons = ('''SELECT sum(огірки_конс) FROM main_file''')
    cursor.execute(cucumbers_cons)
    cucumbers_cons = cursor.fetchall()
    cucumbers_cons = cucumbers_cons[0]

    cons_peas = ('''SELECT sum(горошок) FROM main_file''')
    cursor.execute(cons_peas)
    cons_peas = cursor.fetchall()
    cons_peas = cons_peas[0]

    cons_corn = ('''SELECT sum(кукурудза_конс) FROM main_file''')
    cursor.execute(cons_corn)
    cons_corn = cursor.fetchall()
    cons_corn = cons_corn[0]

    cons_beans = ('''SELECT sum(квасоля_конс) FROM main_file''')
    cursor.execute(cons_beans)
    cons_beans = cursor.fetchall()
    cons_beans = cons_beans[0]

    veg_salads = ('''SELECT sum(салати_овочеві) FROM main_file''')
    cursor.execute(veg_salads)
    veg_salads = cursor.fetchall()
    veg_salads = veg_salads[0]

    yeast = ('''SELECT sum(дріжджі) FROM main_file''')
    cursor.execute(yeast)
    yeast = cursor.fetchall()
    yeast = yeast[0]

    water = ('''SELECT sum(вода_питн_бут) FROM main_file''')
    cursor.execute(water)
    water = cursor.fetchall()
    water = water[0]

    gecsav = ('''SELECT sum(гексавіт) FROM main_file''')
    cursor.execute(gecsav)
    gecsav = cursor.fetchall()
    gecsav = gecsav[0]

    dry_milk = ('''SELECT sum(молоко_сухе) FROM main_file''')
    cursor.execute(dry_milk)
    dry_milk = cursor.fetchall()
    dry_milk = dry_milk[0]

    biscuit = ('''SELECT sum(печиво) FROM main_file''')
    cursor.execute(biscuit)
    biscuit = cursor.fetchall()
    biscuit = biscuit[0]

    DSP_10 = ('''SELECT sum(ПНСП) FROM main_file''')
    cursor.execute(DSP_10)
    DSP_10 = cursor.fetchall()
    DSP_10 = DSP_10[0]

    DSP_15 = ('''SELECT sum(ДПНП) FROM main_file''')
    cursor.execute(DSP_15)
    DSP_15 = cursor.fetchall()
    DSP_15 = DSP_15[0]

    dog_food = ('''SELECT sum(сухий_корм) FROM main_file''')
    cursor.execute(dog_food)
    dog_food = cursor.fetchall()
    dog_food = dog_food[0]

    detergent = ('''SELECT sum(миючий_засіб_рідкий) FROM main_file''')
    cursor.execute(detergent)
    detergent = cursor.fetchall()
    detergent = detergent[0]

    amount_sum = number + date_opn + bread + meet_carc + meat_blocks + meat_chicken + sausage + liver + cons_meat + cons_meat_veg + fish_hake + fish_pike + fish_pollock + herring + fish_smoked + cons_fish + fat_pepper + fat_salt + honey + jam + butter + oil + marg_fat + cheese + sugar + egg + rice + buckwheat + millet + pears + barley + pearl + wheat + corn + bulgur + pasta + wheat_fl_first + tea + salt + pepper + l_list + g_porokh + vinegar + tomat_pasta + dried_fruits + juice + fresh_fruits + potato + cabbage_fr + cabbage_ferm + cabbage_cons + carrot_fr + carrot_cons + beet_fr + beet_cons + onion_on + onion_fr + cucumbers_fr + cucumbers_ferm + cucumbers_cons + cons_peas + cons_corn + cons_beans + veg_salads + yeast + water + gecsav + dry_milk + biscuit + DSP_10 + DSP_15 + dog_food + detergent
    val_sum = []
    val_sum.append(amount_sum)

    cursor.executemany(
        "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        val_sum)

    if signal == 2:
        cursor.executemany(
            "INSERT INTO loss VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val)
    elif signal == 3:
        cursor.executemany(
            "INSERT INTO menu_loss VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val)

    conn.commit()

    row = ("""SELECT rowid FROM main_file WHERE rowid>0 ORDER BY rowid LIMIT 2""")
    cursor.execute(row)
    rows = cursor.fetchall()
    row1 = rows[0]
    row2 = rows[1]
    delete_row = ("""DELETE FROM main_file WHERE rowid = ?""")
    cursor.execute(delete_row, (row1))
    conn.commit()
    delete_row = ("""DELETE FROM main_file WHERE rowid = ?""")
    cursor.execute(delete_row, (row2))
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

def clear_rozclad_db():
    '''
    func for clear old values of rozclad_db
    '''
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rozklad_db ;")
    conn.commit()
    print('deleted')

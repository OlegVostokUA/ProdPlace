import sqlite3

names_production = ('Назва підрозділу', 'Індекс підрозділу', 'ОС', 'Дата', 'Хліб', 'М’ясо яловичина, свинина(тущі, напівтущі, чверть)',
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
index_zag = (1111,)
date = ('11.11.22',)
person = ('pers',)
val_zag = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def conn_db():
    """
    func for connection to database and create tables
    """
    sqlite_connection = sqlite3.connect('../Database/prod_database.db')
    print("База данных подключена к SQLite")

    sqlite_create_table_query1 = '''CREATE TABLE IF NOT EXISTS names_prod (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб TEXT, ялов_свин_туші TEXT, ялов_свин_блоки TEXT, мясо_птиці TEXT, сардельки TEXT, печінка TEXT, конс_мясні TEXT, конс_мясорослинні TEXT, риба_замор_Хек TEXT, риба_замор_Сайда TEXT, риба_замор_Минтай TEXT, оселедець TEXT, риба_копчена TEXT, конс_рибні TEXT, сало_зі_спец TEXT, сало_солене TEXT, мед TEXT, джем TEXT, масло TEXT, олія TEXT, маргарин TEXT, сир_тв TEXT, цукор TEXT, яйце TEXT, рис TEXT, гречана TEXT, пшоно TEXT, горох TEXT, ячмінна TEXT, перлова TEXT, пшенична TEXT, кукурудзяна TEXT, булгур TEXT, макаронні_вироби TEXT, борошно TEXT, чай TEXT, сіль TEXT, перець TEXT, лавр_лист TEXT, гірч_порошок TEXT, оцет TEXT, томат_паста TEXT, фрукти_сушені TEXT, соки_фруктові TEXT, фрукти_свіжі TEXT, картопля TEXT, капуста_св TEXT, капуста_кв TEXT, капуста_конс TEXT, морква_св TEXT, морква_конс TEXT, буряк_св TEXT, буряк_конс TEXT, цибуля_ріпчаста TEXT, цибуля_перо TEXT, огірки_св TEXT, огірки_мар TEXT, огірки_конс TEXT, горошок TEXT, кукурудза_конс TEXT, квасоля_конс TEXT, салати_овочеві TEXT, дріжджі TEXT, вода_питн_бут TEXT, гексавіт TEXT, молоко_сухе TEXT, печиво TEXT, ПНСП TEXT, ДПНП TEXT, сухий_корм TEXT, миючий_засіб_рідкий TEXT)'''
    print("Таблица names_prod создана")
    sqlite_create_table_query2 = '''CREATE TABLE IF NOT EXISTS main_file (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица main_file создана")
    sqlite_create_table_query3 = '''CREATE TABLE IF NOT EXISTS profit (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица profit создана")
    sqlite_create_table_query4 = '''CREATE TABLE IF NOT EXISTS loss (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица loss создана")
    sqlite_create_table_query5 = '''CREATE TABLE IF NOT EXISTS menu_loss (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица menu_loss создана")
    sqlite_create_table_query6 = '''CREATE TABLE IF NOT EXISTS rozklad_db (день_тижн TEXT, прийом TEXT, страва TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица rozklad_db создана")
    sqlite_create_table_query7 = '''CREATE TABLE IF NOT EXISTS bread_baking (дата TEXT, витр_бор DECIMAL, хліб DECIMAL, вих_план DECIMAL, вих_факт DECIMAL, олія_н_кг DECIMAL, олія_н_п DECIMAL, олія_ф_кг DECIMAL, олія_ф_п DECIMAL, сіль_н_кг DECIMAL, сіль_н_п DECIMAL, сіль_ф_кг DECIMAL, сіль_ф_п DECIMAL, држ_н_кг DECIMAL, држ_н_п DECIMAL, држ_ф_кг DECIMAL, држ_ф_п DECIMAL)'''
    print("Таблица bread_baking создана")

    sqlite_create_table_query8 = '''CREATE TABLE IF NOT EXISTS detach (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица detach создана")
    sqlite_create_table_query9 = '''CREATE TABLE IF NOT EXISTS detach_loss (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица detach_loss создана")
    sqlite_create_table_query10 = '''CREATE TABLE IF NOT EXISTS detach_profit (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица detach_profit создана")
    sqlite_create_table_query11 = '''CREATE TABLE IF NOT EXISTS detach_temp (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица detach_temp создана")
    sqlite_create_table_query12 = '''CREATE TABLE IF NOT EXISTS detach_start_zvit (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица detach_start_zvit создана")
    sqlite_create_table_query13 = '''CREATE TABLE IF NOT EXISTS detach_menu_loss (name_db TEXT, index_db TEXT, person TEXT, дата TEXT, хліб DECIMAL, ялов_свин_туші DECIMAL, ялов_свин_блоки DECIMAL, мясо_птиці DECIMAL, сардельки DECIMAL, печінка DECIMAL, конс_мясні DECIMAL, конс_мясорослинні DECIMAL, риба_замор_Хек DECIMAL, риба_замор_Сайда DECIMAL, риба_замор_Минтай DECIMAL, оселедець DECIMAL, риба_копчена DECIMAL, конс_рибні DECIMAL, сало_зі_спец DECIMAL, сало_солене DECIMAL, мед DECIMAL, джем DECIMAL, масло DECIMAL, олія DECIMAL, маргарин DECIMAL, сир_тв DECIMAL, цукор DECIMAL, яйце DECIMAL, рис DECIMAL, гречана DECIMAL, пшоно DECIMAL, горох DECIMAL, ячмінна DECIMAL, перлова DECIMAL, пшенична DECIMAL, кукурудзяна DECIMAL, булгур DECIMAL, макаронні_вироби DECIMAL, борошно DECIMAL, чай DECIMAL, сіль DECIMAL, перець DECIMAL, лавр_лист DECIMAL, гірч_порошок DECIMAL, оцет DECIMAL, томат_паста DECIMAL, фрукти_сушені DECIMAL, соки_фруктові DECIMAL, фрукти_свіжі DECIMAL, картопля DECIMAL, капуста_св DECIMAL, капуста_кв DECIMAL, капуста_конс DECIMAL, морква_св DECIMAL, морква_конс DECIMAL, буряк_св DECIMAL, буряк_конс DECIMAL, цибуля_ріпчаста DECIMAL, цибуля_перо DECIMAL, огірки_св DECIMAL, огірки_мар DECIMAL, огірки_конс DECIMAL, горошок DECIMAL, кукурудза_конс DECIMAL, квасоля_конс DECIMAL, салати_овочеві DECIMAL, дріжджі DECIMAL, вода_питн_бут DECIMAL, гексавіт DECIMAL, молоко_сухе DECIMAL, печиво DECIMAL, ПНСП DECIMAL, ДПНП DECIMAL, сухий_корм DECIMAL, миючий_засіб_рідкий DECIMAL)'''
    print("Таблица detach_menu_loss создана")
    sqlite_create_table_query14 = '''CREATE TABLE IF NOT EXISTS detach_bread_baking (index_db TEXT, дата TEXT, витр_бор DECIMAL, хліб DECIMAL, вих_план DECIMAL, вих_факт DECIMAL, олія_н_кг DECIMAL, олія_н_п DECIMAL, олія_ф_кг DECIMAL, олія_ф_п DECIMAL, сіль_н_кг DECIMAL, сіль_н_п DECIMAL, сіль_ф_кг DECIMAL, сіль_ф_п DECIMAL, држ_н_кг DECIMAL, држ_н_п DECIMAL, држ_ф_кг DECIMAL, држ_ф_п DECIMAL)'''
    print("Таблица detach_bread_baking создана")

    cursor = sqlite_connection.cursor()

    cursor.execute(sqlite_create_table_query1)
    cursor.execute(sqlite_create_table_query2)
    cursor.execute(sqlite_create_table_query3)
    cursor.execute(sqlite_create_table_query4)
    cursor.execute(sqlite_create_table_query5)
    cursor.execute(sqlite_create_table_query6)
    cursor.execute(sqlite_create_table_query7)
    cursor.execute(sqlite_create_table_query8)
    cursor.execute(sqlite_create_table_query9)
    cursor.execute(sqlite_create_table_query10)
    cursor.execute(sqlite_create_table_query11)
    cursor.execute(sqlite_create_table_query12)
    cursor.execute(sqlite_create_table_query13)
    cursor.execute(sqlite_create_table_query14)

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
    conn = sqlite3.connect("../Database/prod_database.db")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO names_prod VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        val)
    conn.commit()


def add_n_to_db_main(number_zag, index_zag, person, date, val_zag):
    number_zag = number_zag
    date = date
    index_zag = index_zag
    person = person
    val_zag = val_zag
    almount1 = number_zag + index_zag + person + date + val_zag
    val = []
    val.append(almount1)
    conn = sqlite3.connect("../Database/prod_database.db")
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        val)
    conn.commit()



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

    # if signal == 1:
    #     data = ('''SELECT * FROM profit WHERE дата BETWEEN ? AND ?''')
    #     cursor.execute(data, (dd))

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
    index = ('хліб', )
    dd = index+day1+day2
    conn = sqlite3.connect("Database/prod_database.db")
    cursor = conn.cursor()
    if signal == 1:
        data = ('''SELECT * FROM profit WHERE index_db <> ? AND дата BETWEEN ? AND ?''')
        cursor.execute(data, (dd))
    elif signal == 2:
        data = ('''SELECT * FROM loss WHERE index_db <> ? AND дата BETWEEN ? AND ?''')
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

    cursor.executemany(
        '''INSERT INTO detach VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        data)
    cursor.executemany(
        '''INSERT INTO detach_start_zvit VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        data)

    conn.commit()


def add_n_to_db(signal, number_ch, index_ch, person, date_op, val_ch): # signal, number_ch, index_ch, person, date_op, val_ch
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
    person = person
    val_ch = val_ch
    date_op = date_op

    # almount = number_ch + index_ch + date_op + val_ch
    almount = number_ch + index_ch + person + date_op + val_ch

    val = []
    val.append(almount)

    temp_tuple = ()
    for i in val_ch:
        n = i - (i * 2)
        n = (n,)
        temp_tuple = temp_tuple + n

    # almount_scnd = number_ch + index_ch + date_op + temp_tuple
    almount_scnd = number_ch + index_ch + person + date_op + temp_tuple
    val_scnd = []
    val_scnd.append(almount_scnd)

    if signal == 1 or signal == 5:
        cursor.executemany(
            "INSERT INTO profit VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val)
        cursor.executemany(
            "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val)
        if signal == 5:
            cursor.executemany(
                "INSERT INTO detach_loss VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
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

    elif signal == 2 or signal == 3 or signal == 4:

        cursor.executemany(
            "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            val_scnd)

        if signal == 2:
            cursor.executemany(
                "INSERT INTO loss VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                val)
        elif signal == 3:
            cursor.executemany(
                "INSERT INTO menu_loss VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                val)
        elif signal == 4:
            cursor.executemany(
                "INSERT INTO loss VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                val)

            cursor.executemany(
                "INSERT INTO detach_profit VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                val)

            old_data_dtch = ('''SELECT * FROM detach WHERE index_db = ?''')
            cursor.execute(old_data_dtch, (index_ch))
            records_dtch = cursor.fetchall()
            cursor.executemany(
                "INSERT INTO detach_temp VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                records_dtch)
            cursor.executemany(
                "INSERT INTO detach_temp VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                val)

    conn.commit()

    number = ('''SELECT name_db FROM main_file''')
    cursor.execute(number)
    number = cursor.fetchall()
    number = number[0]

    index = ('''SELECT index_db FROM main_file''')
    cursor.execute(index)
    index = cursor.fetchall()
    index = index[0]

    person = ('''SELECT person FROM main_file''')
    cursor.execute(person)
    person = cursor.fetchall()
    person = person[0]

    date_opn = ('''SELECT дата FROM main_file''')
    cursor.execute(date_opn)
    date_opn = cursor.fetchall()
    date_opn = date_opn[0]

    amount_sum = number + index + person + date_opn #

    data_db = ('''pragma table_info(main_file); ''')
    cursor.execute(data_db)
    names_column_db = cursor.fetchall()

    for i in names_column_db[4::]:
        name_column = i[1]
        sum_var = ('''SELECT sum('''+name_column+''') FROM main_file''')
        cursor.execute(sum_var)
        final_var = cursor.fetchall()
        final_var = final_var[0]
        amount_sum = amount_sum + final_var

    val_sum = []
    val_sum.append(amount_sum)

    cursor.executemany(
        "INSERT INTO main_file VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        val_sum)

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


    if signal == 4 or signal == 5:
        number = ('''SELECT name_db FROM detach_temp''')
        cursor.execute(number)
        number = cursor.fetchall()
        number = number[0]

        index = ('''SELECT index_db FROM detach_temp''')
        cursor.execute(index)
        index = cursor.fetchall()
        index = index[0]

        date_opn = ('''SELECT дата FROM detach_temp''')
        cursor.execute(date_opn)
        date_opn = cursor.fetchall()
        date_opn = date_opn[0]

        person = ('''SELECT person FROM detach_temp''')
        cursor.execute(person)
        person = cursor.fetchall()
        person = person[0]

        amount_sum = number + index + person + date_opn #

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


def start_database():
    conn_db()
    add_names_to_db_names(names_production)
    add_n_to_db_main(number_zag, index_zag, person, date, val_zag)

# start_database()
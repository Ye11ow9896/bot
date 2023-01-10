import sqlite3
from sqlite3 import Error

class SQLiteDB(object):
    def __init__(self):
        self.create_table = """
             CREATE TABLE IF NOT EXISTS database (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 product TEXT NOT NULL,
                 price REAL,
                 date DATE,
                 link TEXT NOT NULL
             );  
             """
        self.create_assigment = """
            INSERT INTO
                database (product, price, date, link)
            VALUES
                ('Заказ док-ов', 'Сергей', 'Дмитрий', '12.10.2021', '13.10.2012', '14.09.2052', 'Срочно сделать заказ документов, иначе уволю!')
            """

        self.select_all_assigment = "SELECT * from database"
        self.select_last_id = "SELECT * from database where id = (select max(id) from database);"
        self.search_author = """select * from database where author = ?"""
        self.search_executor = """select * from database where executor = ?"""
        self.search_date_assigment = """select * from database where date_assig = ?"""

    def create_connection(self, path):
        conn = None
        try:
            conn =  sqlite3.connect(path)
            print("Connection to data base " + str(path) + " is successful")
        except Error as e:
            print("Connection to data base " + str(path) + " failed")

        return conn

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_varible_into_table(self, product, price, date, link):
        try:
            sqlite_connection = sqlite3.connect('database.sqlite')
            cursor = sqlite_connection.cursor()
            flag_connect = True
            sqlite_insert_with_param = """INSERT INTO database
                                  (product, price, date, link)
                                  VALUES (?, ?, ?, ?);"""
            data_tuple = (product, price, date, link)
            for i in data_tuple:
                if i == '':
                    print("Одно или несколько полей не заполнены. Невозможно добавить запись")
                    sqlite_connection.close()
                    flag_connect = False
                    break
            if flag_connect == True:
                cursor.execute(sqlite_insert_with_param, data_tuple)
                sqlite_connection.commit()
                print("Переменные Python успешно вставлены в таблицу database")
                cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    def get_database_table(self, path):
        self.table = self.execute_read_query(self.create_connection(path), self.select_all_assigment)
        return self.table
    
    def get_last_id(self):
        last_id = self.execute_read_query(self.create_connection('database.sqlite'), self.select_last_id)
        return last_id
    
    def create_new_db(self, db_name):
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute(self.create_table)
        con.commit()
        cur.close()

#SQLiteDB().create_new_db('database.sqlite')
#SQLiteDB().insert_varible_into_table('Orangepi 3LTS', 2790.29, '08-01-2023', 'https://aliexpress.ru/item/1005003577312703.html?spm=a2g2w.productlist.search_results.0.79524aa6maM2Ft&sku_id=12000026945335517')




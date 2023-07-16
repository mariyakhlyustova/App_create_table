import sqlite3
import json
import os

def create_table(): 
    try:
        conn = sqlite3.connect('database.db') 
        cursor = conn.cursor()  
        cursor.execute('''
            CREATE TABLE client (
                name varchar(128),
                lastname varchar(128),
                age integer 
            )
        ''')
        print("Таблица 'client' успешно создана.")
    except sqlite3.OperationalError:
        print("Таблица 'client' уже существует.")
    conn.close()

def add_client(lst):
    try:
        conn = sqlite3.connect('database.db') 
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM client WHERE name=? AND lastname=?''', (lst[0], lst[1]))
        if cursor.fetchone():
            print("Клиент с таким именем и фамилией уже существует.")
            return
        cursor.execute('''
            INSERT INTO client (name, lastname, age)
                VALUES (?, ?, ?)
        ''', lst)
        conn.commit()
        print("Клиент успешно добавлен в таблицу.")
        conn.close()
    except sqlite3.OperationalError:
        print('Таблица не создана!')
    

def json_add_client(path):
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            d = json.load(f)
            try:
                conn = sqlite3.connect('database.db') 
                cursor = conn.cursor()
                for i in d:
                    lst = []
                    for j in i:
                        lst.append(i[j])
                    cursor.execute('''SELECT * FROM client WHERE name=? AND lastname=?''', (lst[0], lst[1]))
                    if cursor.fetchone():
                        return
                    cursor.execute('''
                        INSERT INTO client (name, lastname, age)
                        VALUES (?, ?, ?)
                    ''', lst)
                    conn.commit()
                print("Клиенты успешно добавлены в таблицу.")
                conn.close()
            except sqlite3.OperationalError:
                print('Таблица не создана!')
    except FileNotFoundError:
        print('Путь до файла указан неверно!')

def avg_client_age():
    try:
        conn = sqlite3.connect('database.db') 
        cursor = conn.cursor()
        cursor.execute('''SELECT avg(age) FROM client''')
        avg_age = round(cursor.fetchone()[0], 1)
        print(f'Средний возраст клиентов {avg_age}')
        conn.close()
    except TypeError:
        print(f'{cursor.fetchone()} таблица не заполнена!')
    except sqlite3.OperationalError:
        print('Таблица не создана!')
    

def get_client():
    try:
        conn = sqlite3.connect('database.db') 
        cursor = conn.cursor()
        cursor.execute('''SELECT name, lastname, age FROM client''')
        for row in cursor.fetchall():
            print(row)
        conn.close()
    except sqlite3.OperationalError:
        print('Таблица не создана!')
    
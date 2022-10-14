"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import hashlib
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE if exists users")
cursor.execute("""CREATE TABLE if not exists users (login text, password text)
               """)
conn.commit()


def check_pass():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    hash_res = hashlib.sha256(login.encode("utf-8") + password.encode("utf-8")).hexdigest()
    print(f"В базе данных хранится строка: {hash_res}")
    cursor.execute("INSERT INTO users VALUES(?, ?);", (login, hash_res))
    conn.commit()
    password = input("Введите пароль еще раз для проверки: ")
    cursor.execute("SELECT * FROM users where login=?;", [login])
    hash_res2 = hashlib.sha256(login.encode("utf-8") + password.encode("utf-8")).hexdigest()
    res = cursor.fetchall()
    print("Вы ввели правильный пароль." if hash_res2 == res[0][1] else "Вы ввели не правильный пароль.")


check_pass()
conn.close()

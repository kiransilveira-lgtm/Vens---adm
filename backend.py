import os
import sqlite3
from random import choice, randint, shuffle


class passwordManager:
    def __init__(self):
        os.makedirs('vens', exist_ok=True)
        connection = sqlite3.connect('vens/passwords.db')
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS passwords ('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'website TEXT,'
            'email TEXT,'
            'password TEXT)'
        )
        connection.commit()
        connection.close()

    def save_data(self, website, email, password):
        connection = sqlite3.connect('vens/passwords.db')
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO passwords (website,email,password) VALUES (?,?,?)',
            (website, email, password)
        )
        connection.commit()
        connection.close()

    def search_password(self, website):
        connection = sqlite3.connect('vens/passwords.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM passwords WHERE website=?', (website,))
        result = cursor.fetchone()
        connection.close()
        return result

    def generate_password(self):
        password = ''
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!@#$%^&*'

        for _ in range(randint(8, 12)):
            password += choice(letters)
        for _ in range(randint(3, 5)):
            password += choice(numbers)
        for _ in range(randint(3, 5)):
            password += choice(symbols)

        password_list = list(password)
        shuffle(password_list)
        password = ''.join(password_list)
        return password
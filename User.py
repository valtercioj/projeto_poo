import sqlite3
import sys

connection = sqlite3.connect('confessions.db')
cursor = connection.cursor()

# crie uma tabela para usuários com nome e senha
try:
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT
    )
    ''')
    connection.commit()
except sqlite3.OperationalError:
    pass
# crie uma classe estatica de cadastro de usuario

class User:
    @staticmethod
    def add_user(name, password):
        cursor.execute(f'SELECT id FROM users WHERE name = "{name}"')
        result = cursor.fetchone()
        if result == None:
            cursor.execute("INSERT INTO users (name,password) VALUES (?, ?)", (name, password))
            connection.commit()
            return True
        else:
            return False
    @staticmethod
    def login():
        name = input("Digite seu nome de usuario: ")
        password = input("Digite sua senha: ")
        cursor.execute("SELECT id, name FROM users WHERE name = ? AND password = ?", (name, password))
        result = cursor.fetchone()
        if result != None:
            return result
        else:
            return None
    @staticmethod
    def update_password(name):
        cursor.execute(f'SELECT id FROM users WHERE name = "{name}"')
        result = cursor.fetchone()
        if result != None:
            id = int(result[0])
            password = input("Digite a senha que deseja alterar: ")
            cursor.execute(f'UPDATE users SET password = "{password}" WHERE id = "{id}"')
            connection.commit()
            return True
        else:
            return False
    @staticmethod
    def delete_user(name):
        try:
            cursor.execute(f'DELETE FROM users WHERE name = "{name}"')
            connection.commit()
            return True
        except:
            return False
            
    @staticmethod
    def update_name(name):
        cursor.execute(f'SELECT id FROM users WHERE name = "{name}"')
        result = cursor.fetchone()
        if result != None:
            id = int(result[0])
            name1 = input("Digite o nome de usuario que deseja alterar: ")
            cursor.execute(f'UPDATE users SET name = "{name1}" WHERE id = "{id}"')
            connection.commit()
            return True
        else:
            return False       
    @staticmethod
    def list_users():
        cursor.execute("SELECT name FROM users")
        result = cursor.fetchall()
        for row in result:
            print('\n'+row[0])
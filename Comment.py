from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('confessions.db')
cursor = connection.cursor()

# crie uma classe estatica de comentarios e salve em um arquivo json

class Comment:
    @staticmethod
    def add_comment(user_id):
        cursor.execute('''
            SELECT id, title, comment FROM confessions
        ''')
        for row in cursor.fetchall():
            print(row)
        try:
            id = int(input('Digite o id da confissão que deseja comentar: '))
            comment = input('Digite seu comentário: ')
            cursor.execute(f'UPDATE confessions SET comment = "{comment}" WHERE id = "{id}" AND user_id = {user_id}')
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            return False
    @staticmethod
    def remove_comment(user_id):
        cursor.execute('''
            SELECT id, comment FROM confessions
        ''')
        for row in cursor.fetchall():
            print(row)
        try:
            id = int(input('Digite o id da confissão que deseja comentar: '))
            cursor.execute(f'UPDATE confessions SET comment = "" WHERE id = {id} AND user_id = {user_id}')
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            return False

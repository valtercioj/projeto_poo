import sqlite3
import sys

connection = sqlite3.connect('confessions.db')


class Likes:
    @staticmethod
    def add_like():
        cursor = connection.cursor()
        cursor.execute('''
            SELECT id, title, likes FROM confessions
        ''')
        for row in cursor.fetchall():
            print(row)
        try:
            id = int(input('Digite o id da confissão que deseja curtir: '))
            cursor.execute(f'UPDATE confessions SET likes = likes + 1 WHERE id = {id}')
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            return False

    @staticmethod
    def remove_like():
        cursor = connection.cursor()
        cursor.execute('''
            SELECT id, title FROM confessions
        ''')
        try:
            id = int(input('Digite o id da confissão que deseja dá o deslike: '))
            cursor.execute("UPDATE confessions SET likes = likes - 1 WHERE id = ?", (id,))
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            return False

   
from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('confessions.db')
cursor = connection.cursor()


# crie uma classe estatica de reações

class Reaction:
    @staticmethod
    def add_reaction(user_id):
        cursor.execute('''
            SELECT id, title FROM confessions
        ''')
        for row in cursor.fetchall():
            print(row)
        try:
            id = int(input('Digite o id da confissão que deseja reagir: '))
            reaction = ['haha','lol','amei','triste','feliz','surpreso']
            for i in range(len(reaction)):
                print(f'{i} - {reaction[i]}')
            reaction_id = int(input('Digite o id da reação: '))
            cursor.execute(f'UPDATE confessions SET reaction = "{reaction[reaction_id]}" WHERE id = "{id}" AND user_id = {user_id}')
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            return False
    @staticmethod
    def remove_reaction(user_id):
        cursor.execute('''
            SELECT id, reaction FROM confessions
        ''')
        for row in cursor.fetchall():
            print(row)
        try:
            id = int(input('Digite o id da confissão que deseja apagar a reação: '))
            cursor.execute(f'UPDATE confessions SET reaction = "" WHERE id = {id} AND user_id = {user_id}')
            connection.commit()
            return True
        except Exception as e:
            connection.rollback()
            return False
    @staticmethod
    def list_reactions():
        cursor.execute('''
            SELECT * FROM reactions INNER JOIN confessions ON reactions.confession_id = confessions.id
        ''')
        for row in cursor.fetchall():
            print(f'''
Reação: {row[1]}
Titulo: {row[4]}
Confissão: {row[5]}
            ''')



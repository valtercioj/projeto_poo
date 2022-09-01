from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('confessions.db')
cursor = connection.cursor()

# crie uma tabela de temas relacionados a confissão
try:
    
    cursor.execute('''
    CREATE TABLE themes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        theme TEXT,
        confession_id INTEGER,
        FOREIGN KEY (confession_id) REFERENCES confessions (id)
    )
''')
    connection.commit()
except sqlite3.OperationalError:
    pass



# crie uma classe estatica de temas

class Themes:
    @staticmethod
    def add_theme(theme,user_id):
        cursor.execute(f'''
            SELECT id, title FROM confessions where id = {user_id}
        ''')
        for row in cursor.fetchall():
            print(row)
        id = int(input('Digite o id da confissão que deseja adicionar o tema: '))
        cursor.execute("INSERT INTO themes (theme, confession_id) VALUES (?, ?)", (theme, id))
        connection.commit()

    @staticmethod
    def remove_theme():
        cursor.execute('''
            SELECT id, title FROM confessions
        ''')
        id = int(input('Enter the id of the confession you want to comment: '))
        cursor.execute("UPDATE confessions SET comment = comment - 1 WHERE id = ?", (id,))
        connection.commit()


    @staticmethod
    def list_themes():
        cursor.execute('''
            SELECT * FROM themes INNER JOIN confessions ON themes.confession_id = confessions.id
        ''')
        for row in cursor.fetchall():
            print(f'''
Tema: {row[1]}
Titulo: {row[4]}
Confissão: {row[5]}
            ''')

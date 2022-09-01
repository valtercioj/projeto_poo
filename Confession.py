from multiprocessing import connection
import sqlite3
import sys

connection = sqlite3.connect('confessions.db')
cursor = connection.cursor()



class Confession:
    
    @staticmethod
    def criar_confissao(user_id):
        title = input('Título: ')
        confession = input('Confissão: ')
        anonymous = input('Você deseja salvar sua confissão como anônimo? (S/N) ')
        if anonymous == 'S' or anonymous == 's':
            anonymous = True
        else:
            anonymous = False
        like = 0
        comment = ''
        cursor.execute(f'''
            INSERT INTO confessions (title, confession, user_id, likes, comment, anonymous) VALUES (?, ?, {user_id}, {like}, ?, {anonymous})
        ''', (title, confession, comment))
        connection.commit()
        print('Confissão adicionada com sucesso!\n')

    @staticmethod
    def listar_todas_confissoes():
        cursor.execute('''
            SELECT * FROM confessions INNER JOIN users ON confessions.user_id = users.id
        ''')
        for row in cursor.fetchall():
            if row[6] == True:
                print(f'''
            Título: {row[1]}
            Confissão: {row[2]}
            qtd. likes: {row[3]}
            Comentário: {row[4]}
            Reação: {row[7]}
            Usuário respectivo: Anônimo
            \n''')
            else:
                print(f'''
            Título: {row[1]}
            Confissão: {row[2]}
            qtd. likes: {row[3]}
            Comentário: {row[4]}
            Reação: {row[7]}
            Usuário respectivo: {row[2]}
            \n''')
            print(row)
    @staticmethod
    def listar_confissoes(user_id):
        cursor.execute(f'''
            SELECT * FROM confessions WHERE user_id = {user_id}
        ''')
        for row in cursor.fetchall():
            
            print(f'''
            Título: {row[1]}
            Confissão: {row[2]}
            qtd. likes: {row[3]}
            Comentário: {row[4]}
            Reação: {row[7]}
            \n''')
        # crie um metodo estatico para listar apenas as confissões do usuário logado          
    @staticmethod
    def atualizar_confissao(user_id):
        cursor.execute(f'''
            SELECT id, confession FROM confessions WHERE user_id = {user_id}
        ''')
        for row in cursor.fetchall():
            print(row)
        try:
            id = int(input('\nDigite o id da confissão que deseja atualizar: '))
            cursor.execute(f'''
            SELECT confession FROM confessions where user_id = {user_id} AND id = {id}
            ''')
            cursor.fetchall()[0]
            cursor.execute(f'''
            UPDATE confessions SET confession = ? WHERE id = {id}
            ''', (input('Digite a nova confissão: '),))
            connection.commit()
            print('\nConfissão atualizada com sucesso!\n')

        except Exception as e:
            connection.rollback()
            print('\nErro ao atualizar confissão. Permissão negada\n')
        
       
    @staticmethod
    def deletar_confissao(user_id):
        cursor.execute('''
            SELECT id, confession FROM confessions 
        ''')
        for row in cursor.fetchall():
            print(row)
        try:
            id = int(input('\nDigite o id da confissão que deseja deletar: '))
            cursor.execute(f'''
            SELECT confession FROM confessions where user_id = {user_id} AND id = {id}
            ''')
            cursor.fetchall()[0]
            cursor.execute(f'''
            DELETE FROM confessions WHERE id = "{id}"
        ''')
            connection.commit()
            print('\nConfissão deletada com sucesso!\n')

        except Exception as e:
            connection.rollback()
            print('\nErro ao deletar confissão!\n')
    @staticmethod
    def exit():
        connection.close() 
        sys.exit()



import sqlite3
from Confession import Confession 
from Likes import Likes
from Comment import Comment
from User import User
from Themes import Themes
from Reaction import Reaction
import os
connection = sqlite3.connect('confessions.db')
cursor = connection.cursor()

try:
    cursor.execute('''
    CREATE TABLE confessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        confession TEXT,
        likes INTEGER,
        comment TEXT,
        user_id INTEGER,
        anonymous BOOLEAN,
        reaction TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')
    connection.commit()
except sqlite3.OperationalError:
    pass

logado = False



def menu_login():
    try:
        menu = int(input('''
    __   ___   ____   _____  ___  _____ _____ ____  ___   ____   _____
   /  ] /   \ |    \ |     |/  _]/ ___// ___/|    |/   \ |    \ / ___/
  /  / |     ||  _  ||   __/  [_(   \_(   \_  |  ||     ||  _  (   \_ 
 /  /  |  O  ||  |  ||  |_|    _]\__  |\__  | |  ||  O  ||  |  |\__  |
/   \_ |     ||  |  ||   _]   [_ /  \ |/  \ | |  ||     ||  |  |/  \ |
\     ||     ||  |  ||  | |     |\    |\    | |  ||     ||  |  |\    |
 \____| \___/ |__|__||__| |_____| \___| \___||____|\___/ |__|__| \___|
                                                                       
                                                          
    1- Cadastrar usuário
    2 - Login
    3 - Alterar senha
    4 - Alterar nome
    5 - Listar usuários
    6  - Deletar usuário
    99 - Sair

opção: '''))
    except ValueError:
        os.system('cls')
        print('''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       
                Opção inválida
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
\n''')
        menu_login()
    while True:
        if menu == 1:
            name = input("Digite seu nome de usuario: ")
            password = input("Digite sua senha: ")
            result = User.add_user(name, password)
            if result:
                print("Usuário cadastrado com sucesso")
            else:
                print("Usuário já existe")
        elif menu == 2:
            result = User.login()
            if result != None: 
                os.system('cls')
                menu_logado(result[0], result[1])
            else:
                os.system('cls')
                print('''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       
                Usuário ou senha inválidos
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
\n''')
                menu_login()
        elif menu == 3:
            name = input('Digite o nome do usuário: ')
            result = User.update_password(name)
            if result == True:
                os.system('cls')
                print('''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       
                Senha alterada com sucesso
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
\n''')
                menu_login()
            else:
                os.system('cls')
                print('''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       
                Usuário ou senha inválidos
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
\n''')
            menu_login()
        elif menu == 4:
            name = input('Digite seu nome de usuario: ')
            result = User.update_name(name)
            if result:
                os.system('cls')
                print(f'Nome de usuário alterado com sucesso')
                menu_login()
            else:
                os.system('cls')
                print(f'Nome de usuário já existente')
                menu_login()
        elif menu == 5:
            User.list_users()
            menu_login()
        elif menu == 6:
            name = input('Digite o nome do usuário: ')
            result = User.delete_user(name)
            if result:
                os.system('cls')
                print(f'Usuário deletado com sucesso')
                menu_login()
            else:
                os.system('cls')
                print(f'Usuário não existe')
                menu_login()
        elif menu == 99:
            break
        else:
            os.system('cls')
            print('''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       
                Opção inválida
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
\n''')
        menu = int(input('''

            __   ___   ____   _____  ___  _____ _____ ____  ___   ____   _____
   /  ] /   \ |    \ |     |/  _]/ ___// ___/|    |/   \ |    \ / ___/
  /  / |     ||  _  ||   __/  [_(   \_(   \_  |  ||     ||  _  (   \_ 
 /  /  |  O  ||  |  ||  |_|    _]\__  |\__  | |  ||  O  ||  |  |\__  |
/   \_ |     ||  |  ||   _]   [_ /  \ |/  \ | |  ||     ||  |  |/  \ |
\     ||     ||  |  ||  | |     |\    |\    | |  ||     ||  |  |\    |
 \____| \___/ |__|__||__| |_____| \___| \___||____|\___/ |__|__| \___|
                                                                      

    1- Cadastrar usuário
    2 - Login
    3 - Alterar senha
    4 - Alterar nome
    5 - Listar usuários
    6  - Deletar usuário
    99 - Sair

opção: '''))

def menu_logado(user_id, nome):
    menu = int(input(f'''
            ################################################
                Seja bem vindo(a) {nome} ao Confessions
                Escolha uma das opções abaixo:
            ################################################


    1 - Adicionar Confissão
    2 - Ver todas as Confissões
    3 - Ver suas Confissões
    4 - Atualizar Confissão
    5 - Deletar Confissão
    6 - Adicionar Like
    7 - Remover Like
    8 - Comente sobre alguma confissão
    9- Remover comentário de alguma confissão
    10 - Adicionar tema para alguma confissão
    11 - Remover tema de alguma confissão
    12 - Listar temas de alguma confissão
    13 - Reagir a alguma confissão
    14 - Remover reação de alguma confissão
    15 - Logout

opção: '''))
    while menu != 99:
        if menu == 1:
            os.system('cls')
            Confession.criar_confissao(user_id)
        elif menu == 2:
            os.system('cls')
            Confession.listar_todas_confissoes()
        elif menu == 3:
            Confession.listar_confissoes(user_id)
        elif menu == 4:
            Confession.atualizar_confissao(user_id)
        elif menu == 5:
            Confession.deletar_confissao(user_id)
        elif menu == 6:
            result = Likes.add_like()
            if result:
                os.system('cls')
                print('Like adicionado com sucesso')
            else:
                os.system('cls')
                print('Like já existente')
        elif menu == 7:
            result = Likes.remove_like()
            if result:
                os.system('cls')
                print('Like removido com sucesso')
            else:
                os.system('cls')
                print('Like não existente')
        elif menu == 8:
            result = Comment.add_comment(user_id)
            if result:
                os.system('cls')
                print(f'Comentário adicionado com sucesso')
                menu_logado(user_id, nome)
            else:
                os.system('cls')
                print(f'Comentário não adicionado')
                menu_logado(user_id, nome)
        elif menu == 9:
            result = Comment.remove_comment(user_id)
            if result:
                os.system('cls')
                print(f'Comentário removido com sucesso')
                menu_logado(user_id, nome)
            else:
                os.system('cls')
                print(f'Comentário não removido')
                menu_logado(user_id, nome)
        elif menu == 10:
            theme = input('Digite o tema que deseja: ')
            Themes.add_theme(theme, user_id)
        elif menu == 11:
            Themes.remove_theme()
        elif menu == 12:
            Themes.list_themes()
        elif menu == 13:
            Reaction.add_reaction(user_id)
        elif menu == 14:
            Reaction.remove_reaction(user_id)
        elif menu == 15:
            os.system('cls')
            menu_login()
        else:
            print('Opção inválida')
        menu = int(input(f'''
            ################################################
                Seja bem vindo(a) {nome} ao Confissions
                Escolha uma das opções abaixo:
            ################################################

        
    1 - Adicionar Confissão
    2 - Ver todas as Confissões
    3 - Ver suas Confissões
    4 - Atualizar Confissão
    5 - Deletar Confissão
    6 - Adicionar Like
    7 - Remover Like
    8 - Comente sobre alguma confissão
    9- Remover comentário de alguma confissão
    10 - Adicionar tema para alguma confissão
    11 - Remover tema de alguma confissão
    12 - Listar temas de alguma confissão
    13 - Reagir a alguma confissão
    14 - Remover reação de alguma confissão
    15 - Logout

opção: '''))

menu_login()
from models import Pessoas, Usuarios


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome = 'Felipe', idade = 20)
    print(pessoa)
    pessoa.save()

# Consulta tabela pessoa
def consulta():
    pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    print(pessoa)
    #pessoas = Pessoas.query.all()
    #print(pessoas)

# Altera tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome = 'Rodrigo').first()
    pessoa.nome = 'Alessandra'
    pessoa.save

# Exclui dados da tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Adriana').first()
    pessoa.delete()

def insere_usuario(login,senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
   #insere_usuario('rafael', '1234')
    #insere_usuario('galleani', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta()

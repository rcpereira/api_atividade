from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome = 'Adriana', idade = 43)
    print(pessoa)
    pessoa.save()

# Consulta tabela pessoa
def consulta():
    #pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    #print(pessoa.idade)
    pessoas = Pessoas.query.all()
    print(pessoas)

# Altera tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome = 'Adriana').first()
    pessoa.nome = 'Alessandra'
    pessoa.save

# Exclui dados da tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Adriana').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta()

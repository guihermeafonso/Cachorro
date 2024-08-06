from classe import *

def menu_principal():
    print("1-Criar Cão: ")
    print("2-Criar Pessoa: ")
    print("3-Listar Cão: ")
    print("4-Listar Pessoa: ")
    print("5-Excluir Cão: ")
    print("6-Excluir Pessoa: ")
    print("7-Editar Pessoa: ")
    print("8-Editar Cão: ")

def lista_atributos_pessoa():
    print("O que deseja alterar?")
    print("1 - Nome\n2 - Tamanho\n3 - Peso")

def lista_atributos_cao():
    print("O que deseja alterar?")
    print("1 - Nome\n2 - Tamanho\n3 - Raça")

def listar_pessoa(lista_de_humano):
    num=1
    for pessoa in lista_de_humano:
        print(f'{num}: {pessoa.nome}\n')
        num+=1
def listar_cao(lista_de_cao):
    num=1
    for cao in lista_de_cao:
        print(f'{num}: {cao.nome}\n')
        num+=1
        
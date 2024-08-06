from classe import *
from view import *
def criar_cao():
    nome=input("Digite o nome do cão: ")
    tamanho=input("Tamanho em cm: ")
    raca=input("Raça: ")
    cao=Cachorro(nome,tamanho,raca)
    return cao
def excluir_cao(nome_excluir,lista_de_cao):
    for cao in lista_de_cao:
        if nome_excluir == cao.nome:
            lista_de_cao.remove(cao)
            break
    print("Nome não encontrado!")

def excluir_pessoa(nome_excluir,lista_de_humano):
    for pessoa in lista_de_humano:
        if nome_excluir == pessoa.nome:
            lista_de_humano.remove(pessoa)
            break
    print("Nome não encontrado!")

def editar_pessoa(nome_editar,lista_de_humano):
    for pessoa in lista_de_humano:
        if nome_editar == pessoa.nome:
            op = int(input(lista_atributos_pessoa()))
            if op == 1:
                nome = input("Digite o novo nome:")
                pessoa.nome = nome
                break
            elif op == 2:
                tamanho = input("Digite o novo tamanho:")
                pessoa.tamanho = tamanho
                break
            elif op == 3:
                peso = input("Digite o novo nome:")
                pessoa.peso = peso
                break
            else:
                print("Não encontrado")
                break
    print("Nome não encontrado!")

def editar_cao(nome_editar,lista_de_cao):
    for cao in lista_de_cao:
        if nome_editar == cao.nome:
            op = int(input(lista_atributos_cao()))
            if op == 1:
                nome = input("Digite o novo nome:")
                cao.nome = nome
                break
            elif op == 2:
                tamanho = input("Digite o novo tamanho:")
                cao.tamanho = tamanho
                break
            elif op == 3:
                peso = input("Digite o novo nome:")
                cao.peso = peso
                break
            else:
                print("Não encontrado")
                break
    print("Nome não encontrado!")




def criar_humano():
    nome=input("Digite o nome: ") 
    tamanho=input("Tamanho em cm: ") 
    peso=input("Digite o peso: ")
    humano=Humano(nome,peso,tamanho)
    return humano
def listar(lista:list):
    if len(lista)>0:
        for objeto in lista:
            print(objeto.info())
    else:
        print("Lista vazia")
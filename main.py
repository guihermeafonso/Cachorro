from classe import *
from view import*
from functions import *

lista_de_cao=[]
lista_de_humano=[]


while True:
    menu_principal()
    op=int(input("Opção: "))
    if 1 == op:
        lista_de_cao.append(criar_cao())
    elif 2 == op:
        lista_de_humano.append(criar_humano())
    elif 3 == op:
        listar_cao(lista_de_cao)
    elif 4 == op:
        listar_pessoa(lista_de_humano)
    elif 5 == op:
        listar_cao(lista_de_cao)
        nome_excluir = input("Digite o nome do cão para excluir: ")
        excluir_cao(nome_excluir,lista_de_cao)
    elif 6 == op:
        listar_pessoa(lista_de_humano)
        nome_excluir = input("Digite o nome da pessoa para excluir: ")
        excluir_pessoa(nome_excluir,lista_de_humano)
    elif 7 == op:
        listar_pessoa(lista_de_humano)
        nome_editar = input("Digite o nome da pessoa para editar: ")
        editar_pessoa(nome_editar,lista_de_humano)
    elif 8 == op:
        listar_cao(lista_de_cao)
        nome_editar = input("Digite o nome do cao para editar: ")
        editar_cao(nome_editar,lista_de_cao)
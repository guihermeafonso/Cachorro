# class Animal:
#     nome:str
#     coracao:bool
#     racional:bool
#     peso:float
#     sexo:str

#     def __init__(self, nome, coracao, peso, sexo):
#         self.nome=nome
#         self.coracao=coracao
#         self.peso=peso
#         self.sexo=sexo

# class Humano(Animal):
#     cor_cabelo:str
#     def __init__(self, nome, peso, sexo, cor_cabelo):
#         super().__init__(nome,True,peso,sexo)
#         self.cor_cabelo=cor_cabelo


# class Cachorro(Animal):
#     tamanho:int
#     raca:str

#     def __init__(self, nome, tamanho, raca):
#         self.nome=nome
#         self.tamanho = tamanho
#         self.raca = raca
#         self.coracao=True
#         self.racional=False

#     def latir(self):
#         print("Au-Au")



class Animal:
    nome=str
    coracao:bool
    racional=bool
    tamanho=float
    def __init__(self,nome,tamanho,coracao,racional):
        self.nome=nome
        self.coracao=coracao
        self.racional=racional
        self.tamanho=tamanho
    def info(self):
        return{"nome":self.nome}

class Humano(Animal):
    def __init__(self, nome,peso,tamanho):
        super().__init__(nome,tamanho,coracao=True, racional=True)
        self.tamanho=tamanho
        self.racional=True
        self.peso=peso
class Cachorro(Animal):
    raca=""
    def __init__(self,nome,tamanho,raca):
        super().__init__(nome,tamanho,coracao=True,racional=False)
        self.raca=raca
        self.racional=False

    def latir(self):    
        print("Au,Au")
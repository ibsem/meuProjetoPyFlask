# Comentarios de uma linha 
'''
Aqui vai um comentario com varias linhas
''' 

# Primeira seção de um código em python vem com os imports das bibliotecas que vou usar
import os 
from pandas import ExcelWriter
import tkinter

# A segunda seção seção do código podem ser inseridas classes e 
# funções que serão executadas quando chamadas pelo código principal

def funcaoSoma(a,b):
    c = a + b
    return c

def executaAlgoSemParametro():
    print ("Mensagem Qualquer")
    return

# Terceira seçao do Codigo definida por
# if __name__ == '__main__': indica aonde o programa principal começa
if __name__ == '__main__':
    
    print (funcaoSoma(5,8))
    executaAlgoSemParametro()



''' numero = 45
    variavel = "E uma string"
    print ("Alo Python!!")
    print ('Alo Python novamente!!')
    print(variavel)
    resultado = numero + 6.6
    print (resultado)
    texto =  'É quase a minha idade'
    print (resultado, texto)
''' 


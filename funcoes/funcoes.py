import random
import string
from variaveis import *
import pygame

#para inicializar os modulos necessários
pygame.init()

banco_de_palavras = [
    "PYTHON", "CODIGO", "MATRIZ", "LOGICA", "DADOS",
    "LISTA", "WHILE", "INPUT", "PRINT", "DEV"
]

palavras = [] #guarda as palavras embaralhadas

#!pesquisar sobre random.choice and choices 

tela = pygame.display.set_mode((TELA_COMPRIMENTO,TELA_ALTURA))
fonte = pygame.font.SysFont(None, 16) #definindo o tamanho da fonte, e deixando a fonte padrão do pygame

class CacaPalavras:
    
    def __init__(self, linhas=10, colunas=10): 
        self.linhas = linhas 
        self.colunas = colunas 
        
    def montarJogo(self): 
        for _ in range(10): 
            #escolhendo a palavra 
            palavra_escolhida = random.choice(banco_de_palavras) 
            
            #criando uma lista com 10 letras aleatórias  
            aleatorio = random.choices(string.ascii_uppercase, k=10) #passando a biblioteca string e a tabela de letras maiúsculas, k= limite de caracteres
            
            #Sorteando onde a palavra vai começar
            sobra_espaco = 10 - len(palavra_escolhida)
            posicao_inicio = random.randint(0, sobra_espaco)
            
            #colocando a palavra dentro da linha de letras aleatórias
            for index in range(len(palavra_escolhida)):
                # substitui a letra aleatória pela a letra da palavra
                aleatorio[posicao_inicio +index] = palavra_escolhida[index]
            
            palavras.append(aleatorio)
    
    def mostrarJogo(self):

        for linha in range(len(palavras)):
            for coluna in range(len(palavras[linha])):
                
                #definir a posicção do quadrado 
                x = coluna * CELULA_QUADRADO
                y = linha * CELULA_QUADRADO
                
                #desenhar o quadrado
                pygame.draw.rect(tela, (200,200,200), (x + MARGEM_QUADRADO, y + MARGEM_QUADRADO, CELULA_QUADRADO - MARGEM_QUADRADO, CELULA_QUADRADO - MARGEM_QUADRADO), border_radius=10)

                #pegar a letra 
                letra = palavras[linha][coluna]
                
                #letra para texto
                texto = fonte.render(letra, True, (0,0,0))
                
                #centralizando o texto
                texto_centro = texto.get_rect(center=(x + CELULA_QUADRADO //2, y + CELULA_QUADRADO //2))
        
                #desenhar  o texto
                tela.blit(texto, texto_centro)
        
        
        # #mostrar os números das colunas 
        # linha_palavra = palavras[0] #primeira linha
        
        # print('  + ', end='') #dando uns espaços, assim os números ficam em cima das respecitvas letras
        # for index, letra in enumerate(linha_palavra):
        #     print(index, '', end='')
        # print() #evitar juntar a linha que fica a coluna e a linha do for debaixo
        
        # #linhas de divisão coluna/letra
        # print('  +', end='')
        # for index, letra in enumerate(linha_palavra):
        #     print("--", end='')
        # print() #evitar juntar a linha que fica a coluna e a linha do for debaixo
        
        # #mostrar as linhas com as letras separadas
        # for index, linha in enumerate(palavras):
        #     print(index, '|', '',end='')
        #     for letra in linha:
        #         print(letra, '', end="")
        #     print()
            
        # print()
        
        # #mostrar as palavaras a serem encontradas
        # print("Palavras Para Encontrar".center(60,"="))
        # for index,palavra in enumerate(banco_de_palavras):
        #     print(index +1, "|", palavra)
            



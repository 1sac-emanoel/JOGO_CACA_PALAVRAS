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

#!pesquisar sobre random.choice and choices 

tela = pygame.display.set_mode((TELA_COMPRIMENTO,TELA_ALTURA))
fonte = pygame.font.SysFont(None, 16) #definindo o tamanho da fonte, e deixando a fonte padrão do pygame

class CacaPalavras:
    
    def __init__(self, linhas=10, colunas=10):
        self.linhas = linhas
        self.colunas = colunas
        self.palavras = []
        self.selecao = []  # lista de (linha, coluna)
        self.arrastando = False
        self.palavras_encontradas = set()
        self.celulas_fixadas = set()
        self.palavras_no_jogo = []
        self.matriz = [["" for _ in range(self.colunas)] for _ in range(self.linhas)] 

            
    # def montarJogo(self):
    #     self.palavras = []  # limpa antes de montar

    #     for _ in range(self.linhas):
    #         #escolhendo a palavra
    #         palavra_escolhida = random.choice(banco_de_palavras)
            
    #         #criando uma lista com 10 letras aleatórias
    #         aleatorio = random.choices(string.ascii_uppercase, k=self.colunas)#passando a biblioteca string e a tabela de letras maiúsculas, k= limite de caracteres

    #         #Sorteando onde a palavra vai começar
    #         sobra_espaco = self.colunas - len(palavra_escolhida)
    #         posicao_inicio = random.randint(0, sobra_espaco)

    #         #colocando a palavra dentro da linha de letras aleatórias
    #         for index in range(len(palavra_escolhida)):
    #             # substitui a letra aleatória pela a letra da palavra
    #             aleatorio[posicao_inicio + index] = palavra_escolhida[index]

    #         self.palavras.append(aleatorio)
            
    def montarJogo(self):
        self.matriz = [["" for _ in range(self.colunas)] for _ in range(self.linhas)]
        self.palavras_no_jogo = []

        for palavra in banco_de_palavras:
            if self.tentar_inserir_palavra(palavra):
                self.palavras_no_jogo.append(palavra)

        self.preencher_com_letras()

        # matriz vira palavras (pra não quebrar o resto do código)
        self.palavras = self.matriz

    def tentar_inserir_palavra(self, palavra):
        direcao = random.choice(["H", "V"])
        tamanho = len(palavra)

        if direcao == "H":
            linha = random.randint(0, self.linhas - 1)
            coluna = random.randint(0, self.colunas - tamanho)

            for i in range(tamanho):
                letra = self.matriz[linha][coluna + i]
                if letra != "" and letra != palavra[i]:
                    return False

            for i in range(tamanho):
                self.matriz[linha][coluna + i] = palavra[i]

            return True

        else:  # VERTICAL
            linha = random.randint(0, self.linhas - tamanho)
            coluna = random.randint(0, self.colunas - 1)

            for i in range(tamanho):
                letra = self.matriz[linha + i][coluna]
                if letra != "" and letra != palavra[i]:
                    return False

            for i in range(tamanho):
                self.matriz[linha + i][coluna] = palavra[i]

            return True

    def preencher_com_letras(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.matriz[i][j] == "":
                    self.matriz[i][j] = random.choice(string.ascii_uppercase)

    
    def mostrarJogo(self,tela):

        for linha in range(len(self.palavras)):
            for coluna in range(len(self.palavras[linha])):
                
                #definir a posicção do quadrado 
                x = OFFSET_X + coluna * CELULA_QUADRADO
                y = OFFSET_Y + linha * CELULA_QUADRADO

                # cor da célula
                if (linha, coluna) in self.celulas_fixadas:
                    cor = (160, 200, 160)  # verde (encontrada)
                elif (linha, coluna) in self.selecao:
                    cor = (180, 220, 255)  # azul (seleção atual)
                else:
                    cor = (245, 245, 245)  # branca

                    
                    
                #desenhar o quadrado
                pygame.draw.rect(
                    tela,
                    cor,
                    (x, y, CELULA_QUADRADO - 2, CELULA_QUADRADO - 2),
                    border_radius=6
                )


                #pegar a letra 
                letra = self.palavras[linha][coluna]
                
                #letra para texto
                texto = fonte.render(letra, True, (0,0,0))
                
                #centralizando o texto
                texto_centro = texto.get_rect(center=(x + CELULA_QUADRADO //2, y + CELULA_QUADRADO //2))
        
                #desenhar  o texto
                tela.blit(texto, texto_centro)

    def mostrarListaPalavras(self):
        OFFSET_X = 40

        largura_tabuleiro = self.colunas * CELULA_QUADRADO
        fim_tabuleiro = OFFSET_X + largura_tabuleiro

        x = fim_tabuleiro + 40
        y = 120
        espacamento = 30

        # fundo da lista
        pygame.draw.rect(
            tela,
            (255, 255, 255),
            (x - 20, y - 60, 260, 350),
            border_radius=12
        )

        titulo = fonte.render("Palavras para encontrar", True, (40, 40, 40))
        tela.blit(titulo, (x, y - 40))

        for i, palavra in enumerate(self.palavras_no_jogo):
            if palavra in self.palavras_encontradas:
                texto = fonte.render(palavra, True, (120, 120, 120))
                tela.blit(texto, (x, y + i * espacamento))

                # risco
                largura = texto.get_width()
                altura = texto.get_height()
                y_risco = y + i * espacamento + altura // 2

                pygame.draw.line(
                    tela,
                    (120, 120, 120),
                    (x, y_risco),
                    (x + largura, y_risco),
                    2
                )
            else:
                texto = fonte.render(palavra, True, (60, 60, 60))
                tela.blit(texto, (x, y + i * espacamento))


    def mouse_para_celula(self, pos):
        OFFSET_X = 40
        OFFSET_Y = 80

        mx, my = pos

        coluna = (mx - OFFSET_X) // CELULA_QUADRADO
        linha = (my - OFFSET_Y) // CELULA_QUADRADO

        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            return linha, coluna

        return None
    
    
    def tratarMouse(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            celula = self.mouse_para_celula(evento.pos)
            if celula:
                self.selecao = [celula]
                self.arrastando = True

        elif evento.type == pygame.MOUSEMOTION and self.arrastando:
            celula = self.mouse_para_celula(evento.pos)
            if celula and celula not in self.selecao:
                self.selecao.append(celula)

        elif evento.type == pygame.MOUSEBUTTONUP:
            self.arrastando = False

            palavra, palavra_invertida = self.obter_palavra_selecionada()

            if palavra in banco_de_palavras:
                self.palavras_encontradas.add(palavra)
                self.celulas_fixadas.update(self.selecao)

            elif palavra_invertida in banco_de_palavras:
                self.palavras_encontradas.add(palavra_invertida)
                self.celulas_fixadas.update(self.selecao)

            self.selecao = []
            
            
    def obter_palavra_selecionada(self):
        letras = []

        for linha, coluna in self.selecao:
            letras.append(self.palavras[linha][coluna])

        palavra = "".join(letras)
        palavra_invertida = palavra[::-1]

        return palavra, palavra_invertida


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
            



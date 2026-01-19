import pygame
from funcoes.funcoes import CacaPalavras, tela
from variaveis import *

#pygame setup
pygame.init()

pygame.display.set_caption("CAÇA-PALAVRAS")

clock = pygame.time.Clock()

#fundo
fundo = pygame.image.load("assets\Backgrounds\Blue.png").convert()
fundo = pygame.transform.scale(fundo, (TELA_COMPRIMENTO, TELA_ALTURA))

def main():            
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                
        #desenho de fundo da tela
        tela.blit(fundo, (0,0))        
                
        #caça palavras
        Objeto = CacaPalavras()
        Objeto.montarJogo()
        Objeto.mostrarJogo()
        
        #atualizando a tela 
        pygame.display.flip()
        
        clock.tick(60)
        
    
    
if __name__ == "__main__":
    main()
#~~~~~ Sudoku GUI intended for entry point ~~~~~#

import pygame, time
from Sudoku_Solver_GUI import initialiseSolverGUI
from Sudoku_Game_GUI import initialiseGameGUI

def runApplication():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1000,601))
    pygame.display.set_caption("Sudoku by Mattyou Quinn")

    white = (255,255,255)
    black = (50,50,50)
    noticeColour = (170,170,170)
    buttonColour = (65,150,240)
    buttonColourHover = (95,170,255)
    buttonColourPressed = (60,140,225)

    mainTitleFont = pygame.font.SysFont('arial',90)
    buttonTextFont = pygame.font.SysFont('arial',35)
    noticeTextFont = pygame.font.SysFont('arial',20)

    finished = False

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        mousePos = pygame.mouse.get_pos()
        gameDisplay.fill(white)

        gameDisplay.blit(mainTitleFont.render("Welcome to",False,black),(290,70))
        gameDisplay.blit(mainTitleFont.render("sudoku!",False,black),(350,170))

        for i in range(3):
            pygame.draw.rect(gameDisplay,buttonColour,(200*i+190,290,180,60),border_radius=4)
            if (200*i+190) < mousePos[0] < (200*i+370) and 290 < mousePos[1] < 350:
                pygame.draw.rect(gameDisplay,buttonColourHover,(200*i+190,290,180,60),border_radius=4)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(gameDisplay,buttonColourPressed,(200*i+190,290,180,60),border_radius=4)
                    if i == 0:
                        initialiseGameGUI()
                        runApplication()
                    if i == 1:
                        initialiseSolverGUI()
                        runApplication()
                    if i == 2:
                        finished = True

        gameDisplay.blit(buttonTextFont.render("Game",False,black),(238,300))
        gameDisplay.blit(buttonTextFont.render("Solver",False,black),(436,300))
        gameDisplay.blit(buttonTextFont.render("Quit",False,black),(650,300))

        gameDisplay.blit(noticeTextFont.render("Designed + made by Mattyou Quinn",False,noticeColour),(350,360))

        pygame.display.flip()
        time.sleep(0.082)

    pygame.quit()

import pygame
pygame.init

screen = pygame.display.set_mode([1000, 600])
pygame.display.set_caption('Игорь ЛОХ')

def main():
    pygame.init()
    screen.fill((0, 0, 0))
    game_over()
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitbutton.collidepoint(event.pos) == True:
                    running = False
                if restartbutton.collidepoint(event.pos) == True:
                    #gameloop()
                    #pygame.display.flip()
                    pass


def game_over():
    
    global font, restartbutton, exitbutton, go_screen

    go_screen = pygame.display.set_mode([1000, 600])

    font = pygame.font.Font('C:\\Users\\арп\\Desktop\\GeekBrains\\основное\\дз\\game_try\\CholesterolGlitch.otf', 50)

    restarttext = font.render('RESTART', True, (255, 0, 0))
    exittext = font.render('EXIT', True, (255, 0, 0))

    pic = pygame.image.load('C:\\Users\\арп\\Desktop\\GeekBrains\\основное\\дз\\game_try\\gameover.jpg')
    go_screen.blit(pic, (0, 0))

    exitbutton = pygame.draw.rect(screen, (0, 0, 0), (210, 383, 199, 51), 0)
    restartbutton = pygame.draw.rect(screen, (0, 0, 0), (584, 383, 199, 51), 0)
    
    go_screen.blit(restarttext, (603 ,389))
    go_screen.blit(exittext, (265, 389))
    

if __name__ == '__main__':
    main()
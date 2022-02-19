import pygame
from pygame import key
import os
import sys
import math

sys.setrecursionlimit(30000)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Adventures')
    size = width,height = 990,990
    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()
    FPS = 60
    map = []

    with open('DokinsKING version\samples\map.map',encoding='utf-8') as f:
        count = 0
        for i in f:
            map.append([])
            for z in range(1,len(i)):
                map[count].append(i[z-1:z])
            count += 1
        map[-1].append('#')

    world = pygame.Surface((len(map[0]) * 90,len(map) * 90))

    #загрузка изображения игрока
    def load_image(name, color_key=None):
        fullname = os.path.join('DokinsKING version\samples', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)
        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
                image.set_colorkey(color_key)
                return image
            else:
                image = image.convert_alpha()
                return image

    l = 0
    t = 0
    w = False


    for i in range(len(map)):
        for z in range(len(map[i])):
            if map[i][z] == 'P':
                l = z
                t = i



    class Camera():
        def __init__(self,screen,world,l,t):
            self.screen = screen
            self.world = world
            x = -(l - 5)
            y = -(t - 5)
            self.x = x * 90
            self.y = y * 90


        def moving(self):
            ear.spawning()
            box.spawning()
            en.spawning()
            self.screen.blit(self.world, (self.x,self.y))


    class Player():
        def __init__(self,screen):
            self.screen = screen
            self.plg = pygame.sprite.Group()
            self.turn = False

            self.count = 0
            self.frame = ['penguin\Idle\Armature_IDLE_00.png',
                        'penguin\Idle\Armature_IDLE_01.png',
                        'penguin\Idle\Armature_IDLE_02.png',
                        'penguin\Idle\Armature_IDLE_03.png', 
                        'penguin\Idle\Armature_IDLE_04.png',
                        'penguin\Idle\Armature_IDLE_05.png',
                        'penguin\Idle\Armature_IDLE_06.png',
                        'penguin\Idle\Armature_IDLE_07.png',
                        'penguin\Idle\Armature_IDLE_08.png',
                        'penguin\Idle\Armature_IDLE_09.png',
                        'penguin\Idle\Armature_IDLE_10.png',
                        'penguin\Idle\Armature_IDLE_11.png',
                        'penguin\Idle\Armature_IDLE_12.png',
                        'penguin\Idle\Armature_IDLE_13.png',
                        'penguin\Idle\Armature_IDLE_14.png',
                        'penguin\Idle\Armature_IDLE_15.png',
                        'penguin\Idle\Armature_IDLE_16.png',
                        'penguin\Idle\Armature_IDLE_17.png',
                        'penguin\Idle\Armature_IDLE_18.png',
                        'penguin\Idle\Armature_IDLE_19.png',
                        'penguin\Idle\Armature_IDLE_20.png',
                        'penguin\Idle\Armature_IDLE_21.png',
                        'penguin\Idle\Armature_IDLE_22.png',
                        'penguin\Idle\Armature_IDLE_23.png',
                        'penguin\Idle\Armature_IDLE_24.png',
                        'penguin\Idle\Armature_IDLE_25.png',
                        'penguin\Idle\Armature_IDLE_26.png',
                        'penguin\Idle\Armature_IDLE_27.png',
                        'penguin\Idle\Armature_IDLE_28.png',
                        'penguin\Idle\Armature_IDLE_29.png',
                        'penguin\Idle\Armature_IDLE_31.png',
                        'penguin\Idle\Armature_IDLE_32.png',
                        'penguin\Idle\Armature_IDLE_33.png',
                        'penguin\Idle\Armature_IDLE_34.png',
                        'penguin\Idle\Armature_IDLE_35.png',
                        'penguin\Idle\Armature_IDLE_36.png',
                        'penguin\Idle\Armature_IDLE_37.png',
                        'penguin\Idle\Armature_IDLE_38.png',
                        'penguin\Idle\Armature_IDLE_40.png']

            self.frame_attack = ['penguin\Shot\Armature_SHOT_1_0.png',
                                'penguin\Shot\Armature_SHOT_1_1.png',       
                                'penguin\Shot\Armature_SHOT_1_2.png',      
                                'penguin\Shot\Armature_SHOT_1_3.png',           
                                'penguin\Shot\Armature_SHOT_1_4.png',       
                                'penguin\Shot\Armature_SHOT_1_5.png',        
                                'penguin\Shot\Armature_SHOT_1_6.png',        
                                'penguin\Shot\Armature_SHOT_1_7.png']

            self.frame_hurt = ['penguin\Hurt\Armature_HURT_0.png',
                            'penguin\Hurt\Armature_HURT_1.png',
                            'penguin\Hurt\Armature_HURT_2.png',
                            'penguin\Hurt\Armature_HURT_3.png',
                            'penguin\Hurt\Armature_HURT_4.png',
                            'penguin\Hurt\Armature_HURT_5.png',
                            'penguin\Hurt\Armature_HURT_6.png',
                            'penguin\Hurt\Armature_HURT_7.png']
            
            self.frame_reload = ['penguin\Reload\Armature_RELOAD_00.png',
                                'penguin\Reload\Armature_RELOAD_01.png',
                                'penguin\Reload\Armature_RELOAD_02.png',
                                'penguin\Reload\Armature_RELOAD_03.png',
                                'penguin\Reload\Armature_RELOAD_04.png',
                                'penguin\Reload\Armature_RELOAD_05.png',
                                'penguin\Reload\Armature_RELOAD_06.png',
                                'penguin\Reload\Armature_RELOAD_07.png',
                                'penguin\Reload\Armature_RELOAD_08.png',
                                'penguin\Reload\Armature_RELOAD_09.png',
                                'penguin\Reload\Armature_RELOAD_10.png',
                                'penguin\Reload\Armature_RELOAD_11.png',
                                'penguin\Reload\Armature_RELOAD_12.png',
                                'penguin\Reload\Armature_RELOAD_13.png',
                                'penguin\Reload\Armature_RELOAD_14.png',
                                'penguin\Reload\Armature_RELOAD_15.png',
                                'penguin\Reload\Armature_RELOAD_16.png',
                                'penguin\Reload\Armature_RELOAD_17.png',
                                'penguin\Reload\Armature_RELOAD_18.png',
                                'penguin\Reload\Armature_RELOAD_19.png',
                                'penguin\Reload\Armature_RELOAD_20.png',
                                'penguin\Reload\Armature_RELOAD_21.png',
                                'penguin\Reload\Armature_RELOAD_22.png',
                                'penguin\Reload\Armature_RELOAD_23.png',
                                'penguin\Reload\Armature_RELOAD_24.png',
                                'penguin\Reload\Armature_RELOAD_25.png',
                                'penguin\Reload\Armature_RELOAD_26.png',
                                'penguin\Reload\Armature_RELOAD_27.png',
                                'penguin\Reload\Armature_RELOAD_28.png',
                                'penguin\Reload\Armature_RELOAD_29.png',
                                'penguin\Reload\Armature_RELOAD_30.png',
                                'penguin\Reload\Armature_RELOAD_31.png',
                                'penguin\Reload\Armature_RELOAD_32.png',
                                'penguin\Reload\Armature_RELOAD_33.png',
                                'penguin\Reload\Armature_RELOAD_34.png',
                                'penguin\Reload\Armature_RELOAD_35.png',
                                'penguin\Reload\Armature_RELOAD_36.png',
                                'penguin\Reload\Armature_RELOAD_37.png',
                                'penguin\Reload\Armature_RELOAD_38.png',
                                'penguin\Reload\Armature_RELOAD_39.png',
                                'penguin\Reload\Armature_RELOAD_40.png']

            self.frame_death = ['penguin\Death\Armature_DEAD_00.png',
                                'penguin\Death\Armature_DEAD_01.png',                   
                                'penguin\Death\Armature_DEAD_02.png',
                                'penguin\Death\Armature_DEAD_03.png',
                                'penguin\Death\Armature_DEAD_04.png',
                                'penguin\Death\Armature_DEAD_05.png',
                                'penguin\Death\Armature_DEAD_06.png',
                                'penguin\Death\Armature_DEAD_07.png',
                                'penguin\Death\Armature_DEAD_08.png',
                                'penguin\Death\Armature_DEAD_09.png',
                                'penguin\Death\Armature_DEAD_10.png',
                                'penguin\Death\Armature_DEAD_11.png',
                                'penguin\Death\Armature_DEAD_12.png',
                                'penguin\Death\Armature_DEAD_13.png',
                                'penguin\Death\Armature_DEAD_14.png',
                                'penguin\Death\Armature_DEAD_15.png',
                                'penguin\Death\Armature_DEAD_16.png',
                                'penguin\Death\Armature_DEAD_17.png',
                                'penguin\Death\Armature_DEAD_18.png',
                                'penguin\Death\Armature_DEAD_19.png',
                                'penguin\Death\Armature_DEAD_20.png',
                                'penguin\Death\Armature_DEAD_21.png',
                                'penguin\Death\Armature_DEAD_22.png',
                                'penguin\Death\Armature_DEAD_23.png',
                                'penguin\Death\Armature_DEAD_24.png',
                                'penguin\Death\Armature_DEAD_25.png',
                                'penguin\Death\Armature_DEAD_26.png',
                                'penguin\Death\Armature_DEAD_27.png',
                                'penguin\Death\Armature_DEAD_28.png',
                                'penguin\Death\Armature_DEAD_29.png',
                                'penguin\Death\Armature_DEAD_30.png',
                                'penguin\Death\Armature_DEAD_31.png',
                                'penguin\Death\Armature_DEAD_32.png']


            self.frame_run = ['penguin\Run\Armature_RUN_00.png', 
                            'penguin\Run\Armature_RUN_01.png',                                          
                            'penguin\Run\Armature_RUN_02.png',                                          
                            'penguin\Run\Armature_RUN_03.png',                                          
                            'penguin\Run\Armature_RUN_04.png',                                          
                            'penguin\Run\Armature_RUN_05.png',                                          
                            'penguin\Run\Armature_RUN_06.png',                                          
                            'penguin\Run\Armature_RUN_07.png',                                          
                            'penguin\Run\Armature_RUN_08.png',                                          
                            'penguin\Run\Armature_RUN_09.png',                                          
                            'penguin\Run\Armature_RUN_10.png',                                          
                            'penguin\Run\Armature_RUN_11.png',
                            'penguin\Run\Armature_RUN_12.png',
                            'penguin\Run\Armature_RUN_13.png',                                          
                            'penguin\Run\Armature_RUN_14.png',                                          
                            'penguin\Run\Armature_RUN_15.png']

            self.image = pygame.transform.scale(load_image(self.frame[self.count],-1), (90, 90))

            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = self.image
            self.sprite.rect = self.sprite.image.get_rect()
            self.plg.add(self.sprite)

        def spawning(self,w,l,t):
            if self.turn:
                self.sprite.image = pygame.transform.flip(self.image, self.turn, False)
            else:
                self.sprite.image = self.image
            if w:
                if l < 5:
                    self.sprite.rect.x = l * 105
                    self.plg.draw(self.screen)
            else:
                self.sprite.rect.x = 480
                self.sprite.rect.y = 450
                self.plg.draw(self.screen)

    class Enemy():
        image = load_image('penguin\Idle\Armature_IDLE_00.png',-1)
        def __init__(self,world):
            self.world = world
            self.eng = pygame.sprite.Group()

            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = pygame.transform.scale(Enemy.image,(90,90))
            self.sprite.rect = self.sprite.image.get_rect()
            self.eng.add(self.sprite)

        def spawning(self):
            for i in range(len(map)):
                for z in range(len(map[i])):
                    if map[i][z] == 'E':
                        self.sprite.rect.x = z * 90
                        self.sprite.rect.y = i * 90
                        self.eng.draw(self.world)

    class Earth():
        image = load_image('grass.png',0)
        def __init__(self,world):
            self.world = world
            self.earg = pygame.sprite.Group()

            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = Earth.image
            self.sprite.rect = self.sprite.image.get_rect()
            self.earg.add(self.sprite)

        def spawning(self):
            for i in range(len(map)):
                for z in range(len(map[i])):
                    if map[i][z] == '.' or map[i][z] == 'P' or map[i][z] == 'E':
                        self.sprite.rect.x = z * 90
                        self.sprite.rect.y = i * 90
                        self.earg.draw(self.world)
    
    class Box():
        image = load_image('box.png',0)
        
        def __init__(self,world):
            self.world = world
            self.boxg = pygame.sprite.Group()

            self.sprite = pygame.sprite.Sprite()
            self.sprite.image = Box.image
            self.sprite.rect = self.sprite.image.get_rect()
            self.boxg.add(self.sprite)

        def spawning(self):
            for i in range(len(map)):
                for z in range(len(map[i])):
                    if map[i][z] == '#':
                        self.sprite.rect.x = z * 90
                        self.sprite.rect.y = i * 90
                        self.boxg.draw(self.world)

    camera = Camera(screen,world,l,t)
    pl = Player(screen)
    en = Enemy(world)
    ear = Earth(world)
    box = Box(world)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print(map)

        if l < 5:
            w = True
        else:
            w = False


        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_w]: 
            if map[t-1][l] != '#' and map[t-1][l] != 'E':
                map[t][l] = '.'
                map[t-1][l] = 'P'
                t -= 1
                camera.y += 90
        elif keys[pygame.K_s]:
            if map[t+1][l] != '#' and map[t+1][l] != 'E':
                map[t][l] = '.'
                map[t+1][l] = 'P'
                t += 1
                camera.y -= 90
        if keys[pygame.K_a]:
            if map[t][l-1] != '#' and map[t][l-1] != 'E':
                pl.turn = True
                map[t][l] = '.'
                map[t][l-1] = 'P'
                l -= 1
                if w:
                    pass
                elif not w and l > 4:
                    camera.x += 90
        elif keys[pygame.K_d]:
            if map[t][l+1] != '#' and map[t][l+1] != 'E':
                pl.turn = False
                map[t][l] = '.'
                map[t][l+1] = 'P'
                l += 1
                if w:
                    pass
                elif not w and l > 4:
                    camera.x -= 90
        camera.moving()
        pl.spawning(w,l,t)

        clock.tick(FPS)
        pygame.display.flip()
        screen.fill('black')

    pygame.quit()
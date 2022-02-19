import pygame
import os 
import sys
import argparse
import math
import time 
import random



map = []

with open('E:\ERNEST_GANDON\game_try\map.map', encoding='utf-8') as f:
    count = 0
    for i in f:
        map.append([])
        for z in range(1,len(i)):
            map[count].append(i[z-1:z])
        count += 1
    map[-1].append('#')

    world = pygame.Surface((len(map[0]) * 90,len(map) * 90))

def load_image(name, color_key=None):
    fullname = 'game_try\\' + name
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    return image


class Heart(pygame.sprite.Sprite):
    def __init__(self, group, screen):
        super().__init__(group)
        
        self.screen = screen
        self.image = pygame.transform.scale(load_image('data\heart\heart.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.coord_list = []
        self.make_coord()
    
    
    def make_coord(self):
        for i in range(5):
            self.coord_list.append(i * 30 + 10)

    def update(self):
        for i in self.coord_list:
            self.screen.blit(self.image, (i, 10))

class Coins(pygame.sprite.Sprite):
    def __init__(self, group, sheet, columns, x, y):
        super().__init__(group)
        self.x = x + 40
        self.y = y + 50
        self.frames = []
        self.cut_sheet(sheet, columns)
        self.cur_frame = 0
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (50, 50))
        self.rect = self.rect.move(self.x, self.y)
        
    
    def cut_sheet(self, sheet, columns):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height())
        for i in range(columns):
            frame_location = (self.rect.w * i, 0)
            self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        if self.cur_frame > 69:
            self.cur_frame = 0 
        self.cur_frame += 1
        self.res_count = math.floor(self.cur_frame / 3)
        self.image = pygame.transform.scale(self.frames[self.res_count], (50, 50))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, group, sheet, columns, x, y, pos):
        super().__init__(group)
        self.pos = pos
        if self.pos:
            self.x = x - 90
        else:
            self.x = x + 90
        self.y = y + 13
        self.frames = []
        self.cut_sheet(sheet, columns)
        self.cur_frame = 0
        self.image = pygame.transform.scale(self.frames[self.cur_frame], (30, 30))
        self.rect = self.rect.move(self.x, self.y)
        self.count = 0
        
        
    
    def cut_sheet(self, sheet, columns):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height())
        for i in range(columns):
            frame_location = (self.rect.w * i, 0)
            self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):

        if self.cur_frame > 12:
            self.cur_frame = 0 
        self.cur_frame += 1
        
        self.res_count = math.floor(self.cur_frame / 4)
        self.image = pygame.transform.scale(self.frames[self.res_count], (50, 50))
        self.count += 1
        if self.pos:
            self.rect.x -= 5
        else:
            self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.count = 0
        self.frame = ['data\penguin\Idle\Armature_IDLE_00.png',
                      'data\penguin\Idle\Armature_IDLE_01.png',
                      'data\penguin\Idle\Armature_IDLE_02.png',
                      'data\penguin\Idle\Armature_IDLE_03.png', 
                      'data\penguin\Idle\Armature_IDLE_04.png',
                      'data\penguin\Idle\Armature_IDLE_05.png',
                      'data\penguin\Idle\Armature_IDLE_06.png',
                      'data\penguin\Idle\Armature_IDLE_07.png',
                      'data\penguin\Idle\Armature_IDLE_08.png',
                      'data\penguin\Idle\Armature_IDLE_09.png',
                      'data\penguin\Idle\Armature_IDLE_10.png',
                      'data\penguin\Idle\Armature_IDLE_11.png',
                      'data\penguin\Idle\Armature_IDLE_12.png',
                      'data\penguin\Idle\Armature_IDLE_13.png',
                      'data\penguin\Idle\Armature_IDLE_14.png',
                      'data\penguin\Idle\Armature_IDLE_15.png',
                      'data\penguin\Idle\Armature_IDLE_16.png',
                      'data\penguin\Idle\Armature_IDLE_17.png',
                      'data\penguin\Idle\Armature_IDLE_18.png',
                      'data\penguin\Idle\Armature_IDLE_19.png',
                      'data\penguin\Idle\Armature_IDLE_20.png',
                      'data\penguin\Idle\Armature_IDLE_21.png',
                      'data\penguin\Idle\Armature_IDLE_22.png',
                      'data\penguin\Idle\Armature_IDLE_23.png',
                      'data\penguin\Idle\Armature_IDLE_24.png',
                      'data\penguin\Idle\Armature_IDLE_25.png',
                      'data\penguin\Idle\Armature_IDLE_26.png',
                      'data\penguin\Idle\Armature_IDLE_27.png',
                      'data\penguin\Idle\Armature_IDLE_28.png',
                      'data\penguin\Idle\Armature_IDLE_29.png',
                      'data\penguin\Idle\Armature_IDLE_31.png',
                      'data\penguin\Idle\Armature_IDLE_32.png',
                      'data\penguin\Idle\Armature_IDLE_33.png',
                      'data\penguin\Idle\Armature_IDLE_34.png',
                      'data\penguin\Idle\Armature_IDLE_35.png',
                      'data\penguin\Idle\Armature_IDLE_36.png',
                      'data\penguin\Idle\Armature_IDLE_37.png',
                      'data\penguin\Idle\Armature_IDLE_38.png',
                      'data\penguin\Idle\Armature_IDLE_40.png']                                                        

        self.frame_attack = ['data\penguin\Shot\Armature_SHOT_1_0.png',
                             'data\penguin\Shot\Armature_SHOT_1_1.png',       
                             'data\penguin\Shot\Armature_SHOT_1_2.png',      
                             'data\penguin\Shot\Armature_SHOT_1_3.png',           
                             'data\penguin\Shot\Armature_SHOT_1_4.png',       
                             'data\penguin\Shot\Armature_SHOT_1_5.png',        
                             'data\penguin\Shot\Armature_SHOT_1_6.png',        
                             'data\penguin\Shot\Armature_SHOT_1_7.png']

        self.frame_hurt = ['data\penguin\Hurt\Armature_HURT_0.png',
                           'data\penguin\Hurt\Armature_HURT_1.png',
                           'data\penguin\Hurt\Armature_HURT_2.png',
                           'data\penguin\Hurt\Armature_HURT_3.png',
                           'data\penguin\Hurt\Armature_HURT_4.png',
                           'data\penguin\Hurt\Armature_HURT_5.png',
                           'data\penguin\Hurt\Armature_HURT_6.png',
                           'data\penguin\Hurt\Armature_HURT_7.png']

        self.frame_jump = ['data\penguin\Jump\Armature_JUMP_00.png',
                           'data\penguin\Jump\Armature_JUMP_01.png',
                           'data\penguin\Jump\Armature_JUMP_02.png',
                           'data\penguin\Jump\Armature_JUMP_03.png',
                           'data\penguin\Jump\Armature_JUMP_04.png',
                           'data\penguin\Jump\Armature_JUMP_05.png',
                           'data\penguin\Jump\Armature_JUMP_06.png',
                           'data\penguin\Jump\Armature_JUMP_07.png',
                           'data\penguin\Jump\Armature_JUMP_08.png',
                           'data\penguin\Jump\Armature_JUMP_09.png',
                           'data\penguin\Jump\Armature_JUMP_10.png',
                           'data\penguin\Jump\Armature_JUMP_11.png',
                           'data\penguin\Jump\Armature_JUMP_12.png',
                           'data\penguin\Jump\Armature_JUMP_13.png',
                           'data\penguin\Jump\Armature_JUMP_14.png',
                           'data\penguin\Jump\Armature_JUMP_15.png',
                           'data\penguin\Jump\Armature_JUMP_16.png',
                           'data\penguin\Jump\Armature_JUMP_17.png',
                           'data\penguin\Jump\Armature_JUMP_18.png',
                           'data\penguin\Jump\Armature_JUMP_19.png',
                           'data\penguin\Jump\Armature_JUMP_20.png',
                           'data\penguin\Jump\Armature_JUMP_21.png',
                           'data\penguin\Jump\Armature_JUMP_22.png',
                           'data\penguin\Jump\Armature_JUMP_23.png',
                           'data\penguin\Jump\Armature_JUMP_24.png',
                           'data\penguin\Jump\Armature_JUMP_25.png',
                           'data\penguin\Jump\Armature_JUMP_26.png',
                           'data\penguin\Jump\Armature_JUMP_27.png',
                           'data\penguin\Jump\Armature_JUMP_28.png',
                           'data\penguin\Jump\Armature_JUMP_29.png',
                           'data\penguin\Jump\Armature_JUMP_30.png',
                           'data\penguin\Jump\Armature_JUMP_31.png',
                           'data\penguin\Jump\Armature_JUMP_32.png',
                           'data\penguin\Jump\Armature_JUMP_33.png',
                           'data\penguin\Jump\Armature_JUMP_34.png',
                           'data\penguin\Jump\Armature_JUMP_35.png',
                           'data\penguin\Jump\Armature_JUMP_36.png',
                           'data\penguin\Jump\Armature_JUMP_37.png',
                           'data\penguin\Jump\Armature_JUMP_38.png',
                           'data\penguin\Jump\Armature_JUMP_39.png',
                           'data\penguin\Jump\Armature_JUMP_40.png']
        
        self.frame_reload = ['data\penguin\Reload\Armature_RELOAD_00.png',
                             'data\penguin\Reload\Armature_RELOAD_01.png',
                             'data\penguin\Reload\Armature_RELOAD_02.png',
                             'data\penguin\Reload\Armature_RELOAD_03.png',
                             'data\penguin\Reload\Armature_RELOAD_04.png',
                             'data\penguin\Reload\Armature_RELOAD_05.png',
                             'data\penguin\Reload\Armature_RELOAD_06.png',
                             'data\penguin\Reload\Armature_RELOAD_07.png',
                             'data\penguin\Reload\Armature_RELOAD_08.png',
                             'data\penguin\Reload\Armature_RELOAD_09.png',
                             'data\penguin\Reload\Armature_RELOAD_10.png',
                             'data\penguin\Reload\Armature_RELOAD_11.png',
                             'data\penguin\Reload\Armature_RELOAD_12.png',
                             'data\penguin\Reload\Armature_RELOAD_13.png',
                             'data\penguin\Reload\Armature_RELOAD_14.png',
                             'data\penguin\Reload\Armature_RELOAD_15.png',
                             'data\penguin\Reload\Armature_RELOAD_16.png',
                             'data\penguin\Reload\Armature_RELOAD_17.png',
                             'data\penguin\Reload\Armature_RELOAD_18.png',
                             'data\penguin\Reload\Armature_RELOAD_19.png',
                             'data\penguin\Reload\Armature_RELOAD_20.png',
                             'data\penguin\Reload\Armature_RELOAD_21.png',
                             'data\penguin\Reload\Armature_RELOAD_22.png',
                             'data\penguin\Reload\Armature_RELOAD_23.png',
                             'data\penguin\Reload\Armature_RELOAD_24.png',
                             'data\penguin\Reload\Armature_RELOAD_25.png',
                             'data\penguin\Reload\Armature_RELOAD_26.png',
                             'data\penguin\Reload\Armature_RELOAD_27.png',
                             'data\penguin\Reload\Armature_RELOAD_28.png',
                             'data\penguin\Reload\Armature_RELOAD_29.png',
                             'data\penguin\Reload\Armature_RELOAD_30.png',
                             'data\penguin\Reload\Armature_RELOAD_31.png',
                             'data\penguin\Reload\Armature_RELOAD_32.png',
                             'data\penguin\Reload\Armature_RELOAD_33.png',
                             'data\penguin\Reload\Armature_RELOAD_34.png',
                             'data\penguin\Reload\Armature_RELOAD_35.png',
                             'data\penguin\Reload\Armature_RELOAD_36.png',
                             'data\penguin\Reload\Armature_RELOAD_37.png',
                             'data\penguin\Reload\Armature_RELOAD_38.png',
                             'data\penguin\Reload\Armature_RELOAD_39.png',
                             'data\penguin\Reload\Armature_RELOAD_40.png']

        self.frame_death = ['data\penguin\Death\Armature_DEAD_00.png',
                            'data\penguin\Death\Armature_DEAD_01.png',                   
                            'data\penguin\Death\Armature_DEAD_02.png',
                            'data\penguin\Death\Armature_DEAD_03.png',
                            'data\penguin\Death\Armature_DEAD_04.png',
                            'data\penguin\Death\Armature_DEAD_05.png',
                            'data\penguin\Death\Armature_DEAD_06.png',
                            'data\penguin\Death\Armature_DEAD_07.png',
                            'data\penguin\Death\Armature_DEAD_08.png',
                            'data\penguin\Death\Armature_DEAD_09.png',
                            'data\penguin\Death\Armature_DEAD_10.png',
                            'data\penguin\Death\Armature_DEAD_11.png',
                            'data\penguin\Death\Armature_DEAD_12.png',
                            'data\penguin\Death\Armature_DEAD_13.png',
                            'data\penguin\Death\Armature_DEAD_14.png',
                            'data\penguin\Death\Armature_DEAD_15.png',
                            'data\penguin\Death\Armature_DEAD_16.png',
                            'data\penguin\Death\Armature_DEAD_17.png',
                            'data\penguin\Death\Armature_DEAD_18.png',
                            'data\penguin\Death\Armature_DEAD_19.png',
                            'data\penguin\Death\Armature_DEAD_20.png',
                            'data\penguin\Death\Armature_DEAD_21.png',
                            'data\penguin\Death\Armature_DEAD_22.png',
                            'data\penguin\Death\Armature_DEAD_23.png',
                            'data\penguin\Death\Armature_DEAD_24.png',
                            'data\penguin\Death\Armature_DEAD_25.png',
                            'data\penguin\Death\Armature_DEAD_26.png',
                            'data\penguin\Death\Armature_DEAD_27.png',
                            'data\penguin\Death\Armature_DEAD_28.png',
                            'data\penguin\Death\Armature_DEAD_29.png',
                            'data\penguin\Death\Armature_DEAD_30.png',
                            'data\penguin\Death\Armature_DEAD_31.png',
                            'data\penguin\Death\Armature_DEAD_32.png']

        self.image = pygame.transform.scale(load_image(self.frame[self.count]), (90, 90))
        self.image = pygame.transform.flip(self.image, True, False)
      
        self.rect = self.image.get_rect()
        self.action = 'shot'
        self.pos = True
        self.health = 5
        self.res_count = 0
        self.gun_cartridges = 10
        self.rect.x = x
        self.rect.y = y
        self.restart_timer()
        

        
    def update(self, action, count):
        if self.count > count[0]:
            self.count = 0
        self.count += 1
        self.res_count = math.floor(self.count / count[1])
        if action == 'idle':
            self.image = pygame.transform.scale(load_image(self.frame[self.res_count]), (90, 90))
        elif action == 'shot':
            self.image = pygame.transform.scale(load_image(self.frame_attack[self.res_count]), (130, 90))
        elif action == 'death':
            self.image = pygame.transform.scale(load_image(self.frame_death[self.res_count]), (130, 90))
        elif action == 'reload':
            self.image = pygame.transform.scale(load_image(self.frame_reload[self.res_count]), (90, 90))
        elif action == 'hurt':
            self.image = pygame.transform.scale(load_image(self.frame_hurt[self.res_count]), (90, 90))
        self.image = pygame.transform.flip(self.image, True, False)

        self.acction = action
    
    def restart_timer(self):
        self.start_ticks = pygame.time.get_ticks()
    def timer(self):
        self.seconds = (pygame.time.get_ticks()-self.start_ticks) / 1000
        return self.seconds

#------------------------------------------------------------------------------------------------ Главное меню и экран окончания        
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
    
def menu():
    
    global fontmenu, menuscreen, startbuttonmenu, exitbuttonmenu

    fontmenu = pygame.font.Font(None, 50)
    menuscreen = pygame.display.set_mode([1000, 600])

    starttext = fontmenu.render('START', True, (130, 100, 150))
    exittext = fontmenu.render('EXIT', True, (130, 100, 150))

    pic = pygame.image.load('C:\\Users\\арп\\Desktop\\GeekBrains\\основное\\дз\\game_try\\menu.jpg')
    menuscreen.blit(pic, (0, 0))

    startbuttonmenu = pygame.draw.rect(screen, (128, 128, 128), (400, 383, 199, 51), 5)
    exitbuttonmenu = pygame.draw.rect(screen, (128, 128, 128), (400, 483, 199, 51), 5)

    menuscreen.blit(starttext, (444 ,394))
    menuscreen.blit(exittext, (457, 494))
#--------------------------------------------------------------------------------------------------




class Player(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.count = 0
        self.image = pygame.Surface((90,90))
        self.frame = ['data\penguin\Idle\Armature_IDLE_00.png',
                      'data\penguin\Idle\Armature_IDLE_01.png',
                      'data\penguin\Idle\Armature_IDLE_02.png',
                      'data\penguin\Idle\Armature_IDLE_03.png', 
                      'data\penguin\Idle\Armature_IDLE_04.png',
                      'data\penguin\Idle\Armature_IDLE_05.png',
                      'data\penguin\Idle\Armature_IDLE_06.png',
                      'data\penguin\Idle\Armature_IDLE_07.png',
                      'data\penguin\Idle\Armature_IDLE_08.png',
                      'data\penguin\Idle\Armature_IDLE_09.png',
                      'data\penguin\Idle\Armature_IDLE_10.png',
                      'data\penguin\Idle\Armature_IDLE_11.png',
                      'data\penguin\Idle\Armature_IDLE_12.png',
                      'data\penguin\Idle\Armature_IDLE_13.png',
                      'data\penguin\Idle\Armature_IDLE_14.png',
                      'data\penguin\Idle\Armature_IDLE_15.png',
                      'data\penguin\Idle\Armature_IDLE_16.png',
                      'data\penguin\Idle\Armature_IDLE_17.png',
                      'data\penguin\Idle\Armature_IDLE_18.png',
                      'data\penguin\Idle\Armature_IDLE_19.png',
                      'data\penguin\Idle\Armature_IDLE_20.png',
                      'data\penguin\Idle\Armature_IDLE_21.png',
                      'data\penguin\Idle\Armature_IDLE_22.png',
                      'data\penguin\Idle\Armature_IDLE_23.png',
                      'data\penguin\Idle\Armature_IDLE_24.png',
                      'data\penguin\Idle\Armature_IDLE_25.png',
                      'data\penguin\Idle\Armature_IDLE_26.png',
                      'data\penguin\Idle\Armature_IDLE_27.png',
                      'data\penguin\Idle\Armature_IDLE_28.png',
                      'data\penguin\Idle\Armature_IDLE_29.png',
                      'data\penguin\Idle\Armature_IDLE_31.png',
                      'data\penguin\Idle\Armature_IDLE_32.png',
                      'data\penguin\Idle\Armature_IDLE_33.png',
                      'data\penguin\Idle\Armature_IDLE_34.png',
                      'data\penguin\Idle\Armature_IDLE_35.png',
                      'data\penguin\Idle\Armature_IDLE_36.png',
                      'data\penguin\Idle\Armature_IDLE_37.png',
                      'data\penguin\Idle\Armature_IDLE_38.png',
                      'data\penguin\Idle\Armature_IDLE_40.png']

        self.frame_attack = ['data\penguin\Shot\Armature_SHOT_1_0.png',
                             'data\penguin\Shot\Armature_SHOT_1_1.png',       
                             'data\penguin\Shot\Armature_SHOT_1_2.png',      
                             'data\penguin\Shot\Armature_SHOT_1_3.png',           
                             'data\penguin\Shot\Armature_SHOT_1_4.png',       
                             'data\penguin\Shot\Armature_SHOT_1_5.png',        
                             'data\penguin\Shot\Armature_SHOT_1_6.png',        
                             'data\penguin\Shot\Armature_SHOT_1_7.png']

        self.frame_hurt = ['data\penguin\Hurt\Armature_HURT_0.png',
                           'data\penguin\Hurt\Armature_HURT_1.png',
                           'data\penguin\Hurt\Armature_HURT_2.png',
                           'data\penguin\Hurt\Armature_HURT_3.png',
                           'data\penguin\Hurt\Armature_HURT_4.png',
                           'data\penguin\Hurt\Armature_HURT_5.png',
                           'data\penguin\Hurt\Armature_HURT_6.png',
                           'data\penguin\Hurt\Armature_HURT_7.png']
        
        self.frame_reload = ['data\penguin\Reload\Armature_RELOAD_00.png',
                             'data\penguin\Reload\Armature_RELOAD_01.png',
                             'data\penguin\Reload\Armature_RELOAD_02.png',
                             'data\penguin\Reload\Armature_RELOAD_03.png',
                             'data\penguin\Reload\Armature_RELOAD_04.png',
                             'data\penguin\Reload\Armature_RELOAD_05.png',
                             'data\penguin\Reload\Armature_RELOAD_06.png',
                             'data\penguin\Reload\Armature_RELOAD_07.png',
                             'data\penguin\Reload\Armature_RELOAD_08.png',
                             'data\penguin\Reload\Armature_RELOAD_09.png',
                             'data\penguin\Reload\Armature_RELOAD_10.png',
                             'data\penguin\Reload\Armature_RELOAD_11.png',
                             'data\penguin\Reload\Armature_RELOAD_12.png',
                             'data\penguin\Reload\Armature_RELOAD_13.png',
                             'data\penguin\Reload\Armature_RELOAD_14.png',
                             'data\penguin\Reload\Armature_RELOAD_15.png',
                             'data\penguin\Reload\Armature_RELOAD_16.png',
                             'data\penguin\Reload\Armature_RELOAD_17.png',
                             'data\penguin\Reload\Armature_RELOAD_18.png',
                             'data\penguin\Reload\Armature_RELOAD_19.png',
                             'data\penguin\Reload\Armature_RELOAD_20.png',
                             'data\penguin\Reload\Armature_RELOAD_21.png',
                             'data\penguin\Reload\Armature_RELOAD_22.png',
                             'data\penguin\Reload\Armature_RELOAD_23.png',
                             'data\penguin\Reload\Armature_RELOAD_24.png',
                             'data\penguin\Reload\Armature_RELOAD_25.png',
                             'data\penguin\Reload\Armature_RELOAD_26.png',
                             'data\penguin\Reload\Armature_RELOAD_27.png',
                             'data\penguin\Reload\Armature_RELOAD_28.png',
                             'data\penguin\Reload\Armature_RELOAD_29.png',
                             'data\penguin\Reload\Armature_RELOAD_30.png',
                             'data\penguin\Reload\Armature_RELOAD_31.png',
                             'data\penguin\Reload\Armature_RELOAD_32.png',
                             'data\penguin\Reload\Armature_RELOAD_33.png',
                             'data\penguin\Reload\Armature_RELOAD_34.png',
                             'data\penguin\Reload\Armature_RELOAD_35.png',
                             'data\penguin\Reload\Armature_RELOAD_36.png',
                             'data\penguin\Reload\Armature_RELOAD_37.png',
                             'data\penguin\Reload\Armature_RELOAD_38.png',
                             'data\penguin\Reload\Armature_RELOAD_39.png',
                             'data\penguin\Reload\Armature_RELOAD_40.png']

        self.frame_death = ['data\penguin\Death\Armature_DEAD_00.png',
                            'data\penguin\Death\Armature_DEAD_01.png',                   
                            'data\penguin\Death\Armature_DEAD_02.png',
                            'data\penguin\Death\Armature_DEAD_03.png',
                            'data\penguin\Death\Armature_DEAD_04.png',
                            'data\penguin\Death\Armature_DEAD_05.png',
                            'data\penguin\Death\Armature_DEAD_06.png',
                            'data\penguin\Death\Armature_DEAD_07.png',
                            'data\penguin\Death\Armature_DEAD_08.png',
                            'data\penguin\Death\Armature_DEAD_09.png',
                            'data\penguin\Death\Armature_DEAD_10.png',
                            'data\penguin\Death\Armature_DEAD_11.png',
                            'data\penguin\Death\Armature_DEAD_12.png',
                            'data\penguin\Death\Armature_DEAD_13.png',
                            'data\penguin\Death\Armature_DEAD_14.png',
                            'data\penguin\Death\Armature_DEAD_15.png',
                            'data\penguin\Death\Armature_DEAD_16.png',
                            'data\penguin\Death\Armature_DEAD_17.png',
                            'data\penguin\Death\Armature_DEAD_18.png',
                            'data\penguin\Death\Armature_DEAD_19.png',
                            'data\penguin\Death\Armature_DEAD_20.png',
                            'data\penguin\Death\Armature_DEAD_21.png',
                            'data\penguin\Death\Armature_DEAD_22.png',
                            'data\penguin\Death\Armature_DEAD_23.png',
                            'data\penguin\Death\Armature_DEAD_24.png',
                            'data\penguin\Death\Armature_DEAD_25.png',
                            'data\penguin\Death\Armature_DEAD_26.png',
                            'data\penguin\Death\Armature_DEAD_27.png',
                            'data\penguin\Death\Armature_DEAD_28.png',
                            'data\penguin\Death\Armature_DEAD_29.png',
                            'data\penguin\Death\Armature_DEAD_30.png',
                            'data\penguin\Death\Armature_DEAD_31.png',
                            'data\penguin\Death\Armature_DEAD_32.png']

        self.frame_run = ['data\penguin\Run\Armature_RUN_00.png',
                          'data\penguin\Run\Armature_RUN_01.png',                                          
                          'data\penguin\Run\Armature_RUN_02.png',                                          
                          'data\penguin\Run\Armature_RUN_03.png',                                          
                          'data\penguin\Run\Armature_RUN_04.png',                                          
                          'data\penguin\Run\Armature_RUN_05.png',                                          
                          'data\penguin\Run\Armature_RUN_06.png',                                          
                          'data\penguin\Run\Armature_RUN_07.png',                                          
                          'data\penguin\Run\Armature_RUN_08.png',                                          
                          'data\penguin\Run\Armature_RUN_09.png',                                          
                          'data\penguin\Run\Armature_RUN_10.png',                                          
                          'data\penguin\Run\Armature_RUN_11.png',
                          'data\penguin\Run\Armature_RUN_12.png',
                          'data\penguin\Run\Armature_RUN_13.png',                                          
                          'data\penguin\Run\Armature_RUN_14.png',                                          
                          'data\penguin\Run\Armature_RUN_15.png']

        self.pers = pygame.transform.scale(load_image(self.frame[self.count]), (90, 90))
        # self.image.blit(self.pers, (0, 0))
        

        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.pos_x = 0
        self.pos_y = 0
        self.action = 'idle'
        self.pos = False
        self.res_count = 0
        self.gun_cartridges = 10
        self.health = 5
        self.coins = 0

        
    def update(self, action, count):
        self.image.fill((0, 0, 0))
        # if self.action != action:
        #     self.count = 0
        if self.count > count[0]:
            self.count = 0
        self.count += 1
        self.res_count = math.floor(self.count / count[1])
        if action == 'idle':
            self.pers = pygame.transform.scale(load_image(self.frame[self.res_count]), (90, 90))
        elif action == 'run':
            self.pers = pygame.transform.scale(load_image(self.frame_run[self.res_count]), (90, 90))
        elif action == 'shot':
            self.pers = pygame.transform.scale(load_image(self.frame_attack[self.res_count]), (130, 90))
        elif action == 'death':
            self.pers = pygame.transform.scale(load_image(self.frame_death[self.res_count]), (90, 90))
        elif action == 'reload':
            self.pers = pygame.transform.scale(load_image(self.frame_reload[self.res_count]), (90, 90))
        elif action == 'jump':
            self.pers = pygame.transform.scale(load_image(self.frame_jump[self.res_count]), (90, 90))
        elif action == 'hurt':
            self.pers = pygame.transform.scale(load_image(self.frame_hurt[self.res_count]), (90, 90))
        self.pers = pygame.transform.flip(self.pers, self.pos, False)
        # self.image.blit(self.pers, (0, 0))
       
        self.acction = action
    
    

def change_action(sprite, count, action):
    if sprite.count != count[0]:
        sprite.update(action, (count[0], count[1]))
        return False
    else:
        sprite.count = 0
        return True
        

class Earth(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.image = load_image('data\\grass.png',0)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        # world.blit(self.image, (pos[0], pos[1]))



world_group = pygame.sprite.Group()
def spawning():
    for i in range(len(map)):
        for z in range(len(map[i])):
            if map[i][z] == '.' or map[i][z] == 'P':
                _ = Earth(world_group, (z*90, i*90))
        



def s_bullet(bullet_group):
    for bullet in bullet_group:
        if bullet.count >= 50:
            bullet.kill()

def check_mask_bullet(group, bullet_group):
    for bullet in bullet_group:
        for sprite in group:
            if pygame.sprite.collide_mask(bullet, sprite):
                return [True, bullet, sprite]
    else: return [False]

def check_coin_mask(player, coins_group):
    for coin in coins_group:
        if pygame.sprite.collide_mask(coin, player):
            coin.kill()
            player.coins += 1


def check_s_enemy(enemy_group, player):
    for enemy in enemy_group:
        if abs(enemy.rect.x - (player.rect.x + 90)) <= 245:
            return [True, enemy]
    else: return [False, enemy]


def coin_draw(screen, coin):
    font = pygame.font.Font(None, 50)
    text = font.render(f'Coins: {coin}', True, 'black')
    text_rect = text.get_rect(center=(80, 60))
    screen.blit(text, text_rect)




pygame.init()
screen2 = pygame.Surface((3800, 1000))
screen3 = pygame.Surface((3800, 1000))

spawning()
world_group.draw(screen3)

size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
running = True


hero_group = pygame.sprite.Group()
player = Player(hero_group, 500, 300)

bullet_group = pygame.sprite.Group()
bullet_enemy_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()
_ = Enemy(enemy_group, 500, 300)

heart_group = pygame.sprite.Group()
heart = Heart(heart_group, screen)

coins_group = pygame.sprite.Group()


camera_pos = (0, 0)



attack = False
reload_gun = False
hurt = False
death = False



attack_enemy = False
idle_enemy = False
hurt_enemy = False
death_enemy = False

clock = pygame.time.Clock()


background = pygame.transform.scale(load_image('data\\background\\background.jpg'), (1000, 600))
player.pos_x, player.pos_y = 0, 0



while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    screen2.fill((0, 0, 0))
    screen2.blit(screen3, (0, 0))
    screen2.blit(player.pers, (player.rect.x, player.rect.y))
    screen.blit(screen2, (player.pos_x, player.pos_y))
    coin_draw(screen, player.coins)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            attack = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reload_gun = True


    check_coin_mask(player, coins_group)                
    if len(enemy_group.sprites()) > 0:

        result_mask_enemy = check_mask_bullet(enemy_group, bullet_group)
        if result_mask_enemy[0]:
            result_mask_enemy[1].kill()
            result_mask_enemy[2].health -= 1
            hurt_enemy = True
            if result_mask_enemy[2].health == 0:
                death_enemy = True


                
        check_enemy = check_s_enemy(enemy_group, player)
        attack_enemy = check_enemy[0]

        if hurt_enemy:
            if change_action(check_enemy[1], (14, 2), 'hurt'):
                hurt_enemy = False
        
        elif death_enemy:
            if change_action(check_enemy[1], (32, 1), 'death'):
                hurt_enemy = False
                check_enemy[1].kill()
                # _ = Coins(coins_group, load_image('data\coin\GoldCoinSpinning.png'), 24, check_enemy[1].rect.x, check_enemy[1].rect.y - 30)
                heart.coord_list.append(heart.coord_list[-1] * 30 + 10)

        elif attack_enemy == True:
            check_enemy[1].timer()
            if check_enemy[1].seconds > 1:
                check_enemy[1].rect.x = 460
                if change_action(check_enemy[1], (14, 2), 'shot'):
                    check_enemy[1].restart_timer()
                    _ = Bullet(bullet_enemy_group, load_image('data\\bullet\FireBullet.png'), 4, check_enemy[1].rect.x, check_enemy[1].rect.y, True)
            else: 
                change_action(check_enemy[1], (76, 2), 'idle')
                check_enemy[1].rect.x = 500
            
        else: 
            change_action(check_enemy[1], (76, 2), 'idle')
            attack_enemy = False


    result_mask_player = check_mask_bullet(hero_group, bullet_enemy_group)
    if result_mask_player[0] == True :
        result_mask_player[1].kill()
        player.health -= 1
        heart.coord_list.remove(heart.coord_list[-1])
        hurt = True 
        if player.health == 0:
            death = True


    keys = pygame.key.get_pressed()
    if attack and player.gun_cartridges > 0:
        if change_action(player, (14, 2), 'shot'):
            player.gun_cartridges -= 1
            _ = Bullet(bullet_group, load_image('data\\bullet\FireBullet.png'), 4, player.rect.x, player.rect.y, False)
            attack = False
    
    elif hurt:
        if change_action(player, (14, 2), 'hurt'):
            hurt = False

    elif death:
        if change_action(player, (32, 1), 'death'):
            death = False
            player.kill()
    
  
    elif reload_gun:
        if change_action(player, (80, 2), 'reload'):
            player.gun_cartridges = 10
            reload_gun = False

    elif keys[pygame.K_d]:
        player.pos = False
        player.update('run', (28, 2))
        player.rect.x += 3
        player.pos_x -= 3


    elif keys[pygame.K_a]:
        
        player.pos = True
        player.update('run', (28, 2))
        player.rect.x -= 3
        player.pos_x += 3

    else:
        if change_action(player, (76, 2), 'idle'):
            player.count = 0


    if keys[pygame.K_w]:
        player.rect.y -= 3
        player.pos_y += 3

    elif keys[pygame.K_s]:
        player.rect.y += 3
        player.pos_y -= 3

    # s_bullet(bullet_group)

    # enemy_group.draw(screen)

    bullet_group.update()
    # bullet_enemy_group.update()

    bullet_group.draw(screen)  
    # bullet_enemy_group.draw(screen)

    hero_group.draw(player.image)
    

    coins_group.draw(screen)
    coins_group.update()

    heart_group.update()

    

    pygame.display.flip()

pygame.quit() 
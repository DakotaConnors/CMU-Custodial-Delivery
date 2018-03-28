import pygame

class button():
    #buttons
    def __init__(self, location, size, pic):
        self.location = location
        self.size = size
        self.pic = pic

    def checkCollision(self, click): #checking if the button was clicked on
        if (click[0] >= self.location[0]) & (click[0] <= (self.location[0] + self.size[0])):
            if (click[1] >= self.location[1]) & (click[1] <= (self.location[1] + self.size[0])):
                return True
            else: return False
        else: return False

class textBox():
    #textbox
    def __init__(self):
        self.cursor = pygame.image.load("Pictures\Cursor.png")
        self.location = 0,0
        self.visible = True
        self.inUse = False
        self.timer = 500
        self.text = ''

    def checkTimer(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 500
            if self.visible: self.visible = False
            elif not(self.visible): self.visible = True
    #text_width, text_height = self.font.size("txt")
    def whichKey(self, key):
        if key == pygame.K_a: return 'a'
        elif key == pygame.K_b: return 'b'
        elif key == pygame.K_c: return 'c'
        elif key == pygame.K_d: return 'd'
        elif key == pygame.K_e: return 'e'
        elif key == pygame.K_f: return 'f'
        elif key == pygame.K_g: return 'g'
        elif key == pygame.K_h: return 'h'
        elif key == pygame.K_i: return 'i'
        elif key == pygame.K_j: return 'j'
        elif key == pygame.K_k: return 'k'
        elif key == pygame.K_l: return 'l'
        elif key == pygame.K_m: return 'm'
        elif key == pygame.K_n: return 'n'
        elif key == pygame.K_o: return 'o'
        elif key == pygame.K_p: return 'p'
        elif key == pygame.K_q: return 'q'
        elif key == pygame.K_r: return 'r'
        elif key == pygame.K_s: return 's'
        elif key == pygame.K_t: return 't'
        elif key == pygame.K_u: return 'u'
        elif key == pygame.K_v: return 'v'
        elif key == pygame.K_w: return 'w'
        elif key == pygame.K_x: return 'x'
        elif key == pygame.K_y: return 'y'
        elif key == pygame.K_z: return 'z'
        elif key == pygame.K_0: return '0'
        elif key == pygame.K_1: return '1'
        elif key == pygame.K_2: return '2'
        elif key == pygame.K_3: return '3'
        elif key == pygame.K_4: return '4'
        elif key == pygame.K_5: return '5'
        elif key == pygame.K_6: return '6'
        elif key == pygame.K_7: return '7'
        elif key == pygame.K_8: return '8'
        elif key == pygame.K_9: return '9'
        elif key == pygame.K_SPACE: return ' '
        elif key == pygame.K_BACKSPACE: return 'BACKSPACE'
        elif key == pygame.K_LSHIFT or key == pygame.K_RSHIFT: return 'SHIFT'
        elif key == pygame.K_KP_ENTER: return 'LOAD'
        elif key == pygame.K_KP_PLUS: return 'SAVE'
        elif key == pygame.K_UP: return 'UP'
        elif key == pygame.K_DOWN: return 'DOWN'
        else: return ''

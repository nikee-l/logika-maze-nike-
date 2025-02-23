from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y): 
        super().__init__()
        self.image=transform.scale(image.load(picture),(w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed





window_width = 700
window_height = 500
display.set_caption("Лабіринт")
window = display.set_mode((window_width, window_height))

run = True
wall_1 = GameSprite('assets\\wall.png',80,180,200,250)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((150, 240, 200))
    wall_1.reset()
    display.update()

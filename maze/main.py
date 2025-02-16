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
        



window_width = 700
window_height = 500
display.set_caption("Лабіринт")
window = display.set_mode((window_width, window_height))

run = True
wall_1 = GameSprite('assets/wall.png',80,180,200,250)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((150, 240, 200))
    wall_1.reset()
    display.update()

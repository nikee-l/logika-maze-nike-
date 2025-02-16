from pygame import*

display.set_caption('Моя первая игра')
window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))

run = True 
while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
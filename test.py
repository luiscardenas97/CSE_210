from pickle import REDUCE
from pyray import *
from raylib import ImageDrawRectangle, LoadImage
init_window(800, 450, "Cool Beans")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    
    x = 50
    for _ in range(200):

        draw_text("Cool beans!", 200, 175, 75, VIOLET)

        draw_circle(x,50,50, RED)
        draw_circle(x,400,50, RED)
        x += 50

    y = 100 
    for _ in range(200):

        draw_circle_gradient(y, 50, 50, BLUE, GREEN)
        draw_circle_gradient(y, 400, 50, BLUE, GREEN)
        y += 100
    
    
    end_drawing()

z = load_image("download (3).png")

image_draw_rectangle(z, 100, 100, 500, 500, WHITE)

close_window()
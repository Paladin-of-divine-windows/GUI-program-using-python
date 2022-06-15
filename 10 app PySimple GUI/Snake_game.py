from re import I
from time import time
import PySimpleGUI as sg
from random import randint

def convert_position_to_pixel(cell):
    tl = cell[0]*CELL_SIZE, cell[1]*CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br
def place_apple():
    apple_pos = randint(0,CELL_NUM-1), randint(0,CELL_NUM-1)
    while apple_pos in snake_body:
      apple_pos = randint(0,CELL_NUM-1), randint(0,CELL_NUM-1)
    return apple_pos  

# Game constants
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE/CELL_NUM

snake_body = [(4,4),(3,4),(2,4)]
DIRECTION = {'left':(-1,0), 'right':(1,0), 'up':(0,1), 'down':(0,-1)}
direction = DIRECTION['up']
# apple
apple_pos = (2,4)
apple_eaten = False

sg.theme('Green')
field = sg.Graph(
    canvas_size= (FIELD_SIZE,FIELD_SIZE),
    graph_bottom_left=(0,0),
    graph_top_right=(FIELD_SIZE,FIELD_SIZE),
    background_color='black')
layout = [[field]]

window = sg.Window('Snake_game', layout, return_keyboard_events=True)

star_time = time()
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    if event =='Left:37':
        direction = DIRECTION['left']
    if event =='Up:38':
        direction = DIRECTION['up']
    if event =='Right:39':
        direction = DIRECTION['right']
    if event =='Down:40':
        direction = DIRECTION['down']

    time_since_start = time() - star_time
    if time_since_start >= 0.5:
        star_time = time()    

        # apple snake colsion
        if snake_body[0] == apple_pos:
            apple_pos = place_apple()
            apple_eaten = True

        # Snake updated
        new_head = (snake_body[0][0] + direction[0], snake_body[0][1] + direction[1])
        snake_body.insert(0,new_head)
               
        if not apple_eaten:
            snake_body.pop()
        apple_eaten = False

        # check death
        if not 0 <= snake_body[0][0] <= CELL_NUM-1 or\
            not 0 <= snake_body[0][1] <= CELL_NUM-1 or \
            snake_body[0] in snake_body[1:]:
            break

        field.DrawRectangle((0,0),(FIELD_SIZE,FIELD_SIZE), 'black')

        tl, br = convert_position_to_pixel(apple_pos)
        field.DrawRectangle(tl,br, 'red')
        
        # draw snake
        for index, part in enumerate(snake_body):
            tl, br = convert_position_to_pixel(part)
            color = 'yellow' if index == 0 else 'green'
            field.draw_rectangle(tl, br, color)

window.close()
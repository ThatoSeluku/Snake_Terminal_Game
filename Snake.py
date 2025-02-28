from tkinter import * 
import random
#Game constants 
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3 
SNAKE_COLOR= "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"




class Snake:
        pass 

class Food:
        def __init__(self):
              
                x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
                y  = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
                
                self.coordinates = [x, y]

                canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

#Creation of game functions 
def next_turn():
        pass

def change_direction():
        pass

def check_collisions():
         pass
 
def game_over():
        pass

window = Tk()
window.title("Snake 2025")
window.resizable(False, False)


score = 0;
direction = 'down'

label = Label(window, text = "Score: {}".format(score), font=('consolas', 40 ))
label.pack()

canvas = Canvas(window, bg= BACKGROUND_COLOR, height= GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#x and y variables casted as they cannot be floats:
#Window is set to be in the center of your screen
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

#Set geometry:
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Create snake and food objects:
snake = Snake()
food = Food()


window.mainloop()
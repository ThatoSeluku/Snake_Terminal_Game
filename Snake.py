from tkinter import * 
import random

# Game constants 
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3 
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
        def __init__(self):
                self.body_size = BODY_PARTS
                self.coordinates = []  # Fixed typo here
                self.squares = []

                for i in range(0, BODY_PARTS):
                        self.coordinates.append([0, 0])  # Fixed typo here

                for x, y in self.coordinates:  # Fixed typo here
                        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                        self.squares.append(square)

class Food:
        def __init__(self):
                x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
                y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
                self.coordinates = [x, y]

                canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Creation of game functions 
def next_turn(snake, food):
        # Initialise snake head coordinates
        x, y = snake.coordinates[0]  # Fixed typo here

        # Add snake movement logic:
        # Up and down only relate to y coordinate movement:
        if direction == "up":
                y -= SPACE_SIZE
        elif direction == "down":
                y += SPACE_SIZE
        # Left and right only relate to x coordinate movement:
        elif direction == "left":
                x -= SPACE_SIZE
        elif direction == "right":
                x += SPACE_SIZE




        # Update snake head coordinates after click:
        # 0 is the index x, and y are updated values selected by player
        snake.coordinates.insert(0, (x, y))
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

        snake.squares.insert(0, square)

        #Check colision with objects:
        if x == food.coordinates[0] and y == food.coordinates[1]:
                #Increment score:
                global score 
                score +=1
                label.config(text="Score: {}".format(score))

                #remove item post collision
                canvas.delete("food")
                food = Food()

        else: 
                del snake.coordinates[-1]
                canvas.delete(snake.squares[-1])
                del snake.squares[-1]
                

        # Call next turn recursively
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
        global direction

        #Check direction and make sure old direction doesn't cause an opposite turn: 
        if new_direction == 'left':
                if direction != 'right':
                        direction = new_direction
        elif new_direction == 'right':
                if direction != 'left':
                        direction = new_direction
        elif new_direction == 'up':
                if direction != 'down':
                        direction = new_direction
        elif new_direction == 'down':
                if direction != 'up':
                        direction = new_direction
                        
def check_collisions():
         pass
 
def game_over():
        pass

window = Tk()
window.title("Snake 2025")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# x and y variables casted as they cannot be floats:
# Window is set to be in the center of your screen
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Set geometry:
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#bind controls to keys on your keyboard using a lambda to change directions
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))



# Create snake and food objects:
snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()

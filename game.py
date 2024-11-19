import tkinter as tk

# Create the main game window
root = tk.Tk()
root.title("Ping Pong Game")
root.resizable(False, False)
root.geometry("600x400")

# Global variables
paddle_speed = 20
ball_speed_x = 4
ball_speed_y = 4
score = 0

# Canvas for the game
canvas = tk.Canvas(root, bg="black", width=600, height=400)
canvas.pack()

# Create paddle and ball
paddle = canvas.create_rectangle(250, 350, 350, 360, fill="white")
ball = canvas.create_oval(290, 290, 310, 310, fill="red")

# Score display
score_text = canvas.create_text(50, 20, text=f"Score: {score}", fill="white", font=("Arial", 16))

# Paddle movement
def move_left(event):
    x1, _, x2, _ = canvas.coords(paddle)
    if x1 > 0:
        canvas.move(paddle, -paddle_speed, 0)

def move_right(event):
    x1, _, x2, _ = canvas.coords(paddle)
    if x2 < 600:
        canvas.move(paddle, paddle_speed, 0)

# Bind arrow keys to paddle movement
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Ball movement and collision
def move_ball():
    global ball_speed_x, ball_speed_y, score

    # Move the ball
    canvas.move(ball, ball_speed_x, ball_speed_y)
    x1, y1, x2, y2 = canvas.coords(ball)

    # Ball collision with walls
    if x1 <= 0 or x2 >= 600:
        ball_speed_x = -ball_speed_x
    if y1 <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if y2 >= 350:
        paddle_coords = canvas.coords(paddle)
        if paddle_coords[0] <= x1 <= paddle_coords[2] or paddle_coords[0] <= x2 <= paddle_coords[2]:
            ball_speed_y = -ball_speed_y
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

    # Game over condition
    if y2 > 400:
        canvas.create_text(300, 200, text="Game Over", fill="red", font=("Arial", 24))
        return

    # Call move_ball() again after 20ms
    root.after(20, move_ball)

# Start the game
move_ball()

# Run the main loop
root.mainloop()

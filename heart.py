# Heart.py
# Import required libraries
import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 800)  # Set screen size to 800x800 pixels
screen.bgcolor("#FFE6F0")  # Set background color to light pink

# Create a turtle object and set its properties
heart = turtle.Turtle()
heart.hideturtle()  # Hide the turtle cursor
heart.speed(0)  # 0 is the fastest speed
# Define a function to draw a heart
def draw_heart(x, y, size, color, thickness):
    heart.penup()  # Lift the pen to move without drawing
    heart.goto(x, y)  # Move to the starting position
    heart.color(color)  # Set the heart color
    heart.pensize(thickness)  # Set the line thickness
    heart.pendown()  # Put the pen down to start drawing
    heart.begin_fill()  # Start filling the shape
    heart.left(140)  # Turn left 140 degrees
    heart.forward(size)  # Draw the first line of the heart
   
    # Draw the left curve of the heart
    for _ in range(100):  # Reduced from 200
        heart.right(2)  # Increased from 1
        heart.forward(size * 0.018)  # Doubled from 0.009
   
    heart.left(120)  # Turn left to prepare for the right curve
   
    # Draw the right curve of the heart
    for _ in range(100):  # Reduced from 200
        heart.right(2)  # Increased from 1
        heart.forward(size * 0.018)  # Doubled from 0.009
   
    heart.forward(size)  # Draw the final line of the heart
    heart.end_fill()  # End filling the shape
    heart.setheading(0)  # Reset the turtle's heading to 0 degrees (facing right)

# Define a list of hearts with their properties
hearts = [
    (0, -150, 300, "#FF1493", 5),  # Deep Pink
    (0, -135, 270, "#FF69B4", 5),  # Hot Pink
    (0, -120, 240, "#FF6347", 5),  # Tomato
    (0, -105, 210, "#FF4500", 5),  # Orange Red
    (0, -90, 180, "#FF8C00", 5),   # Dark Orange
    (0, -75, 150, "#FFA500", 5),   # Orange
    (0, -50, 100, "#FFD700", 5)    # Gold
]

# Loop through the hearts list and draw each heart
for heart_params in hearts:
    draw_heart(*heart_params)  # Unpack the tuple and pass as arguments to draw_heart
    # time.sleep(0.5)  # Comment out or remove this line

screen.mainloop() # Keep the screen open 

screen.tracer(0)  # Turn off animation

screen.update()  # Update the screen once all hearts are drawn

import turtle
import math

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("3D-Like Helix Animation")

helix_turtle = turtle.Turtle()
helix_turtle.speed(0.001)

# Function to draw a 3D-like helix
def draw_3d_helix(radius, angle_increment, depth_increment, num_rotations, num_layers):
    for layer in range(num_layers):
        for _ in range(int(360 * num_rotations / angle_increment)):
            radian_angle = math.radians(angle_increment)
            x = radius * math.cos(radian_angle)
            y = radius * math.sin(radian_angle)
            z = layer * depth_increment

            helix_turtle.goto(x, y - z)
            helix_turtle.dot(5, "blue")  # You can customize the dot size and color

            angle_increment += 1

# Set parameters for the 3D-like helix
helix_radius = 10
helix_angle_increment = 5
helix_depth_increment = 1
helix_rotations = 5
helix_layers = 10

# Draw the 3D-like helix
draw_3d_helix(helix_radius, helix_angle_increment, helix_depth_increment, helix_rotations, helix_layers)

# Hide the turtle and display the window
helix_turtle.hideturtle()
screen.mainloop()

import random
import math

# Generate a random angle in degrees
angle_degrees = random.uniform(0, 360)

# Convert the angle to radians
angle_radians = math.radians(angle_degrees)

# Calculate trigonometric values
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

# Prepare the output
output = {
    "angle_degrees": angle_degrees,
    "sin": sin_value,
    "cos": cos_value,
    "tan": tan_value
}

print(output)
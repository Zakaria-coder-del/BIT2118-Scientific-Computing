import numpy as np

print("FLOOR PLAN MATRIX TRANSFORMATION")

# Four corners of a room measuring 4m by 3m
points = np.array([
    [0.0, 0.0],
    [4.0, 0.0],
    [4.0, 3.0],
    [0.0, 3.0]
])

# Rotate the floor plan by 30 degrees
angle = np.deg2rad(30)

rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Reduce the drawing to half its original size
scale = np.array([
    [0.5, 0.0],
    [0.0, 0.5]
])

# Combine rotation and scaling
transformation = rotation @ scale

# Transform all four corners
transformed_points = points @ transformation.T

print("\nOriginal points:")
print(points)

print("\nTransformation matrix:")
print(np.round(transformation, 4))

print("\nTransformed points:")
print(np.round(transformed_points, 4))

# Calculate determinant
determinant = np.linalg.det(transformation)

print("\nDeterminant:", round(determinant, 4))

# Change rotation angle from 30 to 45 degrees
new_angle = np.deg2rad(45)

new_rotation = np.array([
    [np.cos(new_angle), -np.sin(new_angle)],
    [np.sin(new_angle), np.cos(new_angle)]
])

new_transformation = new_rotation @ scale
new_points = points @ new_transformation.T

print("\nAFTER CHANGING ANGLE TO 45 DEGREES:")
print(np.round(new_points, 4))
print("New determinant:", round(np.linalg.det(new_transformation), 4))
import numpy as np
import math

def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def rotation_matrix(angle_degrees):
    theta = math.radians(angle_degrees)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    return np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta,  cos_theta, 0],
        [0,         0,          1]
    ])

def scaling_matrix(sx, sy):
    return np.array([
        [sx, 0,  0],
        [0, sy,  0],
        [0,  0,  1]
    ])

# === User Inputs ===
tx = float(input("Enter translation in x (tx): "))
ty = float(input("Enter translation in y (ty): "))

angle = float(input("Enter rotation angle in degrees: "))

sx = float(input("Enter scaling in x (sx): "))
sy = float(input("Enter scaling in y (sy): "))

# === Display Matrices ===
print("\n--- Translation Matrix ---")
print(translation_matrix(tx, ty))

print("\n--- Rotation Matrix ---")
print(rotation_matrix(angle))

print("\n--- Scaling Matrix ---")
print(scaling_matrix(sx, sy))

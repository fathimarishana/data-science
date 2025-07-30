import numpy as np
import math

# a) Translation Matrix
def translation_matrix(tx, ty, tz):
    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

# b) Rotation Matrices
def rotation_matrix_x(angle_deg):
    angle_rad = math.radians(angle_deg)
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(angle_rad), -math.sin(angle_rad), 0],
        [0, math.sin(angle_rad),  math.cos(angle_rad), 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_y(angle_deg):
    angle_rad = math.radians(angle_deg)
    return np.array([
        [math.cos(angle_rad), 0, math.sin(angle_rad), 0],
        [0, 1, 0, 0],
        [-math.sin(angle_rad), 0, math.cos(angle_rad), 0],
        [0, 0, 0, 1]
    ])

def rotation_matrix_z(angle_deg):
    angle_rad = math.radians(angle_deg)
    return np.array([
        [math.cos(angle_rad), -math.sin(angle_rad), 0, 0],
        [math.sin(angle_rad),  math.cos(angle_rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

# c) Scaling Matrix
def scaling_matrix(sx, sy, sz):
    return np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Display function
def print_matrix(name, mat):
    print(f"\n{name}:\n{mat}")

# Main function
def main():
    print("Enter Translation Values:")
    tx = get_float_input("tx: ")
    ty = get_float_input("ty: ")
    tz = get_float_input("tz: ")

    print("\nEnter Scaling Values:")
    sx = get_float_input("sx: ")
    sy = get_float_input("sy: ")
    sz = get_float_input("sz: ")

    print("\nEnter Rotation Angle (in degrees):")
    angle = get_float_input("Angle: ")

    print_matrix("Translation Matrix", translation_matrix(tx, ty, tz))
    print_matrix("Scaling Matrix", scaling_matrix(sx, sy, sz))
    print_matrix("Rotation Matrix around X-axis", rotation_matrix_x(angle))
    print_matrix("Rotation Matrix around Y-axis", rotation_matrix_y(angle))
    print_matrix("Rotation Matrix around Z-axis", rotation_matrix_z(angle))

if __name__ == "__main__":
    main()

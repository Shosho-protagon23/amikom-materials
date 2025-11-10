import math
import time
import os

def rotate_point(point, angle_x, angle_y, angle_z):
    # Rotation around X axis
    x1 = point[0]
    y1 = point[1] * math.cos(angle_x) - point[2] * math.sin(angle_x)
    z1 = point[1] * math.sin(angle_x) + point[2] * math.cos(angle_x)
    
    # Rotation around Y axis
    x2 = x1 * math.cos(angle_y) + z1 * math.sin(angle_y)
    y2 = y1
    z2 = -x1 * math.sin(angle_y) + z1 * math.cos(angle_y)
    
    # Rotation around Z axis
    x3 = x2 * math.cos(angle_z) - y2 * math.sin(angle_z)
    y3 = x2 * math.sin(angle_z) + y2 * math.cos(angle_z)
    z3 = z2
    
    return [x3, y3, z3]

def project(point, distance):
    # Simple perspective projection
    factor = distance / (distance + point[2])
    x = int(point[0] * factor * 10 + 40)  # Scale and offset for screen
    y = int(point[1] * factor * 10 + 20)
    return [x, y]

def draw_cube(angle_x, angle_y, angle_z):
    cube = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Back face
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # Front face
    ]
    
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
        (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
    ]
    
    rotated = []
    for point in cube:
        rotated.append(rotate_point(point, angle_x, angle_y, angle_z))
    
    projected = []
    for point in rotated:
        projected.append(project(point, 5))  # Distance from camera
    
    # Create a grid for display
    width = 80
    height = 40
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Draw edges
    for edge in edges:
        start = projected[edge[0]]
        end = projected[edge[1]]
        dx = abs(end[0] - start[0])
        dy = abs(end[1] - start[1])
        sx = 1 if start[0] < end[0] else -1
        sy = 1 if start[1] < end[1] else -1
        err = dx - dy
        
        x, y = start[0], start[1]
        while True:
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = '*'
            if x == end[0] and y == end[1]:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
    
    # Print the grid
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(''.join(row))

def main():
    angle = 0
    while True:
        draw_cube(angle * 0.05, angle * 0.05, angle * 0.05)
        time.sleep(0.1)
        angle += 1

if __name__ == "__main__":
    main()
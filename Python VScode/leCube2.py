import tkinter as tk
import math
import time

class RotatingCubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ASCII SPINNING LeCUBE :)")
        self.text_widget = tk.Text(self.root,
                                   font=("Courier", 10),
                                   bg="black", fg="white")
        self.text_widget.pack()

        ## LeCUBE's parameters
        self.cube_size = 10
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        ## Vertices of LeCUBE
        self.vertices = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ]

        ## Edges of LeCUBE
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        self.animate()

    def rotate(self, point, angle_x, angle_y, angle_z):
        x, y, z = point

        # Rotasi sekitar X-axis
        cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
        y, z = y * cos_x - z * sin_x, y * sin_x + z * cos_x

        # Rotasi sekitar Y-axis
        cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
        x, z = x * cos_y + z * sin_y, -x * sin_y + z * cos_y

        # Rotasi sekitar Z-axis
        cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)
        x, y = x * cos_z - y * sin_z, x * sin_z + y * cos_z

        return x, y, z
    
    def project(self, point):
        x, y, z = point

        # Perspektif Projeksi nya
        factor = 200 / (z + 5)
        return int(x * factor + 40), int(y * factor + 20)
    
    def draw_cube(self):
        rotated_vertices = [
            self.rotate(v, self.angle_x, self.angle_y, self.angle_z) for v in self.vertices
        ]
        projected_vertices = [
            self.project(v) for v in rotated_vertices
        ]

        # Buat grid
        grid = [[' ' for _ in range(80)] for _ in range(40)]

        # Buat edges
        for edge in self.edges:
            x1, y1 = projected_vertices[edge[0]]
            x2, y2 = projected_vertices[edge[1]]
            self.draw_line(grid, x1, y1, x2, y2)

        # Konversi ke string
        return '\n'.join(''.join(row) for row in grid)
    
    def draw_line(self, grid, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return
        x_inc = dx / steps
        y_inc = dy / steps
        x, y = x1, y1
        for _ in range(int(steps) + 1):
            if 0 <= int(y) < len(grid) and 0 <= int(x) < len(grid[0]):
                grid[int(y)][int(x)] = '*'
            x += x_inc
            y += y_inc

    def animate(self):
        self.angle_x += 0.05
        self.angle_y += 0.03
        self.angle_z += 0.07
        
        ascii_art = self.draw_cube()
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, ascii_art)
        
        self.root.after(100, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = RotatingCubeApp(root)
    root.mainloop()
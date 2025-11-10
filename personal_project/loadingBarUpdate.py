import tkinter as tk
from tkinter import ttk
import time
import math

def loading_screen_tkinter_with_cube(total_steps, delay=0.1):
    """
    Creates a graphical loading screen using Tkinter with a rotating cube animation,
    progress bar, and percentage.
    
    Args:
    - total_steps: Number of steps in the loading process.
    - delay: Time delay between each step (in seconds) to simulate loading.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Loading Screen")
    root.geometry("400x200")
    
    # Canvas for the rotating cube
    canvas = tk.Canvas(root, width=200, height=100, bg="white")
    canvas.pack(pady=10)
    
    # Label for percentage
    percent_label = tk.Label(root, text="0.0%", font=("Arial", 14))
    percent_label.pack(pady=5)
    
    # Progress bar
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=total_steps)
    progress.pack(pady=10)
    
    # Cube vertices (initial positions for a simple cube)
    vertices = [
        [-50, -50, -50], [50, -50, -50], [50, 50, -50], [-50, 50, -50],
        [-50, -50, 50], [50, -50, 50], [50, 50, 50], [-50, 50, 50]
    ]
    
    # Edges connecting vertices
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
        (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
    ]
    
    # Function to project 3D to 2D (simple orthographic projection)
    def project(x, y, z):
        return x + 100, y + 50  # Center on canvas
    
    # Function to rotate cube around Y-axis
    def rotate_y(vertices, angle):
        cos_a, sin_a = math.cos(angle), math.sin(angle)
        return [
            [x * cos_a - z * sin_a, y, x * sin_a + z * cos_a]
            for x, y, z in vertices
        ]
    
    # Function to draw the cube
    def draw_cube(angle):
        rotated = rotate_y(vertices, angle)
        projected = [project(x, y, z) for x, y, z in rotated]
        canvas.delete("all")
        for edge in edges:
            x1, y1 = projected[edge[0]]
            x2, y2 = projected[edge[1]]
            canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
    
    # Animation variables
    angle = 0
    animation_speed = 0.1  # Radians per frame
    
    # Function to update progress and animate cube
    def update_progress(step):
        nonlocal angle
        if step <= total_steps:
            progress['value'] = step
            percent = (step / total_steps) * 100
            percent_label.config(text=f"{percent:.1f}%")
            
            # Animate cube
            draw_cube(angle)
            angle += animation_speed
            
            root.after(int(delay * 1000), update_progress, step + 1)  # Schedule next update
        else:
            percent_label.config(text="Loading Complete!")
            canvas.delete("all")
            canvas.create_text(100, 50, text="Done!", font=("Arial", 20))
            root.after(2000, root.destroy)  # Close window after 2 seconds
    
    # Start the loading simulation
    update_progress(0)
    
    # Run the Tkinter event loop
    root.mainloop()

# Example usage
loading_screen_tkinter_with_cube(100)  # Simulates 100 steps of loading

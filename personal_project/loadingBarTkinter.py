import tkinter as tk
from tkinter import ttk
import time

def loading_screen_tkinter(total_steps, delay=0.1):
    """
    Creates a graphical loading screen using Tkinter with a progress bar and percentage.
    
    Args:
    - total_steps: Number of steps in the loading process.
    - delay: Time delay between each step (in seconds) to simulate loading.
    """
    # Create the main window
    root = tk.Tk()
    root.title("Loading Screen")
    root.geometry("400x150")
    
    # Label for percentage
    percent_label = tk.Label(root, text="0.0%", font=("Arial", 14))
    percent_label.pack(pady=10)
    
    # Progress bar
    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", maximum=total_steps)
    progress.pack(pady=10)
    
    # Function to update progress
    def update_progress(step):
        if step <= total_steps:
            progress['value'] = step
            percent = (step / total_steps) * 100
            percent_label.config(text=f"{percent:.1f}%")
            root.after(int(delay * 1000), update_progress, step + 1)  # Schedule next update
        else:
            percent_label.config(text="Loading Complete!")
            root.after(2000, root.destroy)  # Close window after 2 seconds
    
    # Start the loading simulation
    update_progress(0)
    
    # Run the Tkinter event loop
    root.mainloop()

# Example usage
loading_screen_tkinter(1000)  # Simulates amount of steps of loading

import time

def loading_screen(total_steps, delay=0.1):
    """
    Simulates a loading screen with a progress bar and percentage.
    
    Args:
    - total_steps: Number of steps in the loading process.
    - delay: Time delay between each step (in seconds) to simulate loading.
    """
    bar_length = 80  # Length of the progress bar
    
    for i in range(total_steps + 1):
        percent = (i / total_steps) * 100
        filled_length = int(bar_length * i // total_steps)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        # Print the bar and percentage, overwriting the line each time
        print(f'\r[{bar}] {percent:.1f}%', end='', flush=True)
        
        time.sleep(delay)  # Simulate loading time
    
    print()  # Move to a new line after completion

# Example usage
loading_screen(1500)  # Simulates 100 steps of loading

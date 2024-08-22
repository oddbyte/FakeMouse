import os
import sys
import pyautogui  # You need to install this library

# Function to send ADB shell commands for mouse movements
def move_mouse(dx, dy):
    # Convert dx and dy to 8-bit signed hex values (for HID)
    x_hex = f"\\\\x{(dx & 0xFF):02X}"  # Convert to 8-bit signed byte
    y_hex = f"\\\\x{(dy & 0xFF):02X}"

    # Construct the hex command to move the mouse relatively by dx, dy
    adb_command = f'adb shell sh /data/local/tmp/script.sh mouse "\\\\x00{x_hex}{y_hex}\\\\x00"'
    
    # Execute the command to simulate mouse movement
    os.system(adb_command)

# Function for --fast: move the mouse quickly by breaking large movements into smaller capped movements
def move_mouse_fast(target_x, target_y, cap=127):
    # Get the current mouse position from pyautogui
    current_x, current_y = pyautogui.position()

    # Calculate the total difference in X and Y
    x_diff = target_x - current_x
    y_diff = target_y - current_y

    # While there's still movement left to do
    while abs(x_diff) > 0 or abs(y_diff) > 0:
        # Cap the movement to fit within the HID device's limit (-127 to 127)
        x_step = max(min(x_diff, cap), -cap)
        y_step = max(min(y_diff, cap), -cap)

        # Move the mouse by the capped amount
        move_mouse(int(x_step), int(y_step))

        # Recalculate remaining distance after the movement
        current_x, current_y = pyautogui.position()
        x_diff = target_x - current_x
        y_diff = target_y - current_y

# Function for --step: attempt to move the mouse as far as possible in one event
def move_mouse_all_in_one(target_x, target_y):
    # Get the current mouse position from pyautogui
    current_x, current_y = pyautogui.position()

    # Calculate the total difference in X and Y
    x_diff = target_x - current_x
    y_diff = target_y - current_y

    # Cap dx and dy between -127 and 127 to prevent overflow but try to get as close as possible
    x_step = max(min(x_diff, 127), -127)
    y_step = max(min(y_diff, 127), -127)

    # Move the mouse by the calculated capped amount in a single event
    move_mouse(int(x_step), int(y_step))

# Function to move the mouse by small steps and check the new position after each step
def move_mouse_in_steps(target_x, target_y, tolerance=3, step_size=10):
    while True:
        # Get the current mouse position from pyautogui
        current_x, current_y = pyautogui.position()

        # Calculate the difference between the current position and the target
        x_diff = target_x - current_x
        y_diff = target_y - current_y

        # If we are within tolerance, stop moving
        if abs(x_diff) <= tolerance and abs(y_diff) <= tolerance:
            break

        # Calculate the step in each direction
        x_step = max(min(x_diff, step_size), -step_size)
        y_step = max(min(y_diff, step_size), -step_size)

        # Move the mouse by the calculated step
        move_mouse(int(x_step), int(y_step))

# Main script execution
if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Usage: python script.py <target_x> <target_y> [--fast | --step]")
        sys.exit(1)

    # Read target X and Y coordinates from command-line arguments
    target_x = int(sys.argv[1])
    target_y = int(sys.argv[2])

    # Check if the --fast or --step option is used
    if len(sys.argv) == 4 and sys.argv[3] == '--fast':
        # Move the mouse fast by breaking large movements into smaller capped movements
        move_mouse_fast(target_x, target_y)
    elif len(sys.argv) == 4 and sys.argv[3] == '--step':
        # Move the mouse in one event, trying to get as close as possible
        move_mouse_all_in_one(target_x, target_y)
    else:
        # Move the mouse step by step (default behavior)
        move_mouse_in_steps(target_x, target_y)

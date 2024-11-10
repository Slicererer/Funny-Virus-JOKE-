import ctypes
import os

SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = r"C:\Users\merce\OneDrive\Desktop\Noob\Noob2 (1).webp"  # Specify the path to your wallpaper image

# Function to change the wallpaper
def change_wallpaper(image_path):
    if os.path.exists(image_path):
        # Convert the image path to a string that ctypes can handle
        image_path = os.path.abspath(image_path)
        # Set the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
        print(f"Wallpaper changed to {image_path}")
    else:
        print("The image path does not exist.")

# Change wallpaper to the specified image
change_wallpaper(WALLPAPER_PATH)
import os
import platform
import time

def restart_computer():
    # Get the current operating system
    current_os = platform.system().lower()

    try:
        if current_os == 'windows':
            print("Restarting your computer...")
            # Execute restart command for Windows
            os.system("shutdown /r /f /t 0")
        elif current_os == 'linux' or current_os == 'darwin':  # Linux or macOS
            print("Restarting your computer...")
            # Execute restart command for Linux or macOS
            os.system("sudo reboot")
        else:
            print("Unsupported OS")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Give a short delay before restarting to alert the user
    print("This will restart your computer in 5 seconds. Save your work.")
    time.sleep(5)  # Wait for 5 seconds before restart
    restart_computer()

from PIL import ImageGrab
import time
import pyautogui
import keyboard

# Wait a few seconds before start
time.sleep(3)

MODE_PIXEL = (500, 200)
MODE_THRESHOLD = 100

start_time = time.time()

def detect_game_mode(image_data):
    # Check a pixel on screen
    pixel_value = image_data[MODE_PIXEL[0], MODE_PIXEL[1]]
    return "dark" if pixel_value < MODE_THRESHOLD else "light"

def get_dynamic_area():
    elapsed = time.time() - start_time
    # Dino jumps sooner as the game gets faster
    shift = min(int(elapsed // 10) * 10, 100)
    return ((775 + shift, 260), (835 + shift, 289))

def detect_obstacle(image_data, top_left, bottom_right, mode):
    # Check if an obstacle is near the dino
    for y in range(top_left[1], bottom_right[1]):
        for x in range(top_left[0], bottom_right[0]):
            pixel = image_data[x, y]
            if mode == "dark" and pixel > 170:
                return True
            if mode == "light" and pixel < 100:
                return True
    return False

while True:
    img = ImageGrab.grab().convert('L')
    data = img.load()

    mode = detect_game_mode(data)
    area = get_dynamic_area()
    if detect_obstacle(data, area[0], area[1], mode):
        pyautogui.press('up')
        time.sleep(0.1)

    # Press q to quit
    if keyboard.is_pressed('q'):
        break

    time.sleep(0.01)  # prevent 100% CPU usage
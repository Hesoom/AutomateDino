# AutomateDino

A simple Python script that plays the Chrome Dino game.

## Features
- Works in both light and dark mode
- Reacts faster as the game speeds up
- Press `Q` to quit

## Requirements
- Python 3+
- Install with:
  ```
  pip install pillow pyautogui keyboard
  ```

## How to Use
1. Open Chrome and go to `chrome://dino`
2. Start the game
3. Run the script
4. Watch it play

## ⚠️ Important Note
The detection area is based on **fixed screen coordinates**.

This means:
- It works only if your screen resolution, Chrome window size, and zoom level match the setup it was built for.
- If the bot doesn't detect obstacles correctly, you may need to adjust the coordinates manually in the script.

import tkinter as tk
import os

ENCRYPT_FILE_PATH = None
ENCRYPTION_KEY_PATH = None
NEW_ENC_KEY_PATH = None
ENCRYPTION_KEY = None

def init_variables(root):
    global ENCRYPT_FILE_PATH, ENCRYPTION_KEY_PATH, NEW_ENC_KEY_PATH, ENCRYPTION_KEY

    ENCRYPT_FILE_PATH = tk.StringVar(root, value="")
    ENCRYPTION_KEY_PATH = tk.StringVar(root, value="")
    NEW_ENC_KEY_PATH = tk.StringVar(root, value="")
    ENCRYPTION_KEY = tk.StringVar(root, value="")

COLUMN_WIDTH = 100
COLUMNS = 10
ROW_HEIGHT = 50
ROWS = 12
COLOR = "#E9EEF5"

logo_icon = os.path.join("images", "icon.png")
closed_padlock_icon = os.path.join("images", "padlock.png")
open_padlock_icon = os.path.join("images", "open.png")
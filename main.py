# region ====== Imports ======
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

import python_files.classes as cls
import python_files.functions as fc
import python_files.global_var as var
#endregion

# region ====== Ustawienia ======

root = tk.Tk()
root.title("File Encryptor")
root.geometry("1000x700")
root.configure(bg=var.COLOR)

var.init_variables(root) # Zmienne globalne trzeba zainicjalizowac dopiero po utworzeniu glownego okna

#endregion

# region - Kontener na zawartosci
container = tk.Frame(root, bg=var.COLOR)
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
#endregion

# region - Rozdzielenie podstron
main_page = tk.Frame(container, bg=var.COLOR)   #strona glowna
encrypt_page = tk.Frame(container, bg=var.COLOR)   #strona szyfrowania
decrypt_page = tk.Frame(container, bg=var.COLOR)   #strona odszyfrowywania

for box in (main_page, encrypt_page, decrypt_page):
    box.grid(row=0, column=0, sticky="nsew")
#endregion

# region ==== Strona 1 ======
def render_main_page():
    # Naglowek
    header = cls.Header(main_page, "𝖥𝗂𝗅𝖾 𝖤𝗇𝖼𝗋𝗒𝗉𝗍𝗈𝗋")
    header.pack(pady=10)

    frame = tk.Frame(main_page, bg='white', width=8 * var.COLUMN_WIDTH, height=10 * var.ROW_HEIGHT)
    frame.grid_propagate(False)
    frame.pack(pady=10)

    for i in range(2):
        frame.columnconfigure(i, weight=1)
        frame.rowconfigure(i, weight=1)

    #Przycisk szyfrowania
    enc_button = cls.Custom_Button("Encrypt file", frame, lambda: fc.show_frame(encrypt_page))
    enc_button.grid(row=0, column=0, sticky="s", pady=30)

    #Przycisk szyfrowania
    dec_button = cls.Custom_Button("Decrypt file", frame, lambda: fc.show_frame(decrypt_page))
    dec_button.grid(row=1, column=0, sticky="n", pady=30)

    #Obraz
    logo_image = Image.open(fc.resource_path(var.logo_icon))
    logo_image = logo_image.resize((3 * var.COLUMN_WIDTH, 6 * var.ROW_HEIGHT))
    image_object = ImageTk.PhotoImage(logo_image)

    image_label = tk.Label(frame, image=image_object, bg="white")
    image_label.image = image_object
    image_label.grid(row=0, column=1, columnspan=2, rowspan=2, sticky="ew")

    #Przycisk EXIT
    exit_button = cls.Back_Button("Exit", main_page, lambda: fc.exit(root))
    exit_button.pack(pady=15)
    #endregion

# region ==== Strona 2 ======
def render_encrypt_page():
    #====== Header ======
    header = cls.Header(encrypt_page, "​𝐄𝐧𝐜𝐫𝐲𝐩𝐭𝐢𝐨𝐧")
    header.pack(pady=10)

    #====== Bialy kontener ======
    frame = tk.Frame(encrypt_page, bg='white', width=8 * var.COLUMN_WIDTH, height=10 * var.ROW_HEIGHT)
    frame.grid_propagate(False)
    frame.pack(pady=10)

    for i in range(2):
        frame.columnconfigure(i, weight=1)

    choose_file_btt = cls.Action_Button("File to encrypt", frame, lambda: fc.find_file(1))
    choose_file_label = cls.Path_label(frame, var.ENCRYPT_FILE_PATH)

    enc_file_btt = cls.Action_Button("Encryption key file", frame, lambda: fc.find_file(2))
    enc_file_label = cls.Path_label(frame, var.ENCRYPTION_KEY_PATH)

    generate_key_btt = cls.Action_Button("Generate encryption key", frame, lambda: fc.generate_key())
    key_label = cls.Key_Label(frame, var.ENCRYPTION_KEY)
    use_btt = cls.Action_Button("Use", frame, lambda: fc.use_file())
    key_file_label = cls.Path_label(frame, var.NEW_ENC_KEY_PATH)

    encryption_btt = cls.Custom_Button("Encrypt", frame, lambda: fc.encrypt())

    #----------------- Strefa pakowania----------------
    choose_file_btt.grid(column=0, row=0, sticky="nw", pady=(30,5), padx=30)
    choose_file_label.grid(column=0, row=1, sticky="nw", padx=30)

    enc_file_btt.grid(column=0, row=2, sticky="nw", pady=(30,5), padx=30)
    enc_file_label.grid(column=0, row=3, sticky="nw", padx=30)

    generate_key_btt.grid(column=0, row=4, sticky="nw", pady=(30,5), padx=30)
    key_label.grid(column=0, row=5, sticky="nw", padx=30, ipady=3)
    use_btt.grid(column=0, row=6, sticky="w", padx=30, pady=3)
    key_file_label.grid(column=0, row=7, sticky="w", padx=30)

    encryption_btt.grid(column=0, row=8, sticky="sw", padx=30, pady=(30, 0))

    #---------------- Obraz ----------------
    padlock_image = Image.open(fc.resource_path(var.closed_padlock_icon))
    padlock_image = padlock_image.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
    image_object = ImageTk.PhotoImage(padlock_image)

    image_label = tk.Label(frame, image=image_object, bg="white")
    image_label.image = image_object
    image_label.grid(row=0, column=1, rowspan=9, columnspan=1, sticky="nswe")

    #====== BACK ======
    back_button = cls.Back_Button("Back", encrypt_page, lambda: fc.back(main_page))
    back_button.pack(pady=15)
    #endregion

# region ==== Strona 3 ======
def render_decrypt_page():
    header = cls.Header(decrypt_page, "𝗗𝗲𝗰𝗿𝘆𝗽𝘁𝗶𝗼𝗻")
    header.pack(pady=10)

    # ======== Bialy kontener =======
    frame = tk.Frame(decrypt_page, bg='white', width=8 * var.COLUMN_WIDTH, height=10 * var.ROW_HEIGHT)
    frame.grid_propagate(False)
    frame.pack(pady=10)

    for i in range(2):
        frame.columnconfigure(i, weight=1)
    frame.rowconfigure(5, weight=1)

    choose_file_btt = cls.Action_Button("Encrypted file", frame, lambda: fc.find_file(1))
    choose_file_label = cls.Path_label(frame, var.ENCRYPT_FILE_PATH)

    dec_file_btt = cls.Action_Button("Encryption key file", frame, lambda: fc.find_file(2))
    dec_file_label = cls.Path_label(frame, var.ENCRYPTION_KEY_PATH)

    key_entry = cls.Key_Entry(frame)

    decryption_btt = cls.Custom_Button("Decrypt", frame, lambda: fc.decrypt())

    #----------------- Strefa pakowania----------------
    choose_file_btt.grid(column=0, row=0, sticky="nw", pady=(30,5), padx=30)
    choose_file_label.grid(column=0, row=1, sticky="nw", padx=30)

    dec_file_btt.grid(column=0, row=2, sticky="nw", pady=(30,5), padx=30)
    dec_file_label.grid(column=0, row=3, sticky="nw", padx=30)

    key_entry.grid(column=0, row=4, sticky="nw", pady=(30,5), padx=30, ipadx=5, ipady=3)
    fc.set_entry(key_entry)

    decryption_btt.grid(column=0, row=5, sticky="sw", padx=30, pady=(0, 20))

    #---------------- Obraz ----------------
    padlock_image = Image.open(fc.resource_path(var.open_padlock_icon))
    padlock_image = padlock_image.resize((3*var.COLUMN_WIDTH, 6*var.ROW_HEIGHT))
    image_object = ImageTk.PhotoImage(padlock_image)

    image_label = tk.Label(frame, image=image_object, bg="white")
    image_label.image = image_object
    image_label.grid(row=0, column=1, rowspan=6, columnspan=1, sticky="nswe")

    #====== BACK ======
    back_button = cls.Back_Button("Back", decrypt_page, lambda: fc.back(main_page))
    back_button.pack(pady=15)
    #endregion

render_main_page()
render_encrypt_page()
render_decrypt_page()

fc.show_frame(main_page)
root.mainloop()
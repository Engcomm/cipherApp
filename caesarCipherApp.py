## File : caesarCipherApp.py
## decscription : Implimentation of caesarCipher Application using tkinter
## Author: Naveenraj


# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def caesar_encipher(plaintext, key):
    '''
    '''
    # encipher
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
        else: ciphertext += c

    return ciphertext

def caesar_decipher(ciphertext, key):
    '''
    '''
    # decipher
    plaintext = ""
    for c in ciphertext.upper():
        if c.isalpha(): plaintext += I2L[ (L2I[c] - key)%26 ]
        else: plaintext += c

    return plaintext

import tkinter as tk
from tkinter import ttk

class CaesarCipher:

    def __init__(self, root):

        self.plain_text = tk.StringVar(root, value="")
        self.cipher_text = tk.StringVar(root, value="")
        self.key = tk.IntVar(root)

        root.title("Caesar Cipher Application")
        #root.geometry("500x700")

        style = ttk.Style()
        style.configure("TLabel",
                        font = "Serif 15",
                        padding=10)
        style.configure("TButton",
                         font="Serif 15",
                         padding=10)
        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        self.plain_label = tk.Label(root, text="Plain text", fg="lightgreen").grid(row=1, column=0)

        self.plain_entry = ttk.Entry(root,
                                    textvariable=self.plain_text, width=50)
        self.plain_entry.grid(row=0, column=1, rowspan=4 , columnspan=4)

        self.plain_clear = tk.Button(root, text="Clear",
                                    command=lambda: self.clear('plain')).grid(row=2, column=0)

        self.key_label = tk.Label(root, text="Key").grid(row=4, column=0)

        self.key_entry = ttk.Entry(root, textvariable=self.key).grid(row=4, column=1)

        self.encipher_button = ttk.Button(root, text="↓ Encipher ↓",
                                    command=lambda: self.encipher_press()).grid(row=4, column=3)

        self.decipher_button = ttk.Button(root, text="↑ Decipher ↑",
                                    command=lambda: self.decipher_press()).grid(row=4, column=4)

        self.cipher_label = tk.Label(root, text="Cipher text", fg="red").grid(row=7, column=0)

        self.cipher_entry = ttk.Entry(root,
                                    textvariable=self.cipher_text, width=50)
        self.cipher_entry.grid(row=6, column=1, rowspan=4 , columnspan=4)

        self.cipher_clear = tk.Button(root, text="Clear",
                                    command=lambda: self.clear('cipher')).grid(row=8, column=0)


        # Status Bar
        status = tk.Label(root, text="Zebs tech", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status.grid()

    def clear(self, str_val):
        if str_val == 'cipher':
            self.cipher_entry.delete(0, 'end')
        else:
            self.plain_entry.delete(0, 'end')

    def get_key(self):
        key_val = self.key.get()
        return key_val

    def encipher_press(self):
        key = self.get_key()
        cipher_text = caesar_encipher(self.plain_entry.get(), key)
        self.cipher_entry.delete(0, "end")
        self.cipher_entry.insert(0, cipher_text)

    def decipher_press(self):
        key = self.get_key()
        plain_text = caesar_decipher(self.cipher_entry.get(), key)
        self.plain_entry.delete(0, "end")
        self.plain_entry.insert(0, plain_text)


root = tk.Tk()

caesar = CaesarCipher(root)

root.mainloop()

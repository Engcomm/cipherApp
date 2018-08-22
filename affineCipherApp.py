## File : affineCipherApp.py
## decscription : Implimentation of affineCipher Application using tkinter
## Author: Naveenraj

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def affine_encipher(plaintext, a, b):
    # encipher
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha(): ciphertext += I2L[ (L2I[c] * a + b)%26 ]
        else: ciphertext += c

    return ciphertext

def affine_decipher(ciphertext, a, b):
    # decipher
    plaintext = ""
    for c in ciphertext.upper():
        if c.isalpha(): plaintext += I2L[ ( inv_a * (L2I[c] - b) )%26 ]
        else: plaintext += c
    return plaintext

def validate_a(a):
    # to find inverse of a
    inv_a = -1
    for x in range(1,26):
        if (a*x)%26 == 1:
            inv_a = x

    if inv_a == -1:
        # message box display
        messagebox.showerror("Error", "'a' doesn't have an inverse , choose another value for 'a'")
        raise ValueError("a doesn't have an inverse")


class AffineCipher:

    def __init__(self, root):

        self.plain_text = tk.StringVar(root, value="")
        self.cipher_text = tk.StringVar(root, value="")
        self.a = tk.IntVar(root)
        self.b = tk.IntVar(root)

        root.title("Affine Cipher Application")
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

        self.a_label = tk.Label(root, text="a").grid(row=4, column=0)

        self.a_entry = tk.Entry(root, textvariable=self.a).grid(row=4, column=1)

        self.b_label = tk.Label(root, text="b").grid(row=5, column=0)

        self.b_entry = tk.Entry(root, textvariable=self.b).grid(row=5, column=1)

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
        a_val = self.a.get()
        validate_a(a_val)
        b_val = self.b.get()
        return a_val, b_val

    def encipher_press(self):
        a, b = self.get_key()
        cipher_text = affine_encipher(self.plain_entry.get(), a, b)
        self.cipher_entry.delete(0, "end")
        self.cipher_entry.insert(0, cipher_text)

    def decipher_press(self):
        a, b = self.get_key()
        plain_text = affine_decipher(self.cipher_entry.get(), a, b)
        self.plain_entry.delete(0, "end")
        self.plain_entry.insert(0, plain_text)


root = tk.Tk()

caesar = AffineCipher(root)

root.mainloop()

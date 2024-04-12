import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from main import *
from generate_bits import *

class BBSGui:
    def __init__(self, root):
        self.n, self.x = initialize_bbs()

        self.gamma = None

        root.title('BBS Encryption GUI')
        root.geometry('500x300')

        self.gamma_text = scrolledtext.ScrolledText(root, height=2, wrap=tk.WORD)
        self.gamma_text.pack(pady=5)

        self.input_text = tk.Entry(root, width=50)
        self.input_text.pack(pady=5)

        encrypt_button = tk.Button(root, text='Зашифрувати', command=self.encrypt_message)
        encrypt_button.pack(pady=5)

        self.encrypted_text_label = tk.Label(root, text='Зашифроване повідомлення:')
        self.encrypted_text_label.pack()
        self.encrypted_text = tk.Label(root, text='', wraplength=450)
        self.encrypted_text.pack()

        self.decrypted_text_label = tk.Label(root, text='Розшифроване повідомлення:')
        self.decrypted_text_label.pack()
        self.decrypted_text = tk.Label(root, text='', wraplength=450)
        self.decrypted_text.pack()

        self.generate_gamma()

    def generate_gamma(self):
        # для прикладу10 байтів
        self.gamma = bbs_gamma(self.n, self.x, 10)
        self.gamma_text.delete('1.0', tk.END)
        self.gamma_text.insert(tk.INSERT, self.gamma)

    def encrypt_message(self):
        plaintext = self.input_text.get()
        if not plaintext:
            messagebox.showerror("Помилка", "Введіть текст")
            return

        encrypted = encrypt_decrypt_bbs(plaintext, self.gamma)
        decrypted = encrypt_decrypt_bbs(encrypted, self.gamma)

        self.encrypted_text['text'] = encrypted
        self.decrypted_text['text'] = decrypted


root = tk.Tk()
app = BBSGui(root)

root.mainloop()

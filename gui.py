
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
        root.geometry('500x400')  # Size to accommodate new components

        self.gamma_text = scrolledtext.ScrolledText(root, height=2, wrap=tk.WORD)
        self.gamma_text.pack(pady=5)

        self.input_text = tk.Entry(root, width=50)
        self.input_text.pack(pady=5)

        encrypt_button = tk.Button(root, text='Зашифрувати', command=self.encrypt_message)
        encrypt_button.pack(pady=5)

        self.encrypted_text_label = tk.Label(root, text='Зашифроване повідомлення:')
        self.encrypted_text_label.pack()
        self.encrypted_text = tk.Entry(root, width=50, state='readonly')  # Changed from Label to Entry
        self.encrypted_text.pack()

        self.decrypted_text_label = tk.Label(root, text='Розшифроване повідомлення:')
        self.decrypted_text_label.pack()
        self.decrypted_text = tk.Entry(root, width=50, state='readonly')  # Changed from Label to Entry
        self.decrypted_text.pack()

        # New entry for encrypted input
        self.input_encrypted_text = tk.Entry(root, width=50)
        self.input_encrypted_text.pack(pady=5)

        decrypt_button = tk.Button(root, text='Розшифрувати', command=self.decrypt_message)
        decrypt_button.pack(pady=5)

        self.decrypted_output_label = tk.Label(root, text='Розшифроване з введеного:')
        self.decrypted_output_label.pack()
        self.decrypted_output = tk.Entry(root, width=50, state='readonly')  # Changed from Label to Entry
        self.decrypted_output.pack()

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

        self.encrypted_text.config(state='normal')
        self.encrypted_text.delete(0, tk.END)
        self.encrypted_text.insert(0, encrypted)
        self.encrypted_text.config(state='readonly')
        self.decrypted_text.config(state='normal')
        self.decrypted_text.delete(0, tk.END)
        self.decrypted_text.insert(0, decrypted)
        self.decrypted_text.config(state='readonly')

    def decrypt_message(self):
        encrypted = self.input_encrypted_text.get()
        if not encrypted:
            messagebox.showerror("Помилка", "Введіть зашифроване повідомлення")
            return

        decrypted = encrypt_decrypt_bbs(encrypted, self.gamma)
        self.decrypted_output.config(state='normal')
        self.decrypted_output.delete(0, tk.END)
        self.decrypted_output.insert(0, decrypted)
        self.decrypted_output.config(state='readonly')


root = tk.Tk()
app = BBSGui(root)

root.mainloop()

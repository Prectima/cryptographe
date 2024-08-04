import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


class CryptoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cryptographie App")
        self.geometry("700x600")
        self.configure(bg="#f0f0f0")
        self.selected_cipher = None
        self.private_key = None
        self.public_key = None
        self.create_widgets()

    def create_widgets(self):
        # Main container
        self.main_frame = tk.Frame(self, bg="#f0f0f0")
        self.main_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Frame for selecting encryption method
        self.selection_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.selection_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        tk.Label(self.selection_frame, text="Choisissez une méthode de chiffrement", font=("Helvetica", 14, "bold"),
                 bg="#f0f0f0").grid(row=0, column=0, pady=10)

        self.ciphers = ["César", "Vigenère", "Substitution", "Transposition",
                        "Vernam", "Affine", "Hill", "RSA", "XOR"]

        self.buttons = []
        for i, cipher in enumerate(self.ciphers):
            button = tk.Button(self.selection_frame, text=cipher, font=("Helvetica", 12),
                               command=lambda c=cipher: self.select_cipher(c))
            button.grid(row=i + 1, column=0, pady=5, sticky="ew")
            self.buttons.append(button)

        # Frame for text input and output
        self.crypt_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.crypt_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.crypt_frame.grid_forget()

        tk.Label(self.crypt_frame, text="Texte à chiffrer:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=0,
                                                                                                                column=0,
                                                                                                                pady=5,
                                                                                                                sticky="w")
        self.input_text = scrolledtext.ScrolledText(self.crypt_frame, height=8, width=70, wrap=tk.WORD)
        self.input_text.grid(row=1, column=0, pady=10)

        tk.Label(self.crypt_frame, text="Texte chiffré:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").grid(row=2,
                                                                                                             column=0,
                                                                                                             pady=5,
                                                                                                             sticky="w")
        self.output_text = scrolledtext.ScrolledText(self.crypt_frame, height=8, width=70, wrap=tk.WORD,
                                                     state="disabled")
        self.output_text.grid(row=3, column=0, pady=10)

        self.encrypt_button = tk.Button(self.crypt_frame, text="Chiffrer", font=("Helvetica", 12),
                                        command=self.encrypt_text, bg="#4CAF50", fg="white")
        self.encrypt_button.grid(row=4, column=0, pady=10)

        self.back_button = tk.Button(self.crypt_frame, text="Retour", font=("Helvetica", 12), command=self.back_to_main,
                                     bg="#f44336", fg="white")
        self.back_button.grid(row=5, column=0, pady=10)

    def select_cipher(self, cipher):
        self.selected_cipher = cipher
        if cipher == "RSA":
            self.generate_rsa_keys()
        self.show_encrypt_screen()

    def show_encrypt_screen(self):
        self.selection_frame.grid_forget()
        self.crypt_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def encrypt_text(self):
        text = self.input_text.get("1.0", "end-1c")
        if not text:
            messagebox.showerror("Erreur", "Veuillez entrer du texte à chiffrer.")
            return

        if self.selected_cipher == "César":
            shift = 3  # Example shift value for Caesar cipher
            encrypted = self.caesar_cipher(text, shift)
        elif self.selected_cipher == "RSA":
            encrypted = self.rsa_encrypt(text)
        else:
            encrypted = f"Texte chiffré avec {self.selected_cipher} (non implémenté)"

        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", encrypted)
        self.output_text.configure(state="disabled")

    def back_to_main(self):
        self.crypt_frame.grid_forget()
        self.selection_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    def caesar_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result

    def generate_rsa_keys(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def rsa_encrypt(self, text):
        if not self.public_key:
            return "Erreur : Clé publique non générée."

        try:
            ciphertext = self.public_key.encrypt(
                text.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return ciphertext.hex()
        except Exception as e:
            return f"Erreur de chiffrement: {e}"


if __name__ == "__main__":
    app = CryptoApp()
    app.mainloop()

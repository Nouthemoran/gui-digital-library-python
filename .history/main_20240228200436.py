import tkinter as tk
from database import Base, engine  # Mengimpor objek engine
from models import user_model, kategori_model, buku_model, peminjaman_model, koleksi_model, ulasan_model
from views.login_view import login_page


class DigitalLibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Library App")
        self.geometry("12x600")
        
        # Migrasi model ke database
        Base.metadata.create_all(engine)

if __name__ == "__main__":
    login_page()

if __name__ == "__main__":
    app = DigitalLibraryApp()
    app.mainloop()
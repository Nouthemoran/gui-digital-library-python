import tkinter as tk
from database import Base, engine  # Mengimpor objek engine
from models import user_model, kategori_model, buku_model, peminjaman_model, koleksi_model

class DigitalLibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Library App")
        self.geometry("800x600")
        
        # Migrasi model ke database
        Base.metadata.create_all(engine)

if __name__ == "__main__":
    app = DigitalLibraryApp()
    app.mainloop()

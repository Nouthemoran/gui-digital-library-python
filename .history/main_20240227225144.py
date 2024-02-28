import tkinter as tk
from views.login_view import LoginView

class DigitalLibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Library App")
        self.geometry("800x600")
        
        # Tampilkan halaman login saat aplikasi dimulai
        self.show_login_view()

    def show_login_view(self):
        login_view = LoginView(self)
        login_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = DigitalLibraryApp()
    app.mainloop()

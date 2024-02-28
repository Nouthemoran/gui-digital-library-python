from tkinter import *
from controllers.auth_controller import login
from PIL import Image, ImageTk

class LoginForm:
    def __init__(self,window):
        self.window = window
        self.window.geometry("1166x718")

def login_page():
    # Fungsi yang menampilkan halaman login

    def validate_login():
        # Fungsi untuk memvalidasi login saat tombol "Login" ditekan
        username = username_entry.get()
        password = password_entry.get()
        # Panggil fungsi login dari controller
        login(username, password)


    # Buat jendela Tkinter
    window = Tk()
    LoginForm(window)
    window.title("Login")



    # Atur warna latar belakang jendela menjadi dark
    dark_color = "#222330"  # Gunakan kode warna yang lebih gelap
    window.configure(bg=dark_color)

     # Buat kerangka untuk membungkus form login
    login_frame = Frame(window, bg=dark_color)
    login_frame.place(relx=0.5, rely=0.5, anchor="center")
    frame_color = "white"
    login_frame.configure(bg=frame_color)

    # Label dan input field untuk username
    username_label = Label(window, text="Username:")
    username_label.grid(row=0, column=0, padx=100, pady=40)
    username_entry = Entry(window)
    username_entry.grid(row=0, column=1, padx=100, pady=40)

    # Label dan input field untuk password
    password_label = Label(window, text="Password:")
    password_label.grid(row=1, column=0, padx=100, pady=40)
    password_entry = Entry(window, show="*")
    password_entry.grid(row=1, column=1, padx=100, pady=40)

    # Tombol untuk melakukan login
    login_button = Button(window, text="Login", command=validate_login)
    login_button.grid(row=2, column=0, columnspan=2, padx=100, pady=40, sticky="WE")


    window.mainloop()

    if __name__ == "__main__":
        login_page()
from tkinter import Tk, Label, Entry, Button, messagebox
from controllers.auth_controller import login

def login_page():
    # Fungsi yang menampilkan halaman login

    def validate_login():
        # Fungsi untuk memvalidasi login saat tombol "Login" ditekan
        username = username_entry.get()
        password = password_entry.get()
        # Panggil fungsi login dari controller
        login(username, password)

    # Buat jendela Tkinter
    login_window = Tk()
    login_window.title("Login")

        # Set ukuran jendela
    login_window.geometry("600x400")  # Ubah ukuran sesuai kebutuhan
        # Atur warna latar belakang jendela menjadi hitam
    login_window.configure(bg="black")

    # Label dan input field untuk username
    username_label = Label(login_window, text="Username:")
    username_label.grid(row=0, column=0, padx=100, pady=40)
    username_entry = Entry(login_window)
    username_entry.grid(row=0, column=1, padx=100, pady=40)

    # Label dan input field untuk password
    password_label = Label(login_window, text="Password:")
    password_label.grid(row=1, column=0, padx=100, pady=40)
    password_entry = Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=100, pady=40)

    # Tombol untuk melakukan login
    login_button = Button(login_window, text="Login", command=validate_login)
    login_button.grid(row=2, column=0, columnspan=2, padx=100, pady=40, sticky="WE")

    # Jalankan loop utama Tkinter
    login_window.mainloop()

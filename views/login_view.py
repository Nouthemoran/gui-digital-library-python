from tkinter import *
from controllers.auth_controller import login
from PIL import Image, ImageTk

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.state('zoomed')
        self.window.resizable(0, 0)

        # BACKGROUND IMAGE
        self.bg_frame = Image.open('assets/images/background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # LOGIN FORM
        self.login_frame = Frame(self.window, bg="#040405", width='950', height=600)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.txt = 'WELCOME'
        self.heading = Label(self.login_frame, text=self.txt, font=('yu gothie ui', 25, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=80, y=30, width=300, height=30)        
        
        # # Label dan input field untuk username
        # username_label = Label(self.login_frame, text="Username:")
        # username_label.grid(row=0, column=0, padx=10, pady=10)
        # self.username_entry = Entry(self.login_frame)
        # self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # # Label dan input field untuk password
        # password_label = Label(self.login_frame, text="Password:")
        # password_label.grid(row=1, column=0, padx=10, pady=10)
        # self.password_entry = Entry(self.login_frame, show="*")
        # self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # # Tombol untuk melakukan login
        # login_button = Button(self.login_frame, text="Login", command=self.validate_login)
        # login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="WE")

    def validate_login(self):
        # Fungsi untuk memvalidasi login saat tombol "Login" ditekan
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Panggil fungsi login dari controller
        login(username, password)

def login_page():
    # Buat jendela Tkinter
    window = Tk()
    window.title("Login")
    window.configure(bg="#222330")  # Atur warna latar belakang jendela menjadi dark

    # Tampilkan form login
    LoginForm(window)

    window.mainloop()

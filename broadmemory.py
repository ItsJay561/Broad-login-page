from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk

root = Tk()
root.option_add('*Font', 'Tomapip')  # Set default font for the application
root.configure(bg="#C5DECD")  # Set the background color of the root window
root.title("Create Account")  # Set the title of the root window

# Load and display a logo image
logo_image = PhotoImage(file=r"C:\Users\jaybr\OneDrive\Documents\13 DDT - Jay\signup_button.png")
logo_label = Label(root, image=logo_image, background="#C5DECD")
logo_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Load and display an account image
account = PhotoImage(file=r"C:\Users\jaybr\OneDrive\Documents\13 DDT - Jay\loginiamge.png")
account_label = Label(root, image=account, background="#C5DECD")
account_label.grid(row=1, column=0, padx=10, pady=(10, 50), columnspan=2)

# Display a label for signing in
clickhere = ttk.Label(root, text="Sign in to Continue.", font=customtkinter.CTkFont(size=12, weight="bold"),
                      foreground="#185cac", background="#C5DECD")
clickhere.place(x=138, y=232)

# Display a label and entry field for the username
username_label = ttk.Label(root, text="Username:", foreground="#1871ac", background="#C5DECD",
                           font=('Georgia', 13, 'bold'))
username_label.grid(row=3, column=0, pady=5)
username_entry = customtkinter.CTkEntry(root, width=300)
username_entry.grid(row=3, column=1, pady=5)

# Display a label and entry field for the password
password_label = ttk.Label(root, text="Password:", foreground="#1871ac", background="#C5DECD",
                           font=('Georgia', 13, 'bold'))
password_label.grid(row=5, column=0, pady=5)
password_entry = customtkinter.CTkEntry(root, show="", width=300)
password_entry.grid(row=5, column=1, pady=5)

# Function to register the user when the "Sign in" button is clicked
def register_user():
    username = username_entry.get()
    password = password_entry.get()
    message_label.config(text="User registered successfully!", foreground="green")

# Create the "Sign in" button
login = customtkinter.CTkButton(root, text="Sign in", font=customtkinter.CTkFont(family="Kaiti", size=16))
login.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

# Display a label to show registration status or error messages
message_label = ttk.Label(root, text="", foreground="red", background="#C5DECD", font=('Arial', 12, 'bold'))
message_label.grid(row=8, column=0, padx=10, pady=5, columnspan=2)

root.mainloop()  # Start the main event loop

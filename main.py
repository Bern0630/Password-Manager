import tkinter
from tkinter import messagebox
import random
import pyperclip

FONT = ("Courier", 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    rand_password_list = password_letter + password_symbol + password_number

    random.shuffle(rand_password_list)
    rand_password = "".join(rand_password_list)

    password_entry.insert(0, rand_password)
    pyperclip.copy(rand_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    password_list = []
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website and email and password != "":
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email} \nPassword: {password} \n"
                                                              f"Is it ok to save?")
        if is_ok:
            with open("save.txt", mode="a") as data:
                password_list.append(data.write(f"{website} | {email} | {password}\n"))
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
    else:
        messagebox.showinfo(title="Fill The Blanks", message="Please do not leave any fields blank!")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
password_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:", font=FONT)
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=70)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = tkinter.Entry(width=70)
email_entry.insert(0, "hey@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tkinter.Entry(width=51)
password_entry.grid(row=3, column=1)

password_generator = tkinter.Button(text="Generate Password", command=generate_password)
password_generator.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=59, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

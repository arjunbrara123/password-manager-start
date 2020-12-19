from tkinter import *
from tkinter import messagebox
from password_generator import generate_password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def fill_pass():
    txtPassword.delete(0, END)
    txtPassword.insert(0, generate_password())

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_details():

    if len(txtWebsite.get()) == 0 or len(txtPassword.get()) == 0:
        messagebox.showinfo("Error!", "Please finish filling in your entry - don't leave any fields blank.")
    else:

        is_ok = messagebox.askokcancel(title=txtWebsite.get(), message=f"There are the details entered: \nEmail: {txtEmail.get()}"
                                                                       f"\nPassword: {txtPassword.get()} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write((f"{txtWebsite.get()} | {txtEmail.get()} | {txtPassword.get()}\n"))
            txtWebsite.delete(0, END)
            txtEmail.delete(0, END)
            txtPassword.delete(0, END)
            print("Added!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(bg="white", padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
imgLock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=imgLock)

canvas.grid(column=1, row=0, padx=20, pady=20)

lblWebsite = Label(text="Website:", bg="white").grid(column=0, row=1)
lblEmail = Label(text="Email/Username:", bg="white").grid(column=0, row=2)
lblPassword = Label(text="Password:", bg="white").grid(column=0, row=3)

txtWebsite = Entry(width=35)
txtWebsite.grid(column=1, row=1, columnspan=2)
txtWebsite.focus()
txtEmail = Entry(width=35)
txtEmail.grid(column=1, row=2, columnspan=2)
txtEmail.insert(0, "arjun@email.com")
txtPassword = Entry(width=21)
txtPassword.grid(column=1, row=3)

btnGenerate = Button(text="Generate Password", command=fill_pass).grid(column=2, row=3)
rdxAdd = Radiobutton(text="Add", bg="white", width=36, command=save_details).grid(column=1, row=4, columnspan=2)
window.mainloop()

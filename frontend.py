from tkinter import *
from tkinter import messagebox

from backend import passwordManager


class Password_Manager:
    def __init__(self, master):
        self.be = passwordManager()
        master.title('Password ADM')
        master.config(padx=100, pady=100)

        self.canvas = Canvas(width=200, height=200)
        self.logo_img = PhotoImage(file='vens/logo 2.png')
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        self.website_label = Label(text='Website')
        self.website_label.grid(row=1, column=0)
        self.email_label = Label(text='Email/Username')
        self.email_label.grid(row=2, column=0)
        self.password_label = Label(text='Password')
        self.password_label.grid(row=3, column=0)

        self.website_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()

        self.website_entry = Entry(width=39, textvariable=self.website_var)
        self.website_entry.grid(row=1, column=1, columnspan=3, sticky='NSEW')
        self.email_entry = Entry(width=39, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1, columnspan=3, sticky='NSEW')
        self.password_entry = Entry(width=39, textvariable=self.password_var)
        self.password_entry.grid(row=3, column=1, columnspan=2, sticky='NSEW')

        self.generate_password_button = Button(text='Generate', command=self.generate_password)
        self.generate_password_button.grid(row=3, column=3, sticky='NSEW')
        self.add_button = Button(text='Add', command=self.save_data)
        self.add_button.grid(row=4, column=1, sticky='NSEW')
        self.clear_button = Button(text='Clear', command=self.clear)
        self.clear_button.grid(row=4, column=2, sticky='NSEW')
        self.search_button = Button(text='Search', command=self.search_password)
        self.search_button.grid(row=4, column=3, sticky='NSEW')

    def generate_password(self):
        password = self.be.generate_password()
        self.password_entry.delete(0, 'end')
        self.password_entry.insert(0, password)

    def save_data(self):
        if len(self.website_entry.get()) == 0 or len(self.email_entry.get()) == 0 or len(self.password_entry.get()) == 0:
            messagebox.showinfo(title='Error', message='Please fill all the fields')
        else:
            self.be.save_data(self.website_entry.get(), self.email_entry.get(), self.password_entry.get())
            messagebox.showinfo(title='Success', message='Data saved successfully')

    def search_password(self):
        result = self.be.search_password(self.website_entry.get())
        if result is None:
            messagebox.showinfo(title='Error', message='No data found')
        else:
            self.email_entry.delete(0, 'end')
            self.email_entry.insert(0, result[2])
            self.password_entry.delete(0, 'end')
            self.password_entry.insert(0, result[3])

    def clear(self):
        self.website_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')


def main():
    mainWindow = Tk()
    password_manager = Password_Manager(mainWindow)
    mainWindow.mainloop()
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import cv2


class WelcomePage:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Manager Dinu")
        self.root.geometry("400x520+500+100")
        self.root.resizable(False, False)

        # First page with Create account and Login
        self.welcome_frame = tk.Frame(self.root, width=400, height=520)
        self.logo = tk.PhotoImage(file="libs/password_manager_logo2.png")
        self.label = tk.Label(self.root, image=self.logo,
                              padx=1, pady=1,
                              anchor="center",
                              justify="center")
        self.label.grid(row=0, column=0, padx=45, pady=80, sticky=tk.E + tk.W)

        self.create_account = tk.Button(self.root, text="Create Account",
                                        padx=10, pady=10, width=20, justify="center",
                                        bg="white", fg="black",
                                        activeforeground="white", activebackground="#148F77",
                                        command=lambda m="Create Account": self.press_create_account(m))
        self.create_account.grid(row=1, column=0, padx=10, pady=10)

        self.login = tk.Button(self.root, text="Login",
                               padx=10, pady=10, width=20, justify="center",
                               bg="white", fg="black",
                               activeforeground="white", activebackground="#148F77",
                               command=lambda m='Login': self.press_create_account(m))
        self.login.grid(row=3, column=0, padx=10, pady=10)

        self.label = tk.Label(self.root,
                              text="By continuing, you agree with our \n Terms of Services and Privacy Policy")
        self.label.bind('<Button-1>', self.press_key)
        self.label.grid(row=4, column=0, padx=30, pady=60)
        self.root.mainloop()

    def register(self):
        # The main video camera is initialized
        cap = cv2.VideoCapture(0)
        messagebox.showinfo(message="Look at the video camera and press OK when you are ready")
        # Se afiseaza mesajul de inregistrare
        print("Inregistrare...")

        # The image is being captured
        ret, frame = cap.read()

        # The image is resized
        frame = cv2.resize(frame, (500, 500))

        # The image is saved
        cv2.imwrite("libs/user.jpg", frame)

        messagebox.showinfo(message="User successfully registered!")
        # The video camera closes
        cap.release()

    def login_user(self):
        # The main video camera is initialized
        cap = cv2.VideoCapture(0)

        # Se afiseaza mesajul de login
        print("Login...")

        messagebox.showinfo(message="Look at the video camera and press OK when you are ready")
        ret, frame = cap.read()

        # The image is resized
        frame = cv2.resize(frame, (500, 500))

        # The previously saved image is read
        saved_image = cv2.imread("libs/user.jpg")

        # The previously saved image is resized
        saved_image = cv2.resize(saved_image, (500, 500))

        # The image is converted to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_saved_image = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)

        # The two images are compared
        result = cv2.matchTemplate(gray_frame, gray_saved_image, cv2.TM_CCOEFF_NORMED)

        # The maximum position of the correlation is determined
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        while max_val < 0.7:
            messagebox.showerror(message="Login failed. To try again, please press OK")
            # The main video camera is initialized
            cap = cv2.VideoCapture(0)
            # Se afiseaza mesajul de login
            print("Login...")
            messagebox.showinfo(message="Look at the video camera and press OK when you are ready")
            ret, frame = cap.read()

            frame = cv2.resize(frame, (500, 500))

            saved_image = cv2.imread("libs/user.jpg")

            saved_image = cv2.resize(saved_image, (500, 500))

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_saved_image = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)

            result = cv2.matchTemplate(gray_frame, gray_saved_image, cv2.TM_CCOEFF_NORMED)

            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            cap.release()
        else:
            messagebox.showinfo(message="V-ati logat cu succes!")
            cap.release()

    def press_create_account(self, m):
        if m == "Create Account":
            self.register()
            self.root.destroy()
            MainMenu()
        elif m == "Login":
            self.login_user()
            self.root.destroy()
            MainMenu()
        else:
            raise ValueError(f"Unexpected value for m: {m}")

        self.root.mainloop()

    @staticmethod
    def press_key(event):
        print("Legatura s-a realizat cu succes")
        path = "libs/Terms_condition.pdf"
        os.system(path)


class MainMenu:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Password Manager Dinu")
        self.root.geometry("850x650+500+100")
        self.root.resizable(False, False)

        # Frame
        self.main_menu_frame = tk.Frame(self.root, width=850, height=650, bg="#ff5733")
        self.main_menu_frame.pack(fill="both", expand=1)
        #  Label png
        self.logo = tk.PhotoImage(file="libs/password_manager_logo2.png")
        self.label = tk.Label(self.main_menu_frame, image=self.logo,
                              padx=1, pady=1,
                              anchor="center",
                              justify="center",
                              bg="#ff5733")
        self.label.grid(row=0, column=0, padx=60, pady=20, sticky=tk.E + tk.W, columnspan=4)

        # Menu Entry

        self.label_website = tk.Label(self.main_menu_frame,
                                      padx=1, pady=5, text="Website",
                                      justify="center",
                                      bg="#5cb85c")
        self.label_website.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E + tk.W)

        self.entry_website = tk.Entry(self.main_menu_frame, width=40,
                                      font=("Arial", 12),
                                      bg="#F8F9F9", bd=3,
                                      justify="center")
        self.entry_website.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

        self.label_username = tk.Label(self.main_menu_frame,
                                       padx=1, pady=5, text="Username",
                                       justify="center",
                                       bg="#5cb85c")
        self.label_username.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E + tk.W)

        self.entry_username = tk.Entry(self.main_menu_frame, width=40,
                                       font=("Arial", 12),
                                       bg="#F8F9F9", bd=3,
                                       justify="center")
        self.entry_username.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

        self.label_password = tk.Label(self.main_menu_frame,
                                       padx=1, pady=5, text="Password",
                                       justify="center",
                                       bg="#5cb85c")
        self.label_password.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E + tk.W)

        self.entry_password = tk.Entry(self.main_menu_frame, width=40,
                                       font=("Arial", 12),
                                       bg="#F8F9F9", bd=3,
                                       justify="center", show="*")
        self.entry_password.grid(row=3, column=1, padx=10, pady=10, columnspan=3)

        self.save_btn = tk.Button(self.main_menu_frame, text="Save", command=self.button_save)
        self.save_btn.grid(row=4, column=0, padx=10, pady=10)

        # "show password" button
        self.check_var = tk.IntVar()
        self.show_pw_chkbtn = tk.Checkbutton(self.main_menu_frame, text="show password", command=self.show_password,
                                             onvalue=1, offvalue=0, variable=self.check_var)
        self.show_pw_chkbtn.grid(row=4, column=1, padx=10, pady=10)

        self.delete_btn = tk.Button(self.main_menu_frame, text="Delete", bg="#FFFFFF", command=self.button_delete)
        self.delete_btn.grid(row=4, column=2, padx=10, pady=10)

        self.edit_btn = tk.Button(self.main_menu_frame, text="Edit", command=self.button_edit)
        self.edit_btn.grid(row=5, column=0, padx=10, pady=10)

        self.copy_pw_btn = tk.Button(self.main_menu_frame, text="Copy Password")
        self.copy_pw_btn.grid(row=5, column=1, padx=10, pady=10)

        self.show_items_btn = tk.Button(self.main_menu_frame, text="Show all items")
        self.show_items_btn.grid(row=6, column=0, padx=10, pady=10)

        self.search_entry = tk.Entry(self.main_menu_frame)
        self.search_entry.grid(row=6, column=1, padx=10, pady=10)

        self.search_btn = tk.Button(self.main_menu_frame, text="Search")
        self.search_btn.grid(row=6, column=2, padx=10, pady=10)

        # create Treeview
        columns = ("id", "website", "username", "password")
        self.tree = ttk.Treeview(self.main_menu_frame, columns=columns, show="headings")
        self.tree.grid(row=7, column=0, columnspan=4, padx=5, pady=0)

        # the table header is created. They must be identical with the order in columns variable.
        self.tree.heading("id", text="id")
        self.tree.heading("website", text="Website")
        self.tree.heading("username", text="Username")
        self.tree.heading("password", text="Password")
        self.tree['displaycolumns'] = ("id", "website", "username", "password")

        # scrollbar from treeview
        self.scrollbar = ttk.Scrollbar(self.main_menu_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=7, column=4, sticky="ns", padx=0)

        s = SQL("", "", "")
        result = s.get_data_for_tree()
        for data in result:
            self.tree.insert("", tk.END, values=data)

    def show_password(self):
        """
        The show password button - which shows what is written in the password field
        """
        if self.check_var.get():
            self.entry_password["show"] = ""
        else:
            self.entry_password.configure(show="*")

    def get_text_data(self):
        """
        takes the data filled in by the user from the website, username and password fields
        """
        return self.entry_website.get(), self.entry_username.get(), self.entry_password.get()

    def clear_entry_data(self):
        """
        delete the data from the entry fields after pressing the save button
        """
        self.entry_website.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def button_save(self):
        """
        What happens when the user presses the save button
       """
        website, username, password = self.get_text_data()
        s = SQL(website, username, password)
        s.add_data()
        result = s.get_data_for_tree()
        data = [result[-1][0], website, username, password]
        self.tree.insert("", tk.END, values=data)
        self.clear_entry_data()

    def button_delete(self):
        """
        What happens when the user presses the delete button.
        """
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)

    def button_edit(self):
        selected_item = self.tree.selection()[0]
        self.tree.item(selected_item, text="blub", values=("", ""))

        self.root.mainloop()


class SQL:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password
        # database connection
        self.connection = sqlite3.connect("password_manager.db")
        self.cursor = self.connection.cursor()

        # the table is created when the SQL instance is created
        self.create_table()

    def create_table(self):
        """
        The table management_password is created
        """
        create_command = """CREATE TABLE IF NOT EXISTS management_password(
                            website TEXT,
                            username TEXT,
                            password  TEXT                                                    
                            );"""
        self.cursor.execute(create_command)

    def add_data(self):
        """
        Function that adds values to the table
        """
        self.cursor.execute('INSERT INTO management_password VALUES(?,?,?)',
                            (self.website, self.username, self.password))
        self.connection.commit()

    def get_data_for_tree(self):
        """
        Select data from the table. Rowid - is the autoincrement id
        """
        select_command = """SELECT rowid, website, username, password website FROM management_password;"""
        result = self.cursor.execute(select_command)
        return result.fetchall()

    def delete_record(self, table_name="management_password"):
        delete_command = f'''DELETE FROM {table_name} WHERE ID = ? '''
        self.cursor.execute(delete_command)
        self.connection.commit()


def main():
    main_menu = WelcomePage()


if __name__ == "__main__":
    main()

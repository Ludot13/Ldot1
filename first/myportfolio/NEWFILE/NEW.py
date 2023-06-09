import csv

def register():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    with open("users.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])

    print("Регистрация успешно завершена.")

def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    with open("users.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Авторизация успешна.")
                return

    print("Неверное имя пользователя или пароль.")

def logout():
    print("Выход из учетной записи.")

def main():
    while True:
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

import csv
import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()

    with open("users.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])

    messagebox.showinfo("Регистрация", "Регистрация успешно завершена.")

def login():
    username = entry_username.get()
    password = entry_password.get()

    with open("users.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == username and row[1] == password:
                messagebox.showinfo("Авторизация", "Авторизация успешна.")
                return

    messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль.")

def logout():
    messagebox.showinfo("Выход", "Выход из учетной записи.")

def main():
    window = tk.Tk()
    window.title("Регистрация и авторизация")

    label_username = tk.Label(window, text="Имя пользователя:")
    label_username.pack()
    entry_username = tk.Entry(window)
    entry_username.pack()

    label_password = tk.Label(window, text="Пароль:")
    label_password.pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    button_register = tk.Button(window, text="Регистрация", command=register)
    button_register.pack()

    button_login = tk.Button(window, text="Авторизация", command=login)
    button_login.pack()

    button_logout = tk.Button(window, text="Выход", command=logout)
    button_logout.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
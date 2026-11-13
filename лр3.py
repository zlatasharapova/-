import tkinter as tk
from random import choice, shuffle
from string import ascii_uppercase, digits
import subprocess

def play_music():
    global player
    if player is None or player.poll() is not None:
        player = subprocess.Popen(['afplay', 'song.mp3'])
    window.after(1000, play_music)


def on_close():
    if player is not None:
        player.terminate()
    window.destroy()

def generate_block():
    block = [choice(ascii_uppercase) for _ in range(3)]
    block.append(choice(digits))
    shuffle(block)
    return ''.join(block)

def generate_key():
    return '-'.join(generate_block() for _ in range(4))

step=0
player=None

def animate():
    global step
    key_var.set(generate_key())
    step += 1
    if step < 15:
        window.after(200, animate)
    else:
        step = 0
        btn.configure(state='normal')


def generate():
    btn.configure(state='disabled')
    animate()


window = tk.Tk()
window.title('key generation')
window.geometry('776x714')
window.resizable(0, 0)
bg_img = tk.PhotoImage(file='cinnamonroll.png')

label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window,
                       text='KEY GENERATOR',
                       font=('Consolas', '24'),
                       bg='black',
                       fg='pink')
title_label.grid(row=0, column=0, pady=30, padx=100)

key_var = tk.StringVar(value='XXXX-XXXX-XXXX-XXXX')
key_entry = tk.Entry(window,
                     textvariable=key_var,
                     width=19,
                     font=('Consolas', '24'),
                     fg='pink',
                     justify='center',
                     state='readonly')
key_entry.grid(row=1, column=0, pady=20)

btn = tk.Button(window,
                text='Generate',
                width=10,
                font=('Consolas', '24'),
                fg='pink',
                command=generate)
btn.grid(row=2, column=0, pady=20)
window.protocol('WM_DELETE_WINDOW', on_close)
play_music()
window.mainloop()
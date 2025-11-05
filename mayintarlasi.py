import tkinter as tk
from tkinter import Label

import random


root = tk.Tk()
root.title("Mayın Tarlası")

mesaj=tk.Label(root, text="", font=("Arial", 16))
mesaj.grid(row=10, column=0, columnspan=10, pady=10)

alan= [[0 for j in range(10)] for i in range(10)]

mayin_sayisi = 10
for _ in range(mayin_sayisi):
    i=random.randint(0,9)
    j=random.randint(0,9)
    while alan[i][j] == 1:
        i=random.randint(0,9)
        j=random.randint(0,9)
    alan[i][j] = 1

def tikla(i, j):
    if alan[i][j]==1:
        butonlar[i][j].config(text="*", bg="red")
        print("Mayına bastınız! Oyun bitti.")
        mesaj.config(text="Mayına bastınız! Oyun bitti.")
        root.after(2000, root.destroy)

    else:
        butonlar[i][j].config(text="0", bg="green")

butonlar= [[None for j in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        buton = tk.Button(root,text=" ", width=3, height=1,
                          command=lambda i=i, j=j: tikla(i, j))
        buton.grid(row=i, column=j)
        butonlar[i][j] = buton
root.mainloop()





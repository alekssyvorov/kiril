from tkinter import *

bomb = 100
score = 0
press_return = True


def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text='')
        update_bomb()
        update_score()
        update_display()
        press_return = False


def update_display():
    global bomb
    global score
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif bomb > 0 and bomb <= 50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse: " + str(bomb))
    score_label.config(text="Score: " + str(score))
    fuse_label.after(100, update_display)


def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(1000, update_bomb)


def update_score():
    global score
    score += 2
    if is_alive():
        score_label.after(4000, update_score)


def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        label.config(text="BANG! BANG! BANG!")
        press_return = True
        return False
    else:
        return True


def click():
    global bomb
    if is_alive():
        bomb -= 1


root = Tk()
root.geometry("400x550")
root.resizable(False, False)

label = Label(root, text='Press [ENTER] to start the game',
              font=('Comic Sans MS', 12))
label.pack()
fuse_label = Label(root, text="Fuse: " + str(bomb), font=('Comic Sans MS', 14))
fuse_label.pack()
score_label = Label(root, text="Score: " + str(score), font=('Comic Sans MS', 14))
score_label.pack()

no_photo = PhotoImage(file="img/bomb_no.gif")
normal_photo = PhotoImage(file="img/bomb_normal.gif")
bang_photo = PhotoImage(file="img/pow.gif")

bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text='Click me', font=('Comic Sans MS', 14),
                      bg="#000000", fg='#ffffff', bd=2, command=click)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()

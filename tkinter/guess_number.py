from asyncio import get_event_loop
from math import degrees
from tkinter import *
from tkinter import messagebox
lives = 10
total_score = 1

root = Tk()
root.geometry('215x215')
# my_number = StringVar()

def cange_score(score):
    score = score + 1
    return cange_score

def callback(event, total_score = cange_score):
    if my_number.get() == "10":
        messagebox.showinfo("GUI Python", "Yep, you'r right!")
        
        run(cange_score(total_score))

        
    else:
        messagebox.showerror("GUI Python", "No, try again \n Lives remain: " + str(lives) )
    # my_number["text"] = my_number.get()
    
    

def run(total_score = total_score):
    
    for widget in root.winfo_children():
        widget.grid_forget()
        widget.place_forget()

    life_str = Label(root, text='Lives remain: ' + str(lives), anchor="w", justify=LEFT)
    life_str.place(relx=.0, rely=.0, height=20, width=root.winfo_width()/2)
    score = Label(root, text='Score: ' + str(total_score), anchor="w", justify=LEFT)
    score.place(relx=.5, rely=.0, height=20, width=root.winfo_width()/2)
    Label(root, text='Guess a number between 1 and 10:', anchor="w", justify=LEFT).place(relx=.0, rely=.1, height=20, width=200)
    my_number.place(relx=.37, rely=.2, height=20, width=110)
    Label(root, text='Enter number:', anchor="w", justify=LEFT).place(relx=.0, rely=.2, height=20, width=80)
    root.bind('<Return>', callback)




hello_lbl = Label(root, text = 'Hi there!\n Do you wanna play guess the number? \n').grid(row=1, column=1)

btn_start = Button(root, text="Yep", background="#6c0", foreground="#000000", padx="15", pady="6", font="15", command=run)
btn_start.place(relx=.35, rely=.3, height=30, width=60)

btn_exit = Button(root, text="Nope", background="#cecece", foreground="#000000", padx="15", pady="6", font="15", command=root.quit)
btn_exit.place(relx=.35, rely=.5, height=30, width=60)

my_number = Entry(root, textvariable='')
root.mainloop()
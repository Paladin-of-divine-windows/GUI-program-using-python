from textwrap import wrap
from tkinter import *


root = Tk()
root.title('Mad Libs Generator на tkinter')
root.geometry('250x400+400+150')
apple_story_label_txt = ["Enter adjective :", "Enter a color name:", "Enter a thing name:", "Enter a place name:", "Enter a person name:",
            "Enter a adjactive:", "Enter a insect name:", "Enter a food name:", "Enter a verb name:"]

butterfly_story_label_txt = ["Enter person name:", "Enter color:", "Enter food name:", "Enter an adjective:", "Enter a thing name:",
            "Enter place:", "Enter verb:", "Enter adverb:", "Enter food name:", "Enter a thing name:"]

photographer_story_label_txt = ["Enter a animal name:", "Enter a profession:", "Enter a cloth name:", "Enter a thing name:", "Enter a name:",
            "Enter a name:", "Enter a ing verb:", "Enter food name:"]
person_name = StringVar()
color = StringVar()
foods = StringVar()
adjective = StringVar()
sec_adjective = StringVar()
thing = StringVar()
place = StringVar()
verb = StringVar()
adverb = StringVar()
food = StringVar()
things = StringVar()
insect_name = StringVar()
animals = StringVar()
profession = StringVar()
cloth = StringVar()
apple_var_list = [adjective, color, thing, place, person_name, sec_adjective, insect_name, food, verb]
butterfly_var_list = [person_name, color, foods, adjective, thing, place, verb, adverb, food, things]
photographer_var_list = [animals, profession, cloth, thing, person_name, place, verb, food]
all_var_list = [person_name, color, foods, adjective, sec_adjective, thing, place, verb, adverb, food, things, insect_name, animals, profession, cloth]

def text_normalise(text):
    width = root.winfo_width()
    char_width = width / (len(text)*7.8)
    wrapped_text = '\n'.join(wrap(text, int(len(text) * char_width)))  
    Label(text=wrapped_text, font='Georgia', justify='left').grid(row=0,column=0)
    back_btn.place(relx=.5, rely=.88, anchor="c", height=60, width=230, bordermode=OUTSIDE)

def hide_all():
    for widget in root.winfo_children():
        widget.grid_forget()
        widget.place_forget()

def apply_apple_text():
    hide_all()

    text = ('Last night I dreamed I was a ' + adjective.get() + ' butterfly with ' + color.get() + ' splocthes that looked like '
        + thing.get() + ' .I flew to ' + place.get() + ' with my bestfriend and '+ person_name.get() + ' who was a '
        + sec_adjective.get() + ' ' + insect_name.get() + ' .We ate some ' + food.get() + ' when we got there and then decided to '
        + verb.get() + ' and the dream ended when I said-- lets ' + verb.get() + '.')
   
    text_normalise(text)


def apply_butterfly_text():
    hide_all()

    text = ('Today we picked apple from '+ person_name.get() + 
        "'s Orchard. I had no idea there were so many different varieties of apples. I ate " + color.get() +
        ' apples straight off the tree that tested like '+ foods.get() + '. Then there was a '+ adjective.get() + 
        ' apple that looked like a ' + thing.get() + '.When our bag were full, we went on a free hay ride to '+ place.get() + 
        ' and back. It ended at a hay pile where we got to '  +verb.get() + ' ' + adverb.get() + 
        '. I can hardly wait to get home and cook with the apples. We are going to make appple '+ food.get() + 
        ' and '+ things.get() +' pies!.')

    text_normalise(text)

def apply_photographer_text():
    hide_all()

    text = ('say ' + food.get() + ', the photographer said as the camera flashed! ' + person_name.get() + 
        ' and I had gone to ' + place.get() +
        ' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals.get() + 
        ' pretending to be a ' + profession.get() + 
        '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things.get() + ' wearing ' + cloth.get() + 
        ' and ' + verb.get() + ' --exactly what I had in mind')

    text_normalise(text)


def return_back():

    for var in all_var_list:
         var.set('')

    hide_all()

    btn_madLib1.place(relx=.5, rely=.20, anchor="c", height=60, width=230, bordermode=OUTSIDE)
    btn_madLib2.place(relx=.5, rely=.40, anchor="c", height=60, width=230, bordermode=OUTSIDE)
    btn_madLib3.place(relx=.5, rely=.60, anchor="c", height=60, width=230, bordermode=OUTSIDE)
    
def Create_apple_story():
    btn_madLib1.place_forget()
    btn_madLib2.place_forget()
    btn_madLib3.place_forget()
    for i in range(9):
        Entry(root, textvariable=apple_var_list[i]).grid(row=i, column=2, pady=2, sticky ='w')
        Label(text=apple_story_label_txt[i], justify='left').grid(row=i, column=1, pady=2, sticky ='w')
    
    apply_apple_btn = Button(root, text="Apply story", font="arial 15", command=apply_apple_text)
    apply_apple_btn.place(relx=.5, rely=.70, anchor="c", height=60, width=230, bordermode=OUTSIDE)
    back_btn.place(relx=.5, rely=.88, anchor="c", height=60, width=230, bordermode=OUTSIDE)

def Create_butterfly_story():
    what_story = 'butterfly'
    btn_madLib1.place_forget()
    btn_madLib2.place_forget()
    btn_madLib3.place_forget()
    for i in range(10):
        Entry(root, textvariable=butterfly_var_list[i]).grid(row=i, column=2, pady=2, sticky ='w')
        Label(text=butterfly_story_label_txt[i], justify='left').grid(row=i, column=1, pady=2, sticky ='w')

    apply_butterfly_btn = Button(root, text="Apply story", font="arial 15", command=apply_butterfly_text)
    apply_butterfly_btn.place(relx=.5, rely=.70, anchor="c", height=60, width=230, bordermode=OUTSIDE)
    back_btn.place(relx=.5, rely=.88, anchor="c", height=60, width=230, bordermode=OUTSIDE)

def Create_photographer_story():
    what_story = 'photographer'
    btn_madLib1.place_forget()
    btn_madLib2.place_forget()
    btn_madLib3.place_forget()
    for i in range(8):
       Entry(root, textvariable=photographer_var_list[i]).grid(row=i, column=2, pady=2, sticky ='w')
       Label(text=photographer_story_label_txt[i], justify='left').grid(row=i, column=1, pady=2, sticky ='w')
    
    apply_photographer_btn = Button(root, text="Apply story", font="arial 15", command=apply_photographer_text)
    apply_photographer_btn.place(relx=.5, rely=.70, anchor="c", height=60, width=230, bordermode=OUTSIDE)
    back_btn.place(relx=.5, rely=.88, anchor="c", height=60, width=230, bordermode=OUTSIDE)

# main menu buttons 
btn_madLib1 = Button(root, text="Apple story", font="arial 15", command=Create_apple_story)
btn_madLib2 = Button(root, text="The butterfly", font="arial 15", command=Create_butterfly_story)
btn_madLib3 = Button(root, text="Photographer", font="arial 15", command=Create_photographer_story)

# Story buttons and input strings
back_btn = Button(root, text="Back to many", font="arial 15", command=return_back)

btn_madLib1.place(relx=.5, rely=.20, anchor="c", height=60, width=230, bordermode=OUTSIDE)
btn_madLib2.place(relx=.5, rely=.40, anchor="c", height=60, width=230, bordermode=OUTSIDE)
btn_madLib3.place(relx=.5, rely=.60, anchor="c", height=60, width=230, bordermode=OUTSIDE)

root.mainloop() 
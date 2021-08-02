from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()

root.geometry("400x400")

def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))


Label(root, text="Dictionary", font=("Helvetika 20 bold"), fg="Green").pack(pady=10)

frame = Frame(root)
Label(frame, text="Type Word", font=("Helvetika 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetika 15 bold"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="meaning:- ", font=("Helvetika 10 bold")).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Helvetika 10 bold"))
meaning.pack()
frame1.pack(pady=10)


frame2 = Frame(root)
Label(frame2, text="synonym:- ", font=("Helvetika 10 bold")).pack(side=LEFT)
synonym = Label(frame2, text="", font=("Helvetika 10 bold"))
synonym.pack()
frame2.pack(pady=10)


frame3 = Frame(root)
Label(frame3, text="antonym:- ", font=("Helvetika 10 bold")).pack(side=LEFT)
antonym = Label(frame3, text="", font=("Helvetika 10 bold"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)

Button(root, text="submit", font=("Helvetika 10 bold"), command=dict).pack()

root.mainloop()




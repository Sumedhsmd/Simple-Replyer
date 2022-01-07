from tkinter import *

window = Tk()

window.geometry('300x100')

replyes = {'how are you': "I'm Good !!!", 'hello': 'Heyy !!!', 'hi': 'Heyy', 'bye': 'Okay, Bye', 'see you':'bye'}

# while True:
#     ask = input(' \t > ')
#     if 'Bye' in ask or 'bye' in ask:
#         print(spl('Bye !!!'))
#         break
#     else:
#         call(ask)

user_rep = Entry(window,width=25)
user_rep.grid(column=0, row=0)

com_rep = Label(window,text='Reply...')
com_rep.grid(column=0, row=2)


def clicked():
    inp = user_rep.get()
    new_inp = inp[0].lower() + inp[1:]
    if new_inp in replyes.keys():
        com_rep.configure(text=f'{replyes[new_inp]}')
    else:
        com_rep.configure(text='Hmm')

user_btn = Button(window, text='Submit', bg='white',fg='blue',command=clicked)
user_btn.grid(column=1,row=0)



window.mainloop()

from tkinter import *
from Function_File import lstSorter, searchEngine, developerGraph, averageplayedGraph, game_info


root = Tk()
root.state("zoomed")

top_frame = Frame(root, bg='skyblue4', height=30)
left_frame = Frame(root, bg='azure4', width=450)
right_frame = Frame(root, bg='LightSteelBlue4', width=500, highlightbackground="azure4", highlightthickness=1)
center_top = Frame(root, bg='LightSteelBlue4', width=650, height=400)
center_bot = Frame(root, bg='LightSteelBlue4', width=650, height=500)

top_frame.pack(fil='x', side='top')
left_frame.pack(fill='y', side='left')
right_frame.pack(fill='y', side='right')
center_top.pack(side='top', expand=False)
center_bot.pack(side='bottom', expand=False)


steam_label = Label(top_frame, text='Steam', bg="skyblue4", fg="black",font=('Arial', 20, 'bold'))
steam_label.pack(padx='225')


listBox = Listbox(left_frame, width=50, bg="#FAF9F6", font=('Arial', 8))
listBox.pack(fill='y', side='left')

for i in lstSorter("name", False):
    listBox.insert('end', i)

optionMenu = Listbox(left_frame, height=3, bg="#FAF9F6", font=('Arial', 9))
optionMenu.pack()
optionMenu.insert(1, "Alfabetische volgorde")
optionMenu.insert(2, "High->Low ratings")
optionMenu.insert(3, "Low->High ratings")

def listbox():
    info = searchbox.get()
    listBox.delete(0, "end")

    if len(info) == 0:

        for i in optionMenu.curselection():
            if optionMenu.get(i) == "Alfabetische volgorde":
                listBox.delete(0, "end")
                for i in lstSorter("name", False):
                    listBox.insert('end', i)

            elif optionMenu.get(i) == "High->Low ratings":
                listBox.delete(0, "end")

                for i in lstSorter("positive_ratings", True):
                    listBox.insert('end', i)
            elif optionMenu.get(i) == "Low->High ratings":
                listBox.delete(0, "end")

                for i in lstSorter("positive_ratings", False):
                    listBox.insert('end', i)
    else:
        for i in searchEngine(info):
            listBox.insert("end", i)

def seleteren():
    for i in listBox.curselection():
        developerGraph(center_top)
        averageplayedGraph(center_bot, listBox.get(i))
        lst = game_info(listBox.get(i))
        # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])


        name_of_game = Entry(right_frame, fg='blue', font=('Arial', 10, 'bold'), width=20)
        name_of_game.grid(row=0, column=1)
        name_of_game.insert("end", listBox.get(i))

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                d = Entry(right_frame, width=35, fg='blue',
                          font=('Arial', 10, 'bold'))

                d.grid(row=1+i, column= 1+j, padx=5, pady=3)
                d.insert(END, lst[i][j])
                d.configure(state='disabled')
    return


searchbox = Entry(left_frame, bg="#FAF9F6", font=('Arial', 9))
searchbox.pack(pady=5)

update_lijst = Button(left_frame, width=20, text="Update lijst", bg="#FAF9F6", font=('Arial', 9), command=listbox)
update_lijst.pack(pady=7)

seleteren_button = Button(left_frame, width=20, text="Selecteren", bg="#FAF9F6", font=('Arial', 9), command=seleteren)
seleteren_button.pack(pady=5)

root.mainloop()
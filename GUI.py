from tkinter import *
from Function_File import lstSorter, searchEngine, developerGraph, averageplayedGraph, game_info,\
    ww_check, sorted_hours_maker


root = Tk()
root.state("zoomed")

### makes sortedhourslst

# na 1x runnen kan je dit uitcommenten
# sorted_hours_maker()

### Frames
top_frame = Frame(root, bg='skyblue4', height=30)
left_frame = Frame(root, bg='azure4', width=450)
right_frame = Frame(root, bg='LightSteelBlue4', width=500, highlightbackground="azure4", highlightthickness=1)
center_top = Frame(root, bg='LightSteelBlue4', width=650, height=400)
center_bot = Frame(root, bg='LightSteelBlue4', width=650, height=500)
login_frame = Frame(root, bg='LightSteelBlue4', width=650, height=500)


### Het maken van alle Frames
top_frame.pack(fil='x', side='top')
left_frame.pack(fill='y', side='left')
right_frame.pack(fill='y', side='right')
center_top.pack(side='top', expand=False)
center_bot.pack(side='bottom', expand=False)

### functies

# def alarm_sensor():
#     ### maakt button een toggle button ###
#     if sensor_button.config('relief')[-1] == 'sunken':
#         sensor_button.config(relief="raised")
#     else:
#         sensor_button.config(relief="sunken")
#
#     alarm = False
#     ### herhaalt totdat de alarm afgaat en maakt een waarshuwing tab aan ###
#     while alarm == False:
#         if "function" == True:
#             top = Toplevel(root, bg="#EDB937")
#             top.geometry("250x125")
#             top.title("Child Window")
#             warning = Label(top, text="WATCH OUT! \n You are going to fall!", font=('Arial', 12, 'bold')
#                             , bg="#A11D2A", height=200, borderwidth=1, relief="solid")
#             warning.pack(pady=20, fill="x")
#             alarm = True


def login_check(wachtwoord):
    ### gebruikt functie om te kijken of wachtwoord klopts ###
    ww = ww_check(wachtwoord)
    if ww == True:
        reverse_pop_up()
        login.configure(bg='white')
    else:
        login.configure(bg='red')


def pop_up():
    ### vergeet frames en maakt nieuwe frame aan voor login scherm ###
    top_frame.pack_forget()
    left_frame.pack_forget()
    right_frame.pack_forget()
    center_top.pack_forget()
    center_bot.pack_forget()
    login_frame.pack(fill="both", expand=True)


def reverse_pop_up():
    ### maakt mainpage frames aan en vergeet login frame ###
    top_frame.pack(fil='x', side='top')
    left_frame.pack(fill='y', side='left')
    right_frame.pack(fill='y', side='right')
    center_top.pack(side='top', expand=False)
    center_bot.pack(side='bottom', expand=False)
    login_frame.pack_forget()

def listbox():
    # deze functie maakt de lijsten die de GUI weergeeft
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
        # rows en column in lijst
        total_rows = len(lst)
        total_columns = len(lst[0])

        name_of_game = Entry(right_frame, fg='blue', font=('Arial', 10, 'bold'), width=20)
        name_of_game.grid(row=0, column=1)
        name_of_game.insert("end", listBox.get(i))

        # het maken van de table
        for i in range(total_rows):
            for j in range(total_columns):
                d = Entry(right_frame, width=35, fg='blue',
                          font=('Arial', 10, 'bold'))

                d.grid(row=1 + i, column=1 + j, padx=5, pady=3)
                d.insert(END, lst[i][j])
                d.configure(state='disabled')

### Login Scherm ###

username = Label(login_frame, text= "Username",font=('Arial', 10, 'bold'))
wachtwoord = Label(login_frame, text="Password", font=('Arial', 10, 'bold'))
wacht_needs = Label(login_frame, bg='LightSteelBlue4', borderwidth=1, relief="sunken", font=('Arial', 10, 'bold'),
                    text="Your password need to be between 10 en 20 digits\n need to contain a special digit\n a number and may not contain '(', ')', '[', ']', '{', '}', '/' ")

### Entry's
entry_username = Entry(login_frame, width=20)
entry_ww = Entry(login_frame, width=20)


### Button's
login = Button(login_frame, text="Login", command=lambda: login_check(entry_ww.get()), width=20)
register = Button(login_frame, text="register", width=20)
go_back = Button(login_frame, text="Go Back", command=reverse_pop_up, width=20)


### Packen van alle widgets
username.pack(pady=(50,0))
entry_username.pack(pady=6)

wachtwoord.pack()
entry_ww.pack(pady=6)
wacht_needs.pack(pady=7)

login.pack(pady=7)
register.pack(pady=7)
go_back.pack(pady=7)

###

### Header
steam_label = Label(top_frame, text='Steam', bg="skyblue4", fg="black",font=('Arial', 20, 'bold'))
steam_label.pack(side="left", padx=(680,0))

loginButton = Button(top_frame, text='Login', bg="skyblue4", fg="black",font=('Arial', 15, 'bold'), command=pop_up)
loginButton.pack(side="right", padx=(0,15))

###

### Lijst van games
listBox = Listbox(left_frame, width=50, bg="#FAF9F6", font=('Arial', 8))
listBox.pack(fill='y', side='left')

optionMenu = Listbox(left_frame, height=3, bg="#FAF9F6", font=('Arial', 9))
optionMenu.pack()
optionMenu.insert(1, "Alfabetische volgorde")
optionMenu.insert(2, "High->Low ratings")
optionMenu.insert(3, "Low->High ratings")

### zorgt ervoor dat listbox direct gevuled is
for i in lstSorter("name", False):
    listBox.insert('end', i)


### widget for listbox
searchbox = Entry(left_frame, bg="#FAF9F6", font=('Arial', 9))
searchbox.pack(pady=5)

update_lijst = Button(left_frame, width=20, text="Update lijst", bg="#FAF9F6", font=('Arial', 9), command=listbox)
update_lijst.pack(pady=7)

seleteren_button = Button(left_frame, width=20, text="Selecteren", bg="#FAF9F6", font=('Arial', 9), command=seleteren)
seleteren_button.pack(pady=5)


### sensor button (IT gedeeldte)
# sensor_button = Button(left_frame, width=20, text='Sensor aanzetten', bg="#FAF9F6", font=('Arial', 9), command=alarm_sensor)
# sensor_button.pack(pady=5)


root.mainloop()

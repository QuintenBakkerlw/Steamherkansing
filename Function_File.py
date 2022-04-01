import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from tkinter import *


def averageplayedGraph(frame, gamechosen):

    def getList():
        sortplayedhours = []

        ### convert txt file naar lijst ###
        with open("sortedHoursLst.txt", "r") as f:
            for line in f:
                sortplayedhours.append(int(line.strip()))
        return sortplayedhours

    ### opent en reads json file ###
    gameNameList = []
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)
    json_file.close()
    for game in data:
        ### append data met key "name" in lst ###
        gameNameList.append(game['name'])

    ### bestaat game in json file ##
    if gamechosen in gameNameList:
        ### pakt index van lijst ###
        indexJson = gameNameList.index(gamechosen)

        ### zoekt game op in json file met behulp van index ###
        dictionary = data[indexJson]
        keys_list = list(data)
        a_key = keys_list[indexJson]
        gameHour = a_key.get('average_playtime')
        sortplayedHours = getList()

        ### het maken van de grafiek ###
        if sortplayedHours.index(gameHour) >= 25750:
            fig1, ax1 = plt.subplots(figsize=(8, 5), dpi=70)
            plt.style.use('seaborn-talk')
            i = np.array(sortplayedHours)
            placement = np.arange(0, 27065)
            ax1.scatter(sortplayedHours.index(gameHour), gameHour, s=150, zorder=2, label=gamechosen, color='#346888')
            ax1.scatter(placement, i, s=12, label='Other games', color='#5886a5')
            plt.ylabel('Average playtime in log')
            plt.legend(loc='upper left')
            plt.title('Average playtime in games')
            plt.xlim(25750, 27250)
            plt.ylim(10 ** 2.5, 10 ** 5.2)
            plt.yscale("log")
            canvas = FigureCanvasTkAgg(fig1, master=frame)
            canvas.draw()
            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().grid(row=2)

        else:
            new_canvas = Canvas(master=frame, height=395, width=560, bg='azure4', highlightbackground="dimgrey", highlightthickness=5)
            new_canvas.grid(row=2)
            new_canvas.create_text(
                325, 200,
                font=("Arial", 16),
                text=f"Sorry, \nthis game doesn't have the\n required amount of hours for a graph.\n{gameHour} average played hours.")


def searchEngine(search):

    gameNameList = []
    ### opent en read de json file ###
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)
        for game in data:
            ### maakt een lijst van alle namen
            gameNameList.append(game["name"])

    searchedGames = []
    for x in gameNameList:
        ### kijkt of de input voor komt in de naam ###
        if search in x.lower():
            ### voegt de name toe aan lijst ###
            searchedGames.append(x)
    return searchedGames


def developerGraph(frame):

    ## functies ###############
    def KeySorter(onderwerp):
        myList = []
        with open("steam.json", "r") as json_file:
            data = json.load(json_file)
        for game in data:
            myList.append(game[onderwerp])
        return myList

    def freq(lst):
        sortlst = sorted(lst)
        dict = {}
        for x in sortlst:
            dict[x] = 0
        for x in sortlst:
            dict[x] += 1
        return dict

    ### Maakt een dictionary met het freqentie van de developer ###
    developerFreq = freq(KeySorter('developer'))

    freqeuntieLijst = []
    for aantal in developerFreq:
        ## pakt alleen de freqeuntie van developerFreq ###
        freqeuntieLijst.append(developerFreq[aantal])
    lstsorted = sorted(freqeuntieLijst)

    top6Developers = []
    ### pakt de top 6 developers ###
    for x in range(-6, 0):
        top6Developers.append(lstsorted[x])
    ### verwijdert verkeerde gevulde developer die niet bestaat ###
    top6Developers.remove(81)

    top5Developers = top6Developers
    top5names = []
    for i in top5Developers:
        findindex = freqeuntieLijst.index(i)
        keys_list = list(developerFreq)
        key = keys_list[findindex]
        top5names.append(key)

    ### Het maken van de Grafiek ###
    colors = ['#3E204F', '#5a4565', '#cec9d6', '#e2dbe9', '#bcaecc']
    explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots(figsize=(9, 6), dpi=65)
    ax1.pie(top5Developers, explode=explode, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    patches, texts = plt.pie(top5Developers, startangle=90, explode=explode, colors=colors)
    plt.legend(patches, top5names, loc="lower left", fontsize=10, bbox_to_anchor=(-0.1, -0.06))
    plt.title('Top5 Developers(most developed games on steam) \n 1.94% of total developers')
    canvas = FigureCanvasTkAgg(fig1, master=frame)
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=1)

    return


def lstSorter(object, reverse):
    gameNameList = []
    ### opent json file en read het ###
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)

    ### sorted de json file ###
    sortedList = sorted(data, key=lambda k: k[object], reverse=reverse)
    for game in sortedList:
        gameNameList.append(game['name'])
    return gameNameList


def game_info(gamechose):
    gameNameList = []
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)
    for game in data:
        gameNameList.append(game['name'])


    lst = []
    if gamechose in gameNameList:
        indexJson = gameNameList.index(gamechose)
        keys_list = list(data)
        a_key = keys_list[indexJson]
        with open("steam.json", "r") as json_file:
            data = json.load(json_file)
            dictionary = data[indexJson]
            lst.append(("release date", dictionary['release_date']))
            lst.append(("developer", dictionary['developer']))
            lst.append(("Publisher", dictionary['publisher']))
            lst.append(("Steam Tags", dictionary['steamspy_tags']))
            lst.append(("Platforms", dictionary['platforms']))
            lst.append(("Categories", dictionary['categories']))
            lst.append(("Genres", dictionary['genres']))
            lst.append(("Price", f"${dictionary['price']}"))
            lst.append(("Positive ratings", dictionary['positive_ratings']))
            lst.append(("Negative ratings", dictionary['negative_ratings']))

        return lst


speciaal = ('!', '@', '#', '$', '%', '^', '&', '*',)
nott = ('(', ')', '[', ']', '{', '}', '/')

def ww_check(wachtwoord):
    hasNumber = False
    hasSpeciaal = False
    hasKlein = False
    hasNott = False
    hasCapital = False
    lenhas = False
    wwjuist = False
    for x in wachtwoord:
        if x.isdigit():
            hasNumber = True
        if x.islower():
            hasKlein = True
        if x.isupper():
            hasCapital = True
        if x in speciaal:
            hasSpeciaal = True
        if x not in nott:
            hasNott = True
    if len(wachtwoord) >= 10 and len(wachtwoord) <= 20:
        lenhas = True
    if lenhas == True and hasNumber == True and hasKlein == True and hasCapital == True and hasSpeciaal == True and hasNott == True:
        wwjuist = True
        return wwjuist
    else:
        return wwjuist


def sorted_hours_maker():
    def nummer_sorter(lst):
        #### while statement True
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(lst) - 1):
                ########### Looks if element is greater then the next( + 1)
                if lst[i] > lst[i + 1]:
                    ########### swaps element ###########
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    ########### swapped set to True to loop ###########
                    swapped = True
            if swapped == False:
                return lst

    playedHours = []
    ########### puts average_playtime in a list ###########
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)
    for x in data:
        playedHours.append(x['average_playtime'])
    json_file.close()

    sorted_played_hours = nummer_sorter(playedHours)

    with open("sortedHoursLst.txt", 'w') as f:
        for s in sorted_played_hours:
            f.write(str(s) + '\n')
    f.close()




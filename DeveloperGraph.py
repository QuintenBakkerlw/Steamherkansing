import json
import matplotlib.pyplot as plt


def developerGraph():

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
    fig1, ax1 = plt.subplots()
    ax1.pie(top5Developers, explode=explode, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    patches, texts = plt.pie(top5Developers, startangle=90, explode=explode, colors=colors)
    plt.legend(patches, top5names, loc="lower left", fontsize=10, bbox_to_anchor=(-0.1, -0.06))
    plt.title('Top5 Developers(most developed games on steam) \n 1.94% of total developers')
    plt.show()
    ##################################
    return

print(developerGraph())
import json


def searchEngine():

    gameNameList = []
    ### opent en read de json file ###
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)
        for game in data:
            ### maakt een lijst van alle namen
            gameNameList.append(game["name"])

    search = input("search")
    searchedGames = []
    for x in gameNameList:
        ### kijkt of de input voor komt in de naam ###
        if search in x.lower():
            ### voegt de name toe aan lijst ###
            searchedGames.append(x)
    return searchedGames

print(searchEngine())
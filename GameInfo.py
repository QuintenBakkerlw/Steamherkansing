import json

gameNameList = []
with open("steam.json", "r") as json_file:
    data = json.load(json_file)
for game in data:
    gameNameList.append(game['name'])


gamechose = input('choose a game')

if gamechose in gameNameList:
    indexJson = gameNameList.index(gamechose)
    # print(gameNameList.index(gamechose))
    keys_list = list(data)
    a_key = keys_list[indexJson]
    # print(a_key)
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)
        dictionary = data[indexJson]
        print(dictionary)
else:
    print('Sorry could not find the game you are looking for :(')
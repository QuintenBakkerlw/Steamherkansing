import json
import pprint

def LstSorter(object, reverse):
    ### opent json file en read het ###
    with open("steam.json", "r") as json_file:
        data = json.load(json_file)

    ### sorted de json file ###
    sortedList = sorted(data, key=lambda k: k[object], reverse=reverse)
    return sortedList

pprint.pprint(LstSorter("positive_ratings", True))




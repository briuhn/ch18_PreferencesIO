import csv
import PresentationLayer

FILE_NAME = "preferences.txt"

def readFromFile():

    preferences_dictionary = {}
    try:
        with open(FILE_NAME , 'r')as file:
            for line in file:
                key, value = line.strip().split('|')
                if key == "autosave":
                    preferences_dictionary[key] = int(value)
                else:
                    preferences_dictionary[key] = value

    except FileNotFoundError:
        return {
            "name": "",
            "language": "English",
            "autosave": 5
        }
 
    return preferences_dictionary



def saveToFile(preferences_dictionary):
    with open(FILE_NAME, "w") as file:
        for key, value in preferences_dictionary.items():
            file.write(f"{key}|{value}\n")
    
                
        

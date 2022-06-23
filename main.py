import json
import pandas as pd

def make_json(csvFilePath, jsonFilePath):
    try:
        df = pd.read_csv (csvFilePath)
        df.to_json (jsonFilePath) #Save as json file
        myJson=df.to_json()
        return myJson
    except IOError:
            print("\nFile not accessible, check the file path\n") 

def print_json(jsonFilePath):
    try:
        file = open(jsonFilePath, "r")
        myJson = json.dumps(json.load(file), indent=4)
        file.close()
        print(myJson)
    except IOError:
            print("\nFile not accessible, check the file path\n")


def menu():
    print("\n[1] Upload File")
    print("[0] Exit\n")


menu()
option=int(input("Enter your choice: "))

while option!=0:
    if option==1:
        csvFilePath= input("Enter the CSV file path: ")
        stripped_string = csvFilePath.strip('"') #remove quotes
        jsonFilePath= input("\nEnter location to save the JSON file \n(If you want to save in the current location, type 1): ")
        if jsonFilePath=='1':
            jsonFilePath = r'output.json'
        else:
            jsonFilePath=jsonFilePath.strip('"')
        make_json(stripped_string, jsonFilePath)
        # print(make_json(stripped_string, jsonFilePath))
        if(make_json(stripped_string, jsonFilePath)):
            print("\nSaved as '"+jsonFilePath+"'")
            print_json(jsonFilePath)
    else:
        print("\nInvalid option")

    print()        
    menu()
    option=int(input("\nEnter your choice: "))

print("\nGOODBYE")





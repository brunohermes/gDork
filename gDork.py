from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import *

print ("""\r                                                                                         
                                                                
             88888888ba,                             88         
             88      `"8b                            88         
             88        `8b                           88         
 ,adPPYb,d8  88         88   ,adPPYba,   8b,dPPYba,  88   ,d8   
a8"    `Y88  88         88  a8"     "8a  88P'   "Y8  88 ,a8"    
8b       88  88         8P  8b       d8  88          8888[      
"8a,   ,d88  88      .a8P   "8a,   ,a8"  88          88`"Yba,   
 `"YbbdP"Y8  88888888Y"'     `"YbbdP"'   88          88   `Y8a  
 aa,    ,88                                                     
  "Y8bbdP"                                                      
""")

def newSearch():
    pdfName = input("File Name: ")
    ext = ['pdf','txt','py','js','doc', 'xlsx', 'csv', 'xls', 'docx']
    print("\nExamples of file extensions: ")
    print(ext)
    print("\nOr you can type a custom file extension.")
    extensao = input("File Extension: ")
    gDork = "inurl: " + extensao + " + filetype: " + extensao + " + intitle: " + pdfName
    PATH = "C:\Program Files (x86)\chromedriver.exe" #Chrome Driver Path (Change this to your new chromedriver directory if you are using a different path)
    driver = webdriver.Chrome(PATH)

#General
    driver.get("https://google.com")
    print("\n" + "Loading Results for: " + gDork + " on " + driver.title)
    gSearch = driver.find_element(By.NAME, "q")
    gSearch.send_keys(gDork)
    gSearch.send_keys(Keys.RETURN)
    gStats = driver.find_element(By.ID, "extabar")
    status = gStats.text
    print (status.splitlines()[0] + "\n")
    print("Type 'quit' for exitting gDork, or 'new' to start a new search.")
    command = input(">_ ")
    commands = ['new', 'quit']
#Recursive commands
    while(command != commands[1]):
        print("Wrong command, type 'help' to show all the commands.\n")
        print("Type 'quit' for exitting gDork, or 'new' to start a new search.\n")
        command = input(">_ ")
        if(command == commands[0]):
            newSearch()
        elif(command == commands[1]):
            print("Quitting...")
            break
newSearch()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import requests
import tkinter
import time

#Configure Window 1
window = tkinter.Tk()
window.title("Input Window")
window.geometry('500x500')
window.configure(bg='#002421')

def rlsYrJudger(yrRlsed):
    result = ""
    if yrRlsed >= 4 and yrRlsed < 6:
        result = "This game was created when the platform was created, probably one of the first ever games or a developer test site."
    elif yrRlsed >= 6 and yrRlsed < 13:
        result = "This game was created in the classic era of Roblox."
    elif yrRlsed >= 13 and yrRlsed < 16:
        result = "This game was created in the post-classic era of Roblox."
    elif yrRlsed >= 16 and yrRlsed < 20:
        result = "This game was created in the golden era of Roblox."
    elif yrRlsed >= 20 and yrRlsed < 22:
        result = "This game was created in the modern era of Roblox."
    elif yrRlsed >= 22:
        result = "This game is pretty fresh, and was created in the post-modern era of Roblox."
    return result

def playerCtJudger(playerCt):
    result = ""
    if playerCt >= 0 and playerCt < 100:
        result = "No one is here!"
    elif playerCt >= 100 and playerCt < 500:
        result = "This game is pretty barren."
    elif playerCt >= 500 and playerCt < 1000:
        result = "It's got some people, though it's still under the radar."
    elif playerCt >= 1000 and playerCt < 3000:
        result = "This is a solid game, likely known by many."
    elif playerCt >= 3000 and playerCt < 10000:
        result = "A pretty popular game, nice."
    elif playerCt >= 10000 and playerCt < 20000:
        result = "A very popular game! Known by many for sure."
    elif playerCt >= 20000 and playerCt < 50000:
        result = "Seems like this game is all the rage, must be a front page game."
    elif playerCt >= 50000 and playerCt < 100000:
        result = "This game must be one of the top games on the site!"
    elif playerCt >= 100000 and playerCt < 500000:
        result = "This game has too many players!"
    elif playerCt >= 500000:
        result = "How can the Roblox servers even handle this?"
    return result


def contains(item1, item2):
    if item1 in item2 or item1.upper() in item2 or item1.lower() in item2:
        return True
    return False

def getYear(dateCr):
    arr = dateCr.split("/")
    return int(arr[2][2:])

def judge():
    
    entryTxt = entry_URL.get()
    print("URL entered --> " + entryTxt)

    if "https://www.roblox.com/games" not in entryTxt:
        print("Invalid URL Entered!")
        return

    options = ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    #entryTxt
    try:
        driver.get(entryTxt)
    except:
        print("Invalid URL Entered!")
        return

    

    #waiting for page load
    time.sleep(5)

    #Gather Judging Data
    title = driver.find_element(By.CLASS_NAME, "game-name")
    description = driver.find_element(By.CLASS_NAME, "game-description")
    
    statistics = driver.find_elements(By.CSS_SELECTOR, ".builder-font .font-caption-body, .builder-font .font-caption-body:active, .builder-font .font-caption-body:focus, .builder-font .font-caption-body:hover, .builder-font .font-caption-body:link, .builder-font .font-caption-body:visited, .builder-font .tooltip .tooltip-inner, .builder-font .tooltip .tooltip-inner:active, .builder-font .tooltip .tooltip-inner:focus, .builder-font .tooltip .tooltip-inner:hover, .builder-font .tooltip .tooltip-inner:link, .builder-font .tooltip .tooltip-inner:visited")
    playerCtStrRaw = statistics[0]
    dateCreated = statistics[3]
    
    #Judge Player Count
    if "," in playerCtStrRaw.text:    
        arr = playerCtStrRaw.text.split(",")
        playerCtStr = arr[0] + arr[1]
    else:
        playerCtStr = playerCtStrRaw.text

    playerCt = int(playerCtStr)
    playerCtResult = playerCtJudger(playerCt)
    playerCt = "Players: " + playerCtStr

    #Judge Release Year
    
    yrRlsed = getYear(dateCreated.text)
    yrRlsedResult = rlsYrJudger(yrRlsed)
    yrRlsed = "Date Created: " + str(dateCreated.text)

    #Judge Pet Games
    
    petResults = None
    if contains("Pet", title.text) or contains("Pet", description.text):
        petResults = "Very likely chance that this game is RNG based, features something close to gambling, and has pretty low-effort gameplay."

    #Judge SCP Games

    scpResults = None
    if contains("SCP", title.text) or contains("SCP", description.text):
        scpResults = "SCP huh? Having fun being part of that somewhat niche fanbase? Me too, it's quite a cool place. :)"

    #Judge Tycoons

    tycResults = None
    if contains("Tycoon", title.text) or contains("Tycoon", description.text):
        tycResults = "Cool that you like growing an empire but go do it for real? You just keep waiting to keep buying more stuff mate."

    #Judge Simulators

    simResults = None
    if contains("Simulator", title.text) or contains("Simulator", description.text):
        simResults = "This is either a clicker game or the very repetitive \"do, earn, buy, reapeat\" cycle, or it may actually be a well-done simulator."

    #Judge Roleplay/RP Games (look in descriptions as well for string literals!)

    obbResults = None
    if contains("Obby", title.text) or contains("Obby", description.text):
        obbResults = "Parkour! Hope it's challenging. :)"

    #Judge Obbies

    rpResults = None
    if contains("RP", title.text) or contains("RP", description.text) or contains("Roleplay", title.text) or contains("Roleplay", description.text):
        rpResults = "So do you have the friends to be playing this, or are you just trolling on here? Also watch out for ODers, they're quite annoying."

    driver.quit()

    renderResults(playerCt, playerCtResult, yrRlsed, yrRlsedResult, petResults, scpResults, tycResults, simResults, obbResults, rpResults)
    

def renderResults(*valsNRslts): #Use arbitrary arguments
    #Window 2
    display = tkinter.Tk()
    display.title("Result Window")
    display.geometry('500x500')
    display.configure(bg='#002421')
    
    render = [None] * len(valsNRslts) 

    #Create Elements (for handling arbitrary arguments, create an array and assign each element a label, then grid them all in another for loop)
    for i in range(len(valsNRslts)):
        if valsNRslts[i] == None:
            continue; 
        render[i] = tkinter.Label(display, text=valsNRslts[i], bg='#424242', fg='#FFFFFF', pady=3, padx=3)
    
    #Render Elements
    for i in range(len(render)):
        if render[i] == None:
            continue; 
        render[i].grid(row=i, column=0)

    display.mainloop()





#Create Elements
enter_URL = tkinter.Label(window, text="Enter Game URL:", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
entry_URL = tkinter.Entry(window)
button_calculate = tkinter.Button(window, text="Calculate", command=judge)

#Render the elements
enter_URL.grid(row=0, column=0)
entry_URL.grid(row=1, column=0)
button_calculate.grid(row=1, column=1)

window.mainloop()

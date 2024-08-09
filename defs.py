from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from datetime import date
import tkinter
import time


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

def lastUpdJudger(lastCh):
    result = ""
    if lastCh >= 0 and lastCh < 8:
        result = "This game is pretty actively maintained!"
    elif lastCh >= 8 and lastCh < 31:
        result = "This game is active, updates tend to take some time to come out though. The sweet spot."
    elif lastCh >= 31 and lastCh < 91:
        result = "This game is likely working on a huge update, just had one. Maybe some planning is taking place."
    elif lastCh >= 91 and lastCh < 181:
        result = "Is this game undergoing a total revamp? Either that or the dev seems like he forgot about it."
    elif lastCh >= 181 and lastCh < 365:
        result = "The game has not been updated in a long time, likely finished or the dev seems to have forgotten."
    elif lastCh >= 365:
        result = "Boy, you must be a skeleton by now waiting for a new update, right?"
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

def splitDate(date):
    return date.split("/")

def daysBetween(date1, date2):
    return ((date1 - date2).days if date1 > date2 else (date2 - date1).days)

def judge(entry_URL, invalid):
    entryTxt = entry_URL.get()
    print("\nURL entered --> " + entryTxt)

    if "https://www.roblox.com/games" not in entryTxt:
        print("Invalid URL Entered!")
        invalid.grid(row=4, column=0, pady = 3)
        return

    options = ChromeOptions()
    options.add_argument("--headless")
    driver = Chrome(options=options)
    #entryTxt
    try:
        driver.get(entryTxt)
    except:
        print("Invalid URL Entered!")
        invalid.grid(row=4, column=0, pady = 3)
        return

    

    #waiting for page load
    time.sleep(5)

    #Gather Judging Data
    title = driver.find_element(By.CLASS_NAME, "game-name")
    temp = driver.find_elements(By.CSS_SELECTOR, ".builder-font .font-bold, .builder-font .font-bold:active, .builder-font .font-bold:hover, .builder-font .font-bold:link, .builder-font .font-bold:visited, .builder-font .font-header-2, .builder-font .font-header-2:active, .builder-font .font-header-2:hover, .builder-font .font-header-2:link, .builder-font .font-header-2:visited, .builder-font .h5, .builder-font .h5:active, .builder-font .h5:hover, .builder-font .h5:link, .builder-font .h5:visited, .builder-font .h6, .builder-font .h6:active, .builder-font .h6:hover, .builder-font .h6:link, .builder-font .h6:visited, .builder-font .text-footer-nav, .builder-font .text-footer-nav:active, .builder-font .text-footer-nav:hover, .builder-font .text-footer-nav:link, .builder-font .text-footer-nav:visited, .builder-font .text-label, .builder-font .text-label:active, .builder-font .text-label:hover, .builder-font .text-label:link, .builder-font .text-label:visited, .builder-font .text-lead, .builder-font .text-lead:active, .builder-font .text-lead:hover, .builder-font .text-lead:link, .builder-font .text-lead:visited, .builder-font .text-name, .builder-font .text-name:active, .builder-font .text-name:hover, .builder-font .text-name:link, .builder-font .text-name:visited, .builder-font .text-subject, .builder-font .text-subject:active, .builder-font .text-subject:hover, .builder-font .text-subject:link, .builder-font .text-subject:visited, .builder-font .text-warning, .builder-font .text-warning:active, .builder-font .text-warning:hover, .builder-font .text-warning:link, .builder-font .text-warning:visited, .builder-font h5, .builder-font h5:active, .builder-font h5:hover, .builder-font h5:link, .builder-font h5:visited, .builder-font h6, .builder-font h6:active, .builder-font h6:hover, .builder-font h6:link, .builder-font h6:visited, .builder-font strong, .builder-font strong:active, .builder-font strong:hover, .builder-font strong:link, .builder-font strong:visited")
    devs = temp[13]
    
    titleCnt = title.text
    devsCnt = devs.text
    
    description = driver.find_element(By.CLASS_NAME, "game-description")
    
    descCnt = description.text

    statistics = driver.find_elements(By.CSS_SELECTOR, ".builder-font .font-caption-body, .builder-font .font-caption-body:active, .builder-font .font-caption-body:focus, .builder-font .font-caption-body:hover, .builder-font .font-caption-body:link, .builder-font .font-caption-body:visited, .builder-font .tooltip .tooltip-inner, .builder-font .tooltip .tooltip-inner:active, .builder-font .tooltip .tooltip-inner:focus, .builder-font .tooltip .tooltip-inner:hover, .builder-font .tooltip .tooltip-inner:link, .builder-font .tooltip .tooltip-inner:visited")    
    genre = statistics[6].text
    playerCtStrRaw = statistics[0]
    dateCreated = statistics[3]
    dateLastChanged = statistics[4]
    
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
    
    yrRlsed = int(splitDate(dateCreated.text)[2][2:])
    yrRlsedResult = rlsYrJudger(yrRlsed)
    yrRlsed = "Date Created: " + str(dateCreated.text)

    #Judge Last Changed Date

    yrChanged = splitDate(dateLastChanged.text)
    yrChangedDate = date(int(yrChanged[2]), int(yrChanged[0]), int(yrChanged[1]))
    today = date.today()
    yrChanged = daysBetween(yrChangedDate, today)
    yrChangedResult = lastUpdJudger(int(yrChanged)) 
    yrChanged = "Last updated: " + str(daysBetween(yrChangedDate, today)) + " days ago"

    #Judge Pet Games
    
    petResults = None
    if contains("Pet", titleCnt) or contains("Pet", descCnt):
        petResults = "Very likely chance that this game is RNG based, features something close to gambling, and has pretty low-effort gameplay."

    #Judge SCP Games

    scpResults = None
    if contains("SCP", titleCnt) or contains("SCP", descCnt):
        scpResults = "SCP, huh? Having fun being part of that somewhat niche fanbase? Interesting. :)"

    #Judge Tycoons

    tycResults = None
    if contains("Tycoon", titleCnt) or contains("Tycoon", descCnt):
        tycResults = "Cool that you like growing an empire but go do it for real? You just keep waiting to keep buying more stuff mate."

    #Judge Simulators

    simResults = None
    if contains("Simulator", titleCnt) or contains("Simulator", descCnt):
        simResults = "This is either a clicker game or the very repetitive \"do, earn, buy, reapeat\" cycle, or it may actually be a well-done simulator."

    #Judge Obbies
    obbResults = None
    if contains("Obby", titleCnt) or contains("Obby", descCnt):
        obbResults = "Parkour! Hope it's challenging. :)"

    #Judge Roleplay/RP Games (look in descriptions as well for string literals!)
    rpResults = None
    if contains("RP", titleCnt) or contains("RP", descCnt) or contains("Roleplay", titleCnt) or contains("Roleplay", descCnt):
        rpResults = "So do you have the friends to be playing this, or are you just trolling on here? Also watch out for ODers, they're quite annoying."
    
    #Judge Genres
    genreTxt = "Genre: " + genre 
    
    #Judge FPS
    fpsResults = None
    if contains("FPS", genre):
        fpsResults = "Ooh an FPS game? Either inspired by COD, COD Zombies, COD Gun Game, boomer shooters, or, quite rarely, it's its own thing."
    
    #Judge Fighting
    fightResults = None
    if contains("Fighting", genre):
        fightResults = "Probably a mislisted FPS game, or even better, swordsplay/medival combat or melee combat."

    #Judge All Genres
    allGenreResults = None
    if contains("All Genres", genre):
        allGenreResults = "Really? Is the dev really that lazy to not list a genre for his game? Well I suppose it really could be \"All Genres,\" you never know."
    
    #Judge Adventure
    advResults = None
    if contains("Adventure", genre):
        advResults = "Either a very underwhelming \"Adventure,\" or maybe something actually decent. Maybe something that's not even a proper adventure at all!"

    #Judge RPG
    rpgResults = None
    if contains("RPG", genre):
        rpgResults = "Interesting, some of these may be classified under Adventure. Don\'t these get quite grindy at times?"



    renderResults(titleCnt, devsCnt, playerCt, playerCtResult, yrRlsed, yrRlsedResult, yrChanged, yrChangedResult, petResults, scpResults, tycResults, simResults, obbResults, rpResults, genreTxt, fpsResults, fightResults, allGenreResults, advResults, rpgResults)
    

def renderResults(*valsNRslts): #Use arbitrary arguments
    #Window 2
    display = tkinter.Tk()
    display.title("Result Window")
    display.configure(bg='#002421')
    
    title = "Game: " + valsNRslts[0]
    devs = "Developers: " + valsNRslts[1]
    renderTitle = tkinter.Label(display, text=title, bg='#424242', fg='#FFFFFF', pady=3, padx=3)
    renderDevs = tkinter.Label(display, text=devs, bg='#424242', fg='#FFFFFF', pady=3, padx=3)

    render = [None] * len(valsNRslts) 

    #Create Elements (for handling arbitrary arguments, create an array and assign each element a label, then grid them all in another for loop)
    for i in range(len(valsNRslts)):
        if valsNRslts[i] == None or i <= 1:
            continue; 
        render[i] = tkinter.Label(display, text=valsNRslts[i], bg='#424242', fg='#FFFFFF', pady=3, padx=3)
    
    #Render Elements 
    renderTitle.grid(row=0, column=0, padx = 3, pady = 3)
    renderDevs.grid(row=1, column=0, padx = 3, pady = 3)
    
    for i in range(len(render)):      
        if render[i] == None or i <= 1:
            continue
        render[i].grid(row=i, column=0, padx = 3, pady = 3)

    display.mainloop()
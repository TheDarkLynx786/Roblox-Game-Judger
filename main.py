from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import requests
import tkinter
import time

#Configure Window 1
window = tkinter.Tk()
window.title("Stoopid Project LOL")
window.geometry('500x500')
window.configure(bg='#002421')

def judge(entryTxt = "https://www.roblox.com/games/12411473842/Pressure"):
    


    options = ChromeOptions()
    #options.add_argument("--headless")
    driver = Chrome(options=options)
    #entryTxt
    driver.get("https://www.roblox.com/games/12411473842/Pressure")

    #waiting for page load
    time.sleep(5)

    playerCtStrRaw = driver.find_element(By.CSS_SELECTOR, ".builder-font .font-caption-body, .builder-font .font-caption-body:active, .builder-font .font-caption-body:focus, .builder-font .font-caption-body:hover, .builder-font .font-caption-body:link, .builder-font .font-caption-body:visited, .builder-font .tooltip .tooltip-inner, .builder-font .tooltip .tooltip-inner:active, .builder-font .tooltip .tooltip-inner:focus, .builder-font .tooltip .tooltip-inner:hover, .builder-font .tooltip .tooltip-inner:link, .builder-font .tooltip .tooltip-inner:visited")


    arr = playerCtStrRaw.text.split(",")
    playerCtStr = arr[0] + arr[1]

    result = ""
    
    playerCt = int(playerCtStr)
    
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
    

    driver.quit()

    renderResults(playerCt, result)

    


    

def renderResults(playerCt, result):
    #Window 2
    display = tkinter.Tk()
    display.title("Stoopid Results LOL")
    display.geometry('500x500')
    display.configure(bg='#002421')
    
    playerCtTxt = "Players: " + str(playerCt)
    
    #Create Elements
    renderPlayers = tkinter.Label(display, text=playerCtTxt, bg='#424242', fg='#FFFFFF', pady=3, padx=3)
    renderResult = tkinter.Label(display, text=result, bg='#424242', fg='#FFFFFF', pady=3, padx=3)

    #Render Elements
    renderPlayers.grid(row=0,column=0)
    renderResult.grid(row=1,column=0)

    display.mainloop()





#Create Elements
enter_URL = tkinter.Label(window, text="Enter Game URL:", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
entry_URL = tkinter.Entry(window)
entryTxt = entry_URL.get()
print(entryTxt)
button_calculate = tkinter.Button(window, text="Calculate", command= lambda: judge(entryTxt))

#Render the elements
enter_URL.grid(row=0, column=0)
entry_URL.grid(row=1, column=0)
button_calculate.grid(row=1, column=1)

window.mainloop()

from bs4 import BeautifulSoup
import requests
import tkinter

#Configure Window 1
window = tkinter.Tk()
window.title("Stoopid Project LOL")
window.geometry('500x500')
window.configure(bg='#002421')

def judge():
    page = requests.get(entry_URL.get())
    try:
        soup = BeautifulSoup(page.text, "html.parser")
    except:
        print("Invalid URL Entered. Make sure you enter the URL of a Roblox game!")
    
    title = soup.findAll("h1", attrs={"class":"game-name"})
    dev = soup.findAll("a", attrs={"class":"text-name text-overflow"})

    #Window 2
    display = tkinter.Tk()
    display.title("Stoopid Results LOL")
    display.geometry('500x500')
    display.configure(bg='#002421')
    

    
    #Create Elements
    renderTitle = tkinter.Label(display, text=title[0].text, bg='#424242', fg='#FFFFFF', pady=3, padx=3)
    renderDev = tkinter.Label(display, text=dev[0].text, bg='#424242', fg='#FFFFFF', pady=3, padx=3)

    #Render Elements
    renderTitle.grid(row=0,column=0)
    renderDev.grid(row=1,column=0)

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
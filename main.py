import tkinter
import defs

def begin():
    loading.grid(row=3, column=0, pady = 3)
    defs.judge(entry_URL, invalid)

#Configure Window 1
window = tkinter.Tk()
window.title("Input Window")
window.configure(bg='#002421')

#Create Elements (Window 1)
enter_URL = tkinter.Label(window, text="Enter Game URL:", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
entry_URL = tkinter.Entry(window)
loading = tkinter.Label(window, text="Give it about 10 seconds, and your results should appear.", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
invalid = tkinter.Label(window, text="Invalid URL Entered! Only enter the URLs of Roblox Game Pages!", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
button_calculate = tkinter.Button(window, text="Calculate", command=begin)

#Render the elements (Window 1)
enter_URL.grid(row=0, column=0)
entry_URL.grid(row=1, column=0)
button_calculate.grid(row=2, column=0)

window.mainloop()

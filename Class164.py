from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

def getImg(imgName):
    return ImageTk.PhotoImage(Image.open(imgName))

planetInfo = {
    'Mercury': ['2,440.5', '3.7', '0', 'Rocky'],
    'Venus': ['6,051.8', '8.87', '0', 'Rocky'],
    'Earth': ['6,378.14', '9.82', '1', 'Rocky'],
    'Mars': ['3,396.2', '3.73', '2', 'Rocky'],
    'Jupiter': ['71,492', '25.92', '92', 'Gas'],
    'Saturn': ['60,268', '11.19', '83', 'Gas'],
    'Uranus': ['25,559', '9.01', '27', 'Gas'],
    'Neptune': ['24,764', '11.27', '14', 'Gas']
}

images = []
for i in list(planetInfo.keys()):
    print(i)
    images.append(getImg(f'Class164+/{ i }.png'))

root = Tk()
root.title('Solar Encyclopedia')
root.geometry('400x400')
root.configure(background = 'snow')

lblName = Label(root, text = 'Planet:', bg = 'light blue')
lblName.place(relx = 0.25, rely = 0.1, anchor = CENTER)
lblImg = Label(root, bg = 'light blue', highlightthickness = 5)
lblImg.place(relx = 0.5, rely = 0.5, anchor = CENTER)

lblInfo = Label(root, text = '', bg = 'light blue')
lblInfo.place(relx = 0.5, rely = 0.75, anchor = CENTER)

selectPlanet = StringVar()
drdName = ttk.Combobox(root, values = list(planetInfo.keys()), textvariable = selectPlanet)
drdName.place(relx = 0.5, rely = 0.1, anchor = CENTER)

def getInfo():
    text = ''
    info = planetInfo.get(selectPlanet.get())
    
    text += f'Radius: { info[0] } km\n'
    text += f'Gravity: { info[1] } m/s^2\n'
    text += f'Number Of Natural Satellites: { info[2] }\n'
    text += f'Type Of Planet: { info[3] }'
    
    lblInfo['text'] = text

btnGetInfo = Button(root, text = 'Get Planet Info', bg = 'snow', command = lambda: getInfo())
btnGetInfo.place(relx = 0.5, rely = 0.2, anchor = CENTER)

root.mainloop()
import PySimpleGUI as sg

sg.theme('LightYellow')

layout  = [[sg.T("")],[sg.Button('Hello World!',size=(20,4))],[sg.Text("  ")],
[sg.Button('Winter Olympics 2022 (Beijing)'), sg.Button('Summer Olympics 2021 (Tokyo)')],[sg.Text(" ")],
[sg.Button('Fifa World Cup 2022 (Qatar)'), sg.T(" "*2),sg.Button('Tour de France')]]

window = sg.Window('Bunch of Buttons', layout, size=(420,250))
event, values = window.read()

##########Button Functions##########
while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Hello World!':
        print("Hello World!")      # call the "Callback" function
    elif event == 'Winter Olympics 2022 (Beijing)':
        print("Winter Olympics 2022 (Beijing)")
    elif event == 'Summer Olympics 2021 (Tokyo)':
        print("Summer Olympics 2021 (Tokyo)")
    elif event == 'Tour de France':
        print("Tour de France")
    elif event == 'Fifa World Cup 2022 (Qatar)':
        print("Fifa World Cup 2022 (Qatar)")
from ast import Break
from curses import window
import PySimpleGUI as sg


layout=[
    [sg.Text("User")],
    [sg.Input(key ="User")],
    [sg.Text('Password')],
    [sg.Input(key ="Password")],
    [sg.Button('login')],
    [sg.Text('',key ="mensagem")],
]

window = sg.Window('login',layout=layout)

while True:
   event, values = window.read()
   if event == sg.WINDOW_CLOSED:
       break 
   elif event == 'login':
        user = values ['User']
        password= values ['Password']
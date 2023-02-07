import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
#layout = [  [sg.Text('Some text on Row 1')],
            #[sg.Text('Enter something on Row 2'), sg.InputText()],
            #[sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
#window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
#while True:
    #event, values = window.read()
    #if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        #break
    #print('You entered ', values[0])

#window.close()

layout = [  [sg.Text("You've not been hacked, dummy")], [sg.Button('Say what') ]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event== 'Say what':
        layout = [[sg.Text('I said NOT.')],[sg.Button('Ohk')]]
        window = sg.Window('Window Title', layout)
        event, values = window.read()
        if event== 'Ohk':
            layout = [[sg.Text('I just have a question for you...')],[sg.Button('Elaborate') ]]
            window = sg.Window('Window Title', layout)
            event, values = window.read()
            
            if event== 'Elaborate':
                layout = [[sg.Text('Will you be my valentine? Say yes.')],[sg.Button('Yes'), sg.Button('No') ]]
                window = sg.Window('Window Title', layout)
                event, values = window.read()
                while (event == 'No'):
                    layout = [[sg.Text('Please')],[sg.Button('Yes'),sg.Button('No')]]
                    window = sg.Window('Window Title', layout)
                    event, values = window.read()
                    if (event == 'Yes'):
                        layout = [[sg.Text("You won't regret this decision")],[sg.Button('Hmm')]]
                        window = sg.Window('Window Title', layout)
                        event, values = window.read()
                        if (event=='Hmm'):
                            window.close()
            else:
                break
            
        else: # if user closes window or clicks cancel
            break
                    
                    
        
    elif (event == sg.WIN_CLOSED or event == 'Cancel'): # if user closes window or clicks cancel
        break
        print('You entered ', values[0])

window.close()

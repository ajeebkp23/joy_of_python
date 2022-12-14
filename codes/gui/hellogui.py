import PySimpleGUI as sg

sg.theme("DarkAmber")  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text("Some text on Row 1")],
    [sg.Text("Enter something on Row 2"), sg.InputText()],
    [sg.Button("Ok"), sg.Button("Cancel")],
]

# Create the Window
window = sg.Window("Window Title", layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if user closes window or clicks cancel
        break
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    print("You entered ", values[0])
    # window.layout.insert(2,[sg.Text()])
    sg.popup(f"You entered: {values[0]}")

window.close()

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("To-do Desktop",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

todos = functions.get_todos()

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()


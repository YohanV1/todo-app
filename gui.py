import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

clock = sg.Text('', key='clock', background_color='#413F42', text_color='#E5E5CB', font="Helvetica 20 underline")
label = sg.Text("Type in a to-do: ", background_color='#413F42', text_color='#E5E5CB')
input_box = sg.InputText(tooltip="Enter to-do", key="todo", background_color='#BBBBBB')
add_button = sg.Button("Add", button_color=('#E5E5CB', '#7F8487'), border_width=0)
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(40, 10), background_color='#BBBBBB', text_color='#0A2647')
edit_button = sg.Button("Edit", button_color=('#E5E5CB', '#7F8487'), border_width=0)
complete_button = sg.Button("Complete", button_color=('#E5E5CB', '#7F8487'), border_width=0)
exit_button = sg.Button("Exit", button_color=('#E5E5CB', '#7F8487'), border_width=0)

window = sg.Window("To-Do Desktop",
                   layout=[[clock], [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('American typewriter', 20),
                   background_color='#413F42')

todos = functions.get_todos()

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:

        case "Add":
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",
                         font=('Helvetica', 20))

        case "todos":
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                continue

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.",
                         font=('Helvetica', 20))

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()


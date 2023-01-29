import functions
import time

while True:
    print(time.strftime("It is %b %d, %Y %H:%M"))
    user_action = input("Type in add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo+'\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index+1}-{item}"
            print(row, end="")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid input!")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)

            functions.write_todos(todos)

            print(f"'{todo_to_remove}' was removed from the list")
        except IndexError:
            print("There is no item with that number!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Unknown Command!")

print("Bye!")
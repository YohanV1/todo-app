import sqlite3


def create_table():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todos
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  todo_text TEXT NOT NULL);''')
    conn.commit()
    conn.close()


def get_todos():
    """ Read the to-do items from the SQLite3 database and return a list. """
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT todo_text FROM todos;')
    todos_local = [row[0] for row in cursor.fetchall()]
    conn.close()
    return todos_local


def write_todos(todos_arg):
    """ Insert or update the to-do items in the SQLite3 database. """
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos;')  # Clear the existing rows in the table
    for todo_text in todos_arg:
        cursor.execute('INSERT INTO todos (todo_text) VALUES (?);', (todo_text,))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_table()


import pickle
from lib.todos import Todo
def todo_list_definer() -> list:
    try:
        file = open("datas/todo_data.pickle", "rb")
        todo_list = pickle.load(file)
    except:
        todo_list = []
        file = open("datas/todo_data.pickle", "wb")
        pickle.dump(todo_list,file)
    return todo_list
def update(todo_list: list):
    file = open("datas/todo_data.pickle", "wb")
    pickle.dump(todo_list,file)
def print_todos(todo_list: list):
    alt_cizgi = ""
    ust_cizgi = ""
    for i in range(38):
        alt_cizgi += "_"
        ust_cizgi += "¯"
    print(alt_cizgi)
    for i, x in enumerate(todo_list):
        if i < 10:
            print(str(i) + " " + " | " + str(x))
        else:
            print(str(i) + " | " + str(x))
    print(alt_cizgi)
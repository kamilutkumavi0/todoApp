import pickle
from lib import funcs, todos, date

todo_list = funcs.todo_list_definer()

#ana ekran
if __name__ == "__main__":
    todo_list = funcs.todo_list_definer()
    print(todo_list)
  
    while True:
 
        print("""
1. Görev Ekle
2. Görev Göster
3. Görev Sil
4. Çıkış
            """)

        a = input("Seçiminiz (1/2/3/4) ")
        if a == "4":
            break
        elif a == "1":
            todo_mission = input("Görev girin: ")
            todo_priority = int(input("Görevin önceliğini girin: "))
            new_todo = todos.Todo(todo_mission, todo_priority)
            todo_list.append(new_todo)
            todo_list.sort(reverse=True)
            funcs.update(todo_list)
        elif a == "2":
            funcs.print_todos(todo_list)
        elif a == "3":
            funcs.print_todos(todo_list)
            silinecek_index = int(input("\nSilinecek görevin indexini yazınız: "))
            todo_list.pop(silinecek_index)
            todo_list.sort(reverse=True)
            funcs.update(todo_list)

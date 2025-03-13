class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Fügt eine Aufgabe zur To-Do-Liste hinzu."""
        self.tasks.append(task)
        print(f'Aufgabe hinzugefügt: "{task}"')

    def show_tasks(self):
        """Zeigt alle Aufgaben in der To-Do-Liste an."""
        if not self.tasks:
            print("Keine Aufgaben vorhanden.")
        else:
            print("Deine To-Do-Liste:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_number):
        """Entfernt eine Aufgabe aus der To-Do-Liste."""
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Aufgabe entfernt: "{removed_task}"')
        else:
            print("Ungültige Aufgabennummer.")

def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do-Liste ---")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe entfernen")
        print("4. Beenden")

        choice = input("Wähle eine Option: ")

        if choice == "1":
            task = input("Gib die Aufgabe ein: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            task_number = int(input("Gib die Nummer der Aufgabe ein, die du entfernen möchtest: "))
            todo_list.remove_task(task_number)
        elif choice == "4":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
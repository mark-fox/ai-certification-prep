from datetime import datetime  

def add_note():
    note = input("Enter your note: ").strip()
    if not note:
        print("Note cannot be empty.")
        return
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")  # Add timestamp
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"{timestamp} {note}\n")  # Save note with timestamp
    print("Note added!")


def view_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes found.")

def delete_note():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        if not notes:
            print("No notes to delete.")
            return

        print("\nWhich note would you like to delete?")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note.strip()}")

        choice = input("Enter the note number to delete: ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(notes):
            print("Invalid choice.")
            return

        index = int(choice) - 1
        deleted = notes.pop(index)

        with open("notes.txt", "w") as f:
            f.writelines(notes)

        print(f"Deleted: {deleted.strip()}")

    except FileNotFoundError:
        print("No notes found.")

def delete_by_phrase():
    phrase = input("Enter a phrase to search for: ").strip()
    if not phrase:
        print("Phrase cannot be empty.")
        return

    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()

        matches = [(i, note) for i, note in enumerate(notes) if phrase.lower() in note.lower()]
        if not matches:
            print("No matching notes found.")
            return

        print("\nMatching Notes:")
        for i, (index, note) in enumerate(matches):
            print(f"{i+1}. {note.strip()}")

        to_delete = input("Enter the number of the note to delete (or 'all' to delete all matches): ").strip()
        if to_delete.lower() == 'all':
            indices_to_delete = [index for index, _ in matches]
        elif to_delete.isdigit() and 1 <= int(to_delete) <= len(matches):
            indices_to_delete = [matches[int(to_delete)-1][0]]
        else:
            print("Invalid selection.")
            return

        updated_notes = [note for i, note in enumerate(notes) if i not in indices_to_delete]
        with open("notes.txt", "w", encoding="utf-8") as file:
            file.writelines(updated_notes)

        print("Note(s) deleted.")

    except FileNotFoundError:
        print("No notes found.")

def main():
    while True:
        print("\n[1] Add note  [2] View notes  [3] Delete note [4] Delete by phrase [5] Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            delete_by_phrase()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

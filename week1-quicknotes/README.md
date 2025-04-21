# 🗒️ QuickNotes CLI App

A simple command-line tool for creating, viewing, and managing text notes. Built as part of my AI engineering prep to reinforce core Python skills like file handling, user input, and CLI interaction.

## 🚀 Features

- ✅ Add notes with automatic timestamps
- ✅ View all saved notes
- ✅ Delete a note by number
- ✅ Delete a note by matching phrase (full or partial)
- ✅ Stored in a local text file (`notes.txt`)

## 📦 How to Run

1. Make sure you have Python 3 installed.
2. Open your terminal and navigate to this folder.
3. Run the app:

```bash
python quicknotes.py
```
## Sample Output
```
[1] Add note
[2] View notes
[3] Delete by number
[4] Delete by phrase
[5] Quit

Enter your choice: 1
Enter your note: Finish this week's project
Note added!

[2025-04-21 13:42] Finish this week's project
```
## 🛠 Skills Practiced
Python file I/O

CLI menu design

datetime module

Searching/filtering lists

Simple terminal interactivity

## 🧠 Future Improvements
Search-only mode

Edit note by number

Export/import notes

Turn into a Flask/Streamlit web app
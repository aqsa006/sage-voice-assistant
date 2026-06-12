from datetime import datetime
import os

def save_note(note):
    
    os.makedirs("notes", exist_ok=True)
    filename = datetime.now().strftime("%Y-%m-%d") + ".txt"
    filepath = os.path.join("notes", filename)

    with open(filepath, "a") as file:
        time = datetime.now().strftime("%H:%M")
        file.write(f"[{time}] {note}\n")

def open_note():
    filename = datetime.now().strftime("%Y-%m-%d") + ".txt"
    filepath = os.path.join("notes", filename)
    os.startfile(filepath)


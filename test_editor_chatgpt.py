import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
        text_edit.insert(tk.END, text)
    window.title(f"AlmdrasaTextEditor - {filepath}")
    status_bar.config(text=f"Opened: {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as file:
        text = text_edit.get(1.0, tk.END)
        file.write(text)
    window.title(f"AlmdrasaTextEditor - {filepath}")
    status_bar.config(text=f"Saved: {filepath}")

def exit_app():
    window.quit()

window = tk.Tk()
window.title("Almdrasa Text Editor")
window.geometry("900x600")

menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

text_edit = tk.Text(window, wrap="word", font=("Arial", 14))
text_edit.pack(fill="both", expand=True, padx=5, pady=5)


status_bar = tk.Label(window, text="Welcome to Almdrasa Text Editor", anchor="w", relief="sunken")
status_bar.pack(fill="x", side="bottom")


window.mainloop()


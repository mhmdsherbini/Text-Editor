import tkinter as tk
from  tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"),("All Files", "*.*") ])
    
    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)
    
    window.title(f"AlmdrasaTextEditor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"),("All Files", "*.*") ])
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0, tk.END)
        output_file.write(text)
        
    window.title(f"AlmdrasaTextEditor - {filepath}")



window = tk.Tk()
window.title("Almdrasa text editor")
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=800)



text_edit = tk.Text(window)
fram_buttons = tk.Frame(window, relief=tk.RAISED)
btn_open = tk.Button(fram_buttons, text="Open file", command=open_file)
btn_save = tk.Button(fram_buttons, text="Save As", command= save_file)


btn_open.grid(column=0, row=0, padx=5, pady=5, sticky="ew" )
btn_save.grid(column=0, row=1, padx=5, pady=5, sticky="ew")

fram_buttons.grid(column= 0 , row =0, sticky="nw")
text_edit.grid(column=1, row=0, sticky= "nsew") 
window.mainloop()

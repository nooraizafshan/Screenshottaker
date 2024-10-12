import pyautogui
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def take_ss():
    add_data = entry.get()
    if add_data:
        path = filedialog.askdirectory() + '/' + add_data + '.png'
        ss = pyautogui.screenshot()
        ss.save(path)
        messagebox.showinfo("Success", f"Screenshot saved at {path}")
    else:
        messagebox.showwarning("Input Error", "Please enter a filename")

# Initialize the main window
win = Tk()
win.title('Screenshot Taker')
win.geometry('700x400')
win.config(bg='#2C3E50')
win.resizable(False, False)

# Add a frame for better layout
frame = Frame(win, bg='#34495E')
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)

# Add an entry for the filename
entry_label = Label(frame, text="Enter filename:", font=('Helvetica', 14), bg='#34495E', fg='white')
entry_label.pack(pady=10)
entry = Entry(frame, font=('Helvetica', 18))
entry.pack(pady=10, padx=20, fill=X)

# Add a button to take the screenshot
button = Button(frame, text='Take Screenshot', font=('Helvetica', 16), bg='#1ABC9C', fg='white', command=take_ss)
button.pack(pady=20)

# Start the GUI loop
win.mainloop()

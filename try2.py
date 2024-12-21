import tkinter as tk

window = tk.Tk()
window.title("Hello World")

def handle_button_press(event):
    window.destroy()

button = tk.Button(text="My simple app.")
button.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button.pack()

button1 = tk.Button(text="FNCS")
button1.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button1.pack()

# Start the event loop.
window.mainloop()
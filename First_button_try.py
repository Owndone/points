import tkinter as tk

kills = 0
window = tk.Tk()
window.title("Fortnite points calculator")

def handle_button_press(event):
    window2 = tk.Tk()
    window2.title("FNCS points calculator")
    window2.mainloop()
    say_calculator(5)

def say_calculator(kills):
    if kills == '':
        print("You didn't enter your kills!")
    else:
        points = kills * 2
        print(kills)

button1 = tk.Button(text="FNCS")
button1.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button1.pack()

lable1 = tk.Label(text="Enter your kills: ")
lable1.pack()
lable2 = tk.Label(textvariable=kills)
lable2.pack()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Start the event loop.
window.mainloop()



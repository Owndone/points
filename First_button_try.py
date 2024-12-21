import tkinter as tk

kills = 0
window = tk.Tk()
window.title("Fortnite points calculator")

def handle_button_press(event):
    window2 = tk.Tk()
    window2.title("FNCS points calculator")
    window2.mainloop()
   
button1 = tk.Button(text="FNCS")
button1.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button1.pack()

def handle_button_press(event):
    window3 = tk.Tk()
    window3.title("Ranked cup points calculator")
    window3.mainloop()

button2 = tk.Button(text="Ranked cup")
button2.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button2.pack()

def handle_button_press(event):
    window4 = tk.Tk()
    window4.title("OG Cup points calculator")
    window4.mainloop()

button3 = tk.Button(text="OG Cup")
button3.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button3.pack()

def handle_button_press(event):
    window5 = tk.Tk()
    window5.title("ZB OG Cup points calculator")
    window5.mainloop()

button4 = tk.Button(text="ZB OG Cup")
button4.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button4.pack()


def handle_button_press(event):
    window6 = tk.Tk()
    window6.title("Cash Cup points calculator")
    window6.mainloop()

button5 = tk.Button(text="Cash Cup")
button5.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button5.pack()

def handle_button_press(event):
    window7 = tk.Tk()
    window7.title("Playstation Cup points calculator")
    window7.mainloop()

button6 = tk.Button(text="Playstation Cup")
button6.bind("<Button-1>", handle_button_press)  # Bind left mouse button click event
button6.pack()















































def say_calculator(kills):
    if kills == '':
        print("You didn't enter your kills!")
    else:
        points = kills * 2
        print(kills)


lable1 = tk.Label(text="Enter your kills: ")
lable1.pack()
lable2 = tk.Label(textvariable=kills)
lable2.pack()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Start the event loop.
window.mainloop()


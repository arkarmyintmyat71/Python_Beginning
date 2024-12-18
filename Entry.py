import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Adding new data")

frame = tkinter.Frame(root)
frame.pack()

#Save New Things Info
things_frame = tkinter.LabelFrame(frame, text='New Thing info')  # Removed text, added corner radius for style
things_frame.grid(row=0, column=0, padx=20, pady=20)  # Added padding and sticky for alignment

name_lb = tkinter.Label(things_frame, text="Name", font=('Arial', 14, 'bold'))
name_lb.grid(row=1, column=0, pady=10, padx=10)
name_ent = tkinter.Entry(things_frame, font=('Arial', 14, 'bold'))
name_ent.grid(row=1, column=1, pady=10, padx=10)

type_lb = tkinter.Label(things_frame, text="Type", font=('Arial', 14, 'bold'))
type_lb.grid(row=2, column=0, pady=10, padx=10)
type_ent = tkinter.Entry(things_frame, font=('Arial', 14, 'bold'))
type_ent.grid(row=2, column=1, pady=10, padx=10)

color_lb = tkinter.Label(things_frame, text="Color", font=('Arial', 14, 'bold'))
color_lb.grid(row=3, column=0, pady=10, padx=10)
color_ent = tkinter.Entry(things_frame, font=('Arial', 14, 'bold'))
color_ent.grid(row=3, column=1, pady=10, padx=10)

weight_lb = tkinter.Label(things_frame, text="Weight", font=('Arial', 14, 'bold'))
weight_lb.grid(row=4, column=0, pady=10, padx=10)
weight_ent = tkinter.Entry(things_frame, font=('Arial', 14, 'bold'))
weight_ent.grid(row=4, column=1, pady=10, padx=10)

age_lb = tkinter.Label(things_frame, text="age", font=('Arial', 14, 'bold'))
age_lb.grid(row=5, column=0, pady=10, padx=10)
age_spinbox = ttk.Spinbox(things_frame, font=('Arial', 14, 'bold'), from_=1, to=100)
age_spinbox.grid(row=5, column=1, pady=10, padx=10)


root.mainloop()
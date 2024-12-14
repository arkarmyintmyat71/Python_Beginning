import customtkinter as ct
from test_final.services import Service

window = ct.CTk()
window.title('Login Form')
window.geometry('500x500')
ct.set_appearance_mode('dark')
ct.set_default_color_theme('green')

frame = ct.CTkFrame(master=window)
frame.pack(pady=50, padx=50, fill="both", expand=True)

#Creating Widgets
new_tg_lb = ct.CTkLabel(frame, text="Add New Thing", font=('corbel', 40, 'bold'))
name_lb = ct.CTkLabel(frame, text="Name", font=('corbel', 20, 'bold'))
name_ent = ct.CTkEntry(frame, font=('corbel', 20, 'bold'))

type_lb = ct.CTkLabel(frame, text="Type", font=('corbel', 20, 'bold'))
type_ent = ct.CTkEntry(frame, font=('corbel', 20, 'bold'))

color_lb = ct.CTkLabel(frame, text="Color", font=('corbel', 20, 'bold'))
color_ent = ct.CTkEntry(frame, font=('corbel', 20, 'bold'))

weight_lb = ct.CTkLabel(frame, text="Weight", font=('corbel', 20, 'bold'))
weight_ent = ct.CTkEntry(frame, font=('corbel', 20, 'bold'))

age_lb = ct.CTkLabel(frame, text="age", font=('corbel', 20, 'bold'))
age_ent = ct.CTkEntry(frame, font=('corbel', 20, 'bold'))

save_btn = ct.CTkButton(frame, text="✔ Save", height=5, width=20, font=('corbel', 20, 'bold'),
                        command=Service.add_thing())
cancel_btn = ct.CTkButton(frame, text="✘ Cancel", height=5, width=20, font=('corbel', 20, 'bold'), fg_color='red', hover_color='#900e35')

#Placing widgets in screen
new_tg_lb.grid(row=0, column=0, columnspan=2, pady=20, padx=50)
name_lb.grid(row=1, column=0, pady=10, padx=50)
name_ent.grid(row=1, column=1)

type_lb.grid(row=2, column=0, pady=10, padx=50)
type_ent.grid(row=2, column=1)

color_lb.grid(row=3, column=0, pady=10, padx=50)
color_ent.grid(row=3, column=1)

weight_lb.grid(row=4, column=0, pady=10, padx=50)
weight_ent.grid(row=4, column=1)

age_lb.grid(row=5, column=0, pady=10, padx=50)
age_ent.grid(row=5, column=1)

save_btn.grid(row=6, column=0, columnspan=2, pady=20, padx=20)
cancel_btn.grid(row=6, column=1, columnspan=2, pady=20, padx=20)
window.mainloop()
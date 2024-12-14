import customtkinter as ct
from test_final.services import Service

# Initialize the window
window = ct.CTk()
window.title('Login Form')
window.geometry('500x500')
ct.set_appearance_mode('dark')
ct.set_default_color_theme('green')

# Functionality for buttons
def add_new_action():
    # Show or reset the frame content when "Add New" is clicked
    for widget in frame.winfo_children():
        widget.destroy()  # Clear the frame
    create_add_new_form()

def edit_action():
    print("Edit clicked!")

def delete_action():
    print("Delete clicked!")

def save_action():
    # Example to gather data from the fields and save
    name = name_ent.get()
    type_ = type_ent.get()
    color = color_ent.get()
    weight = weight_ent.get()
    age = age_ent.get()
    print(f"Saving... Name: {name}, Type: {type_}, Color: {color}, Weight: {weight}, Age: {age}")
    # Call your service logic here
    Service.add_thing()

# Create Menu Navbar Buttons
add_btn = ct.CTkButton(window, text='Add New', font=('Corbel', 20, 'bold'), command=add_new_action)
add_btn.grid(row=0, column=0, pady=10, padx=20)

edit_btn = ct.CTkButton(window, text='Edit', font=('Corbel', 20, 'bold'), command=edit_action)
edit_btn.grid(row=0, column=1, pady=10, padx=20)

delete_btn = ct.CTkButton(window, text='Delete', font=('Corbel', 20, 'bold'), command=delete_action)
delete_btn.grid(row=0, column=2, pady=10, padx=20)

# Create a Frame for Dynamic Content
frame = ct.CTkFrame(master=window, corner_radius=10)
frame.grid(row=1, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")

# Function to Create Add New Form
def create_add_new_form():
    global name_ent, type_ent, color_ent, weight_ent, age_ent

    new_tg_lb = ct.CTkLabel(frame, text="Add New Thing", font=('Corbel', 40, 'bold'))
    new_tg_lb.grid(row=0, column=0, columnspan=2, pady=20, padx=50)

    name_lb = ct.CTkLabel(frame, text="Name", font=('Corbel', 20, 'bold'))
    name_ent = ct.CTkEntry(frame, font=('Corbel', 20, 'bold'))
    name_lb.grid(row=1, column=0, pady=10, padx=50)
    name_ent.grid(row=1, column=1)

    type_lb = ct.CTkLabel(frame, text="Type", font=('Corbel', 20, 'bold'))
    type_ent = ct.CTkEntry(frame, font=('Corbel', 20, 'bold'))
    type_lb.grid(row=2, column=0, pady=10, padx=50)
    type_ent.grid(row=2, column=1)

    color_lb = ct.CTkLabel(frame, text="Color", font=('Corbel', 20, 'bold'))
    color_ent = ct.CTkEntry(frame, font=('Corbel', 20, 'bold'))
    color_lb.grid(row=3, column=0, pady=10, padx=50)
    color_ent.grid(row=3, column=1)

    weight_lb = ct.CTkLabel(frame, text="Weight", font=('Corbel', 20, 'bold'))
    weight_ent = ct.CTkEntry(frame, font=('Corbel', 20, 'bold'))
    weight_lb.grid(row=4, column=0, pady=10, padx=50)
    weight_ent.grid(row=4, column=1)

    age_lb = ct.CTkLabel(frame, text="Age", font=('Corbel', 20, 'bold'))
    age_ent = ct.CTkEntry(frame, font=('Corbel', 20, 'bold'))
    age_lb.grid(row=5, column=0, pady=10, padx=50)
    age_ent.grid(row=5, column=1)

    save_btn = ct.CTkButton(
        frame, text="✔ Save", height=5, width=20, font=('Corbel', 20, 'bold'), command=save_action
    )
    cancel_btn = ct.CTkButton(
        frame, text="✘ Cancel", height=5, width=20, font=('Corbel', 20, 'bold'),
        fg_color='red', hover_color='#900e35', command=lambda: frame.grid_forget()
    )

    save_btn.grid(row=6, column=0, pady=20, padx=20)
    cancel_btn.grid(row=6, column=1, pady=20, padx=20)

# Run the application
window.mainloop()

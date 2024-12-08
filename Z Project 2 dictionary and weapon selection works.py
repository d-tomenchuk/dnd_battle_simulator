# Leroy
# Project Two
# 12/4/2024

import tkinter as tk
from tkinter import Button
from zDiceRollWindow2 import DiceRollWindow

#Add go on adventure button to connect dice roll portion of code

def show_selection():
    # Get the selected weapon and its description
    weapon = selected_value.get()
    description = weapons.get(weapon, "No description available.")
    
    # Display the selected weapon and its description
    result_label.config(text=f"You selected: {weapon}\nDescription: {description}")

def open_dice_roll():
    DiceRollWindow(main_menu)
    #dice_roll = tk.Toplevel(main_menu)
    #dice_roll.title("DnD Battle Simulator part two")
    #dice_roll.geometry("600x450")
    #tk.Label(dice_roll, text="This is a new window!").pack(pady=10)

# Initialize the main window
main_menu = tk.Tk()
main_menu.title("DnD Battle Simulator part one")  # Title for the window

# Set window size
main_menu.geometry("600x450")

# Add label for choosing a weapon
label = tk.Label(main_menu, text="The road is dangerous, select a weapon.", font=("Courier", 12))
label.pack(pady=10)

# List and dictionary for weapons and descriptions
weapons = {
    "Greatsword": "A massive sword used for powerful strikes.",
    "Spear": "A mighty spear for precise thrusts.",
    "Axe": "A hunter's axe perfect for chopping.",
    "Magic Beans": "Small glowing beans with mysterious powers."
}

# Create a frame for radio buttons
frame = tk.Frame(main_menu)
frame.pack(pady=20)

# Variable to track the selected weapon
selected_value = tk.StringVar(value="None")  # Default value

# Create radio buttons for weapon selection
radio1 = tk.Radiobutton(frame, text="Greatsword", variable=selected_value, value="Greatsword")
radio1.pack(anchor="w")
radio2 = tk.Radiobutton(frame, text="Spear", variable=selected_value, value="Spear")
radio2.pack(anchor="w")
radio3 = tk.Radiobutton(frame, text="Axe", variable=selected_value, value="Axe")
radio3.pack(anchor="w")
radio4 = tk.Radiobutton(frame, text="Magic Beans", variable=selected_value, value="Magic Beans")
radio4.pack(anchor="w")

# Function to handle button click

# Button to display the selected value
button = Button(main_menu, text="Show Selection", command=show_selection)
button.pack(pady=10)

# Label to display the result of the selection
result_label = tk.Label(main_menu, text="", font=("Courier", 12), fg="black")
result_label.pack(pady=10)


    
#root = tk.Tk()
#root.title("Main Window.")
adventure_button = Button(main_menu, text="Go on an Adventure", command=open_dice_roll)
adventure_button.pack(pady=10)



# Start the main program loop
main_menu.mainloop()

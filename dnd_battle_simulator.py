import tkinter as tk
import random

class DnDBattleSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("DnD Battle Simulator")
        self.root.geometry("600x450")
        
        # Frame for weapon selection
        self.weapon_frame = tk.Frame(self.root)
        self.weapon_frame.pack(fill="both", expand=True)
        
        # Weapons and their descriptions
        self.weapons = {
            "Greatsword": "A massive sword used for powerful strikes.",
            "Spear": "A mighty spear for precise thrusts.",
            "Axe": "A hunter's axe perfect for chopping.",
            "Magic Beans": "Small glowing beans with mysterious powers."
        }

        # Title for weapon selection
        tk.Label(
            self.weapon_frame, 
            text="The road is dangerous, select a weapon.", 
            font=("Courier", 12)
        ).pack(pady=10)

        # Radio buttons for selecting a weapon
        self.selected_weapon = tk.StringVar(value="None")
        for weapon in self.weapons:
            tk.Radiobutton(
                self.weapon_frame, 
                text=weapon, 
                variable=self.selected_weapon, 
                value=weapon
            ).pack(anchor="w")

        # Button to confirm weapon selection
        tk.Button(
            self.weapon_frame, 
            text="Go on an Adventure", 
            command=self.start_battle
        ).pack(pady=20)

        # Label to display selected weapon
        self.weapon_label = tk.Label(self.weapon_frame, text="", font=("Courier", 12), wraplength=500, justify="center")
        self.weapon_label.pack(pady=10)

        # Frame for the battle simulation
        self.battle_frame = tk.Frame(self.root)

        # Elements for the battle
        self.battle_label = tk.Label(self.battle_frame, text="", font=("Courier", 12), wraplength=500, justify="center")
        self.battle_label.pack(pady=10)

        tk.Button(
            self.battle_frame, 
            text="Attack", 
            command=self.attack
        ).pack(pady=5)

        tk.Button(
            self.battle_frame, 
            text="Flee", 
            command=self.flee
        ).pack(pady=5)

        self.result_label = tk.Label(self.battle_frame, text="", font=("Courier", 12), wraplength=500, justify="center", fg="blue")
        self.result_label.pack(pady=20)

        # Variables to store the selected weapon and its description
        self.current_weapon = None
        self.current_description = None

    def start_battle(self):
        # Show the selected weapon
        weapon = self.selected_weapon.get()
        if weapon == "None":
            self.weapon_label.config(text="Please select a weapon!")
            return

        self.current_weapon = weapon
        self.current_description = self.weapons[weapon]
        self.weapon_label.config(text=f"You selected: {weapon}\n{self.current_description}")

        # Hide weapon selection and show the battle screen
        self.weapon_frame.pack_forget()
        self.battle_frame.pack(fill="both", expand=True)

        # Clear previous battle result
        self.result_label.config(text="")

        # Start battle description
        self.battle_label.config(
            text=f"You are walking down a path with your {self.current_weapon} "
                 f"({self.current_description}) when suddenly,\na Demigorgan ambushes you!\nWill you attack or flee?"
        )

    def attack(self):
        # Simulate a dice roll
        D20 = random.randint(1, 20)
        if D20 >= 14:
            self.result_label.config(
                text=f"You wield your {self.current_weapon} and strike with a {self.current_description}\n"
                     f"You rolled a {D20} and slayed the Demigorgan! You are a hero!"
            )
        else:
            self.result_label.config(
                text=f"You attack with your {self.current_weapon} but miss!\n"
                     f"You rolled a {D20}. The Demigorgan blocks your attack and bites off your head!"
            )

    def flee(self):
        # Display flee message
        self.result_label.config(text="You chose to flee! You live to fight another day!")
        
        # Return to the menu after 1 second
        self.root.after(1000, self.go_back_to_menu)

    def go_back_to_menu(self):
        # Return to weapon selection screen
        self.battle_frame.pack_forget()
        self.weapon_frame.pack(fill="both", expand=True)
        self.weapon_label.config(text="")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DnDBattleSimulator(root)
    root.mainloop()

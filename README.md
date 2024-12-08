
# DnD Battle Simulator

This project is a simple "DnD Battle Simulator" built with Python and Tkinter. It allows users to choose a weapon and engage in a battle with a Demigorgon. The game simulates a dice roll, and the player must choose whether to attack or flee. The player's actions and dice rolls affect the outcome of the battle, with a victory if the player rolls high enough, or defeat if they fail. The game also features weapon descriptions to enhance the player's experience.

## Features

- Select from multiple weapons, each with a unique description.
- Simulate a battle with a random dice roll (D20) to determine the outcome.
- Option to flee the battle with a short result and return to the menu.
- Clean and intuitive GUI created with Tkinter.
- Battle result is displayed dynamically based on the player's choice.

## Project Files

- **Works Project 1-2 dice roll.py**: Contains the initial dice roll logic.
- **Z Project 2 dictionary and weapon selection works.py**: Handles weapon selection and dictionary for weapons.
- **zDiceRollWindow2.py**: Additional logic related to the dice roll window.
- **task_instructions.txt**: Technical assignment for the project.
- **dnd_battle_simulator.py**: Final solution for the DnD Battle Simulator, incorporating all features and functionality.

## Installation

To run the DnD Battle Simulator, ensure you have Python installed on your system. You will also need the `tkinter` module for the graphical user interface (GUI), which is included by default with Python installations.

1. Clone this repository or download the project files.
   
2. Ensure you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).

3. Run the following command to check if `tkinter` is available:
   ```bash
   python -m tkinter
   ```

4. To start the battle simulator, run the following command:
   ```bash
   python dnd_battle_simulator.py
   ```

5. The application will launch, allowing you to select a weapon and begin the battle.

## Usage

1. Select a weapon from the list.
2. Choose whether to attack or flee.
3. The game will simulate a dice roll to determine the outcome of your attack.
4. If you win, you will be notified; if you lose, you will be defeated and can choose to try again.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

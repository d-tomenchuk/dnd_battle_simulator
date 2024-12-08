import tkinter as tk
from tkinter import Button
import random

#Dice Roll window
class DiceRollWindow:
    def __init__(self, parent):
        self.gameplay=tk.Toplevel(parent)
        self.gameplay.title("DnD Battle Simulator Part 2")
        self.gameplay.geometry("600x450")
        self.lbl1=tk.Label(self.gameplay, text="You are walking down a path when suddenly,\na Demigorgan ambushes you!", font=("Courier", 12))
        self.lbl1.pack(pady=10)
        self.lbl2=tk.Label(self.gameplay, text="You must attack or flee")
        #Entry Widget for attack
        #self.t1=tk.Entry(self.gameplay)
        
        
        
        
        
        
        

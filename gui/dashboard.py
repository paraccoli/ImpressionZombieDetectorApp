import tkinter as tk
from tkinter import ttk
from utils.localization import _

class DashboardFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = ttk.Label(self, text=_("Welcome to the Twitter Impression Zombie Detector"))
        self.welcome_label.pack(pady=20)

        self.info_label = ttk.Label(self, text=_("This tool helps you identify potential 'zombie' followers."))
        self.info_label.pack(pady=10)

        self.instruction_label = ttk.Label(self, text=_("Go to the 'Zombie Detector' tab to start analyzing."))
        self.instruction_label.pack(pady=10)

    def refresh_gui(self):
        self.welcome_label.config(text=_("Welcome to the Twitter Impression Zombie Detector"))
        self.info_label.config(text=_("This tool helps you identify potential 'zombie' followers."))
        self.instruction_label.config(text=_("Go to the 'Zombie Detector' tab to start analyzing."))
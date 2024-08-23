import tkinter as tk
from tkinter import ttk
from utils.localization import _
import config

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title(_("Settings"))
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text=_("Settings"))
        self.label.pack(pady=20)

        self.api_key_label = ttk.Label(self, text=_("Twitter API Key:"))
        self.api_key_label.pack(anchor="w", padx=10, pady=5)
        self.api_key_entry = ttk.Entry(self)
        self.api_key_entry.insert(0, config.CONSUMER_KEY)
        self.api_key_entry.pack(fill="x", padx=10, pady=5)

        self.api_secret_label = ttk.Label(self, text=_("Twitter API Secret:"))
        self.api_secret_label.pack(anchor="w", padx=10, pady=5)
        self.api_secret_entry = ttk.Entry(self, show="*")
        self.api_secret_entry.insert(0, config.CONSUMER_SECRET)
        self.api_secret_entry.pack(fill="x", padx=10, pady=5)

        self.save_button = ttk.Button(self, text=_("Save"), command=self.save_settings)
        self.save_button.pack(pady=20)

    def save_settings(self):
        config.CONSUMER_KEY = self.api_key_entry.get()
        config.CONSUMER_SECRET = self.api_secret_entry.get()
        # ここで設定をファイルに保存するロジックを実装する
        self.destroy()
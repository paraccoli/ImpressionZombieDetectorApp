import tkinter as tk
from tkinter import ttk, messagebox
import threading
from utils.twitter_api import get_twitter_api, detect_imprezombies
from utils.localization import _

class ZombieDetectorFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.username_label = ttk.Label(self, text=_("Twitter Username:"))
        self.username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.username_entry = ttk.Entry(self, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.threshold_label = ttk.Label(self, text=_("Threshold (0-1):"))
        self.threshold_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.threshold_entry = ttk.Entry(self, width=10)
        self.threshold_entry.insert(0, "0.8")
        self.threshold_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.detect_button = ttk.Button(self, text=_("Detect Zombies"), command=self.start_detection)
        self.detect_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.result_text = tk.Text(self, height=15, width=70)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.result_text.yview)
        scrollbar.grid(row=3, column=2, sticky="ns")
        self.result_text.configure(yscrollcommand=scrollbar.set)

    def start_detection(self):
        username = self.username_entry.get()
        threshold = float(self.threshold_entry.get())

        if not username:
            messagebox.showerror(_("Error"), _("Please enter a Twitter username."))
            return

        self.detect_button.config(state="disabled")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, _("Detecting zombies... Please wait.\n"))

        thread = threading.Thread(target=self.detect_zombies, args=(username, threshold))
        thread.start()

    def detect_zombies(self, username, threshold):
        try:
            api = get_twitter_api()
            zombies = detect_imprezombies(api, username, threshold)
            self.master.after(0, self.update_results, zombies)
        except Exception as e:
            self.master.after(0, self.show_error, str(e))

    def update_results(self, zombies):
        self.result_text.delete(1.0, tk.END)
        if zombies:
            self.result_text.insert(tk.END, _("Detected Impression Zombies:\n"))
            for zombie in zombies:
                self.result_text.insert(tk.END, f"- @{zombie}\n")
        else:
            self.result_text.insert(tk.END, _("No impression zombies detected."))

        self.detect_button.config(state="normal")

    def show_error(self, error_message):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, _("An error occurred: {error}").format(error=error_message))
        self.detect_button.config(state="normal")

    def refresh_gui(self):
        self.username_label.config(text=_("Twitter Username:"))
        self.threshold_label.config(text=_("Threshold (0-1):"))
        self.detect_button.config(text=_("Detect Zombies"))
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .dashboard import DashboardFrame
from .zombie_detector import ZombieDetectorFrame
from .settings import SettingsWindow
from utils.localization import _, change_language

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title(_("Twitter Impression Zombie Detector"))
        self.master.geometry("800x600")
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')

        self.dashboard = DashboardFrame(self.notebook)
        self.zombie_detector = ZombieDetectorFrame(self.notebook)

        self.notebook.add(self.dashboard, text=_("Dashboard"))
        self.notebook.add(self.zombie_detector, text=_("Zombie Detector"))

        self.setup_menu()

    def setup_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=_("File"), menu=file_menu)
        file_menu.add_command(label=_("Settings"), command=self.open_settings)
        file_menu.add_command(label=_("Exit"), command=self.master.quit)

        language_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=_("Language"), menu=language_menu)
        language_menu.add_command(label="English", command=lambda: self.change_language('en'))
        language_menu.add_command(label="日本語", command=lambda: self.change_language('ja'))

    def open_settings(self):
        SettingsWindow(self.master)

    def change_language(self, lang):
        try:
            change_language(lang)
            self.refresh_gui()
        except Exception as e:
            print(f"Error changing language: {e}")
            import traceback
            traceback.print_exc()  # より詳細なエラー情報を表示
            # エラーメッセージをユーザーに表示
            messagebox.showerror("Error", f"Failed to change language: {e}")

    def refresh_gui(self):
        # GUIのテキストを更新
        self.master.title(_("Twitter Impression Zombie Detector"))
        self.notebook.tab(0, text=_("Dashboard"))
        self.notebook.tab(1, text=_("Zombie Detector"))
        self.dashboard.refresh_gui()
        self.zombie_detector.refresh_gui()
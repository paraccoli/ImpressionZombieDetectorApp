import tkinter as tk
from gui.main_window import MainWindow
from utils.localization import setup_localization
import locale
import sys

def main():
    # エンコーディングを明示的に設定
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
    if sys.stderr.encoding != 'utf-8':
        sys.stderr = open(sys.stderr.fileno(), mode='w', encoding='utf-8', buffering=1)

    # ロケールを明示的に設定
    locale.setlocale(locale.LC_ALL, '')
    setup_localization()
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
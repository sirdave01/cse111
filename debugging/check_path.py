import sys
import tkinter as tk
print(sys.executable)
print(tk.TclVersion, tk.TkVersion)
root = tk.Tk()  # This is the critical step
root.destroy()  # Clean up immediately
print("Tkinter root created successfully!")  # If you see this, it's fixed
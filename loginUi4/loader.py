import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

def browse():
    file_path = filedialog.askopenfilename(title="Select .exe file", filetypes=[("Executable files", "*.exe")])
    launcher_entry.delete(0, tk.END)
    launcher_entry.insert(0, file_path)

def launch():
    exe_path = launcher_entry.get()
    if not exe_path:
        messagebox.showerror("Error", "Please select a .exe file")
        return

    os.system(exe_path)

root = tk.Tk()
root.title("z-launcher")
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Load background image
bg_image = tk.PhotoImage(file="background_image.png")  # Replace "background_image.png" with your image file
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

launcher_frame = tk.Frame(root, bg="#121212", bd=5)
launcher_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

launcher_label = tk.Label(launcher_frame, text="Launcher", font=("Helvetica", 24), fg="white", bg="#121212")
launcher_label.grid(row=0, column=0, columnspan=2, pady=10)

browse_button = tk.Button(launcher_frame, text="Browse", bg="#FF4500", fg="white", command=browse, relief=tk.RAISED, borderwidth=0, padx=30, pady=15, font=("Arial", 14), bd=0, highlightthickness=0)
browse_button.grid(row=1, column=0, pady=10, padx=(40, 10), sticky="ew")

launcher_entry = tk.Entry(launcher_frame, width=50, bg="#d9d9d9", font=("Arial", 14))
launcher_entry.grid(row=1, column=1, pady=10, padx=(0, 40), sticky="ew")

launch_button = tk.Button(launcher_frame, text="Launch", bg="#FF4500", fg="white", command=launch, relief=tk.RAISED, borderwidth=0, padx=30, pady=15, font=("Arial", 14), bd=0, highlightthickness=0)
launch_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#FF4500", fg="white", relief=tk.RAISED, borderwidth=0, padx=30, pady=15, font=("Arial", 14), bd=0, highlightthickness=0)
exit_button.place(relx=1.0, rely=0, anchor=tk.NE, x=-20, y=20)

root.mainloop()

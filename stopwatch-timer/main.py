import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⏱️ Stopwatch & Countdown Timer")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")

        self.is_running = False
        self.is_countdown = False
        self.counter = 0
        self.timer_id = None

        # Title
        self.title_label = tk.Label(root, text="Timer Mode: Stopwatch", font=("Arial", 14, "bold"), bg="#1e1e1e", fg="#FFD700")
        self.title_label.pack(pady=10)

        # Time Display
        self.time_label = tk.Label(root, text="00:00:00", font=("Courier", 40), bg="#1e1e1e", fg="#00FF99")
        self.time_label.pack(pady=10)

        # Countdown Input
        self.entry = tk.Entry(root, font=("Arial", 12), justify='center')
        self.entry.pack(pady=5)
        self.entry.insert(0, "Enter seconds for countdown")

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(btn_frame, text="▶ Start", width=8, command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = tk.Button(btn_frame, text="⏸ Pause", width=8, command=self.pause)
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="🔁 Reset", width=8, command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=5)

        self.mode_btn = tk.Button(root, text="Switch to Countdown", command=self.toggle_mode)
        self.mode_btn.pack(pady=10)

        self.update_display()

    def toggle_mode(self):
        self.reset()
        self.is_countdown = not self.is_countdown
        if self.is_countdown:
            self.title_label.config(text="Timer Mode: Countdown")
            self.mode_btn.config(text="Switch to Stopwatch")
            self.entry.config(state=tk.NORMAL)
        else:
            self.title_label.config(text="Timer Mode: Stopwatch")
            self.mode_btn.config(text="Switch to Countdown")
            self.entry.config(state=tk.DISABLED)

    def start(self):
        if not self.is_running:
            if self.is_countdown:
                try:
                    if self.counter == 0:
                        self.counter = int(self.entry.get())
                except ValueError:
                    messagebox.showerror("Error", "Enter valid number of seconds")
                    return
            self.is_running = True
            self.run_timer()

    def pause(self):
        if self.is_running:
            self.root.after_cancel(self.timer_id)
            self.is_running = False

    def reset(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.counter = 0
        self.is_running = False
        self.update_display()

    def run_timer(self):
        if self.is_running:
            if self.is_countdown:
                if self.counter <= 0:
                    self.is_running = False
                    self.update_display()
                    messagebox.showinfo("⏰ Time's up!", "Countdown completed!")
                    return
                self.counter -= 1
            else:
                self.counter += 1

            self.update_display()
            self.timer_id = self.root.after(1000, self.run_timer)

    def update_display(self):
        hrs = self.counter // 3600
        mins = (self.counter % 3600) // 60
        secs = self.counter % 60
        time_str = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        self.time_label.config(text=time_str)

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

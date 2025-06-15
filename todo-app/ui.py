import tkinter as tk
from tkinter import messagebox
from tasks import load_tasks, save_tasks

tasks = []

def add_task(entry, listbox):
    task = entry.get().strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty", "Task cannot be empty.")

def delete_task(listbox):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Select", "Please select a task to delete.")

def clear_all(listbox):
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()
        save_tasks(tasks)

def create_app():
    global tasks
    tasks = load_tasks()

    root = tk.Tk()
    root.title("📝 To-Do List App")
    root.geometry("400x400")
    root.resizable(False, False)

    entry = tk.Entry(root, width=30, font=("Arial", 12))
    entry.pack(pady=10)

    add_btn = tk.Button(root, text="Add Task", command=lambda: add_task(entry, listbox))
    add_btn.pack()

    listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
    listbox.pack(pady=10)

    for task in tasks:
        listbox.insert(tk.END, task)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=5)

    del_btn = tk.Button(btn_frame, text="Delete Selected", command=lambda: delete_task(listbox))
    del_btn.grid(row=0, column=0, padx=5)

    clr_btn = tk.Button(btn_frame, text="Clear All", command=lambda: clear_all(listbox))
    clr_btn.grid(row=0, column=1, padx=5)

    root.mainloop()

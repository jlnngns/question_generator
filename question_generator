import tkinter as tk
from tkinter import messagebox 

def clear_entries():
    entry_question.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_d.delete(0, tk.END)
    entry_correct.delete(0, tk.END)

def exit_program():
    root.destroy()

def save_question():
    question = entry_question.get()
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    d = entry_d.get()
    correct = entry_correct.get().lower()

    if not (question and a and b and c and c and d and correct in ['a', 'b', 'c', 'd']):
        messagebox.showwarning("Input Error", "Please fill in all fields and ensure correct answer is a, b, c, or d.")
        return
    
    with open("questions.txt", "a", encoding="utf-8") as f:
        f.write(f"a. {a}\n")
        f.write(f"b. {b}\n")
        f.write(f"c. {c}\n")
        f.write(f"d. {d}\n")
        f.write(f"Correct answer: {correct}\n\n")

    clear_entries()
    messagebox.showinfo("Saved", "Question saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Quiz Creator")

tk.Label(root, text="Enter Question:").pack()
entry_question = tk.Entry(root, width=60)
entry_question.pack()

tk.Label(root, text="Answer a:").pack()
entry_a = tk.Entry(root, width=60)
entry_a.pack()

tk.Label(root, text="Answer b:").pack()
entry_b = tk.Entry(root, width=60)
entry_b.pack()

tk.Label(root, text="Answer c:").pack()
entry_c = tk.Entry(root, width=60)
entry_c.pack()

tk.Label(root, text="Answer d:").pack()
entry_d = tk.Entry(root, width=60)
entry_d.pack()

tk.Label(root, text="Correct answer (a/b/c/d):").pack()
entry_correct = tk.Entry(root, width=5)
entry_correct.pack()

tk.Button(root, text="Save Question", command=save_question).pack(pady=5)
tk.Button(root, text="Exit",command=exit_program).pack()

root.mainloop()

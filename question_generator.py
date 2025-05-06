import tkinter as tk
from tkinter import messagebox 

def clear_entries():
    entry_question.delete(0, tk.END)
    entry_option_a.delete(0, tk.END)
    entry_option_b.delete(0, tk.END)
    entry_option_c.delete(0, tk.END)
    entry_option_d.delete(0, tk.END)
    entry_correct_answer.delete(0, tk.END)

def exit_program():
    root.destroy()

def save_question():
    question_text = entry_question.get()
    option_a = entry_option_a.get()
    option_b = entry_option_b.get()
    option_c = entry_option_c.get()
    option_d = entry_option_d.get()
    correct_answer = entry_correct_answer.get().lower()

    if not (question_text and option_a and option_b and option_c and option_d and correct_answer in ['a', 'b', 'c', 'd']):
        messagebox.showwarning("Input Error", "Please fill in all fields and ensure correct answer is a, b, c, or d.")
        return
    
    with open("questions.txt", "a", encoding="utf-8") as file:
        file.write(f"Question: {question_text}\n")
        file.write(f"a. {option_a}\n")
        file.write(f"b. {option_b}\n")
        file.write(f"c. {option_c}\n")
        file.write(f"d. {option_d}\n")
        file.write(f"Correct answer: {correct_answer}\n\n")

    clear_entries()
    messagebox.showinfo("Saved", "Question saved successfully!")

# GUI Setup
root = tk.Tk()
root.title("Quiz Creator")

tk.Label(root, text="Enter Question:").pack()
entry_question = tk.Entry(root, width=60)
entry_question.pack()

tk.Label(root, text="Answer a:").pack()
entry_option_a = tk.Entry(root, width=60)
entry_option_a.pack()

tk.Label(root, text="Answer b:").pack()
entry_option_b = tk.Entry(root, width=60)
entry_option_b.pack()

tk.Label(root, text="Answer c:").pack()
entry_option_c = tk.Entry(root, width=60)
entry_option_c.pack()

tk.Label(root, text="Answer d:").pack()
entry_option_d = tk.Entry(root, width=60)
entry_option_d.pack()

tk.Label(root, text="Correct answer (a/b/c/d):").pack()
entry_correct_answer = tk.Entry(root, width=5)
entry_correct_answer.pack()

tk.Button(root, text="Save Question", command=save_question).pack(pady=5)
tk.Button(root, text="Exit", command=exit_program).pack()

root.mainloop()

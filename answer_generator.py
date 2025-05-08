import tkinter as tk
from tkinter import messagebox
import random

# Function to load questions from the file
def load_questions_from_file(filename="questions.txt"):
    questions_list = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read().strip().split("\n\n")
            for question_block in content:
                lines = question_block.strip().split("\n")
                if len(lines) == 6:
                    question_text = lines[0].replace("Question: ", "").strip()
                    option_a = lines[1].replace("a. ", "").strip()
                    option_b = lines[2].replace("b. ", "").strip()
                    option_c = lines[3].replace("c. ", "").strip()
                    option_d = lines[4].replace("d. ", "").strip()
                    correct_choice = lines[5].replace("Correct answer: ", "").strip().lower()
                    questions_list.append({"question": question_text, "options": {"a": option_a, "b": option_b, "c": option_c, "d": option_d}, "answer": correct_choice})
    except FileNotFoundError:
        messagebox.showerror("Error", "The questions file was not found.")
    return questions_list

# Function to show a random question
def show_next_question():
    global remaining_questions, total_questions, correct_answers_count
    if not remaining_questions:
        messagebox.showinfo("Quiz Complete", f"You answered {correct_answers_count} out of {total_questions} questions correctly.")
        root.quit()
        return
    
    current_question_data = random.choice(remaining_questions); remaining_questions.remove(current_question_data)

    question_label.config(text=current_question_data["question"]); radio_button_a.config(text=f"a.{current_question_data['options']['a']}"); radio_button_b.config(text=f"b.{current_question_data['options']['b']}"); radio_button_c.config(text=f"c.{current_question_data['options']['c']}"); radio_button_d.config(text=f"d.{current_question_data['options']['d']}")

    answer_variable.set(None); next_button.config(command=lambda:check_user_answer(current_question_data))

# Function to check user's answer
def check_user_answer(question_data):
    global correct_answers_count
    selected_answer = answer_variable.get()
    if not selected_answer:
        messagebox.showewarning("Warning", "Please select an answer.")
        return
    
    if selected_answer == question_data["answer"]:
        correct_answers_count += 1
        messagebox.showinfo("Correct", "That's the correct answer!")
    else:
        correct_option_text = question_data["options"][question_data["answer"]]
        messagebox.showinfo("Incorrect", f"Wrong! The correct answer is {question_data['answer']}.{correct_option_text}")

    show_next_question()

# GUI Setup
root = tk.Tk()
root.title("Quiz Creator")

question_label = tk.Label(root, text="Question will appear here", wraplength=500, justify="left", font=("Arial", 12))
question_label.pack(pady=10)

answer_variable = tk.StringVar()

radio_button_a = tk.Radiobutton(root, text="a", variable=answer_variable, value="a", wraplength=500, justify="left")
radio_button_a.pack(anchor="w")
radio_button_b = tk.Radiobutton(root, text="b", variable=answer_variable, value="b", wraplength=500, justify="left")
radio_button_b.pack(anchor="w")
radio_button_c = tk.Radiobutton(root, text="c", variable=answer_variable, value="c", wraplength=500, justify="left")
radio_button_c.pack(anchor="w")
radio_button_d = tk.Radiobutton(root, text="d", variable=answer_variable, value="d", wraplength=500, justify="left")
radio_button_d.pack(anchor="w")

next_button = tk.Button(root, text="Submit Answer")
next_button.pack(pady=10)

# Load questions and begin quiz
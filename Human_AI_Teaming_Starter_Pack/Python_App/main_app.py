import tkinter as tk
from tkinter import messagebox


def get_ai_suggestion(situation):
    # Hardcoded AI logic for now
    return "Send helicopter to Sector A and B first."


def on_decide():
    messagebox.showinfo(
        "Decision", "Your decision has been recorded.\nPlease fill the feedback form."
    )


# GUI setup
root = tk.Tk()
root.title("Human-AI Teaming - Emergency Decision System")

situation_text = "FLOOD ALERT: 5 sectors are in danger.\nYou have 2 helicopters.\nWhere will you send them first?"
tk.Label(root, text=situation_text, padx=20, pady=10).pack()

ai_suggestion = get_ai_suggestion(situation_text)
tk.Label(root, text=f"AI Suggestion: {ai_suggestion}", fg="blue", pady=10).pack()

tk.Button(
    root, text="Make My Decision", command=on_decide, bg="green", fg="white"
).pack(pady=20)

root.mainloop()

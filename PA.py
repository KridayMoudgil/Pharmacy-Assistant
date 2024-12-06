import customtkinter as Ctk
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def show_instruction(problem):
    if problem == "headache":
        instruction = "Press button 1"
        messagebox.showinfo("Instruction", instruction)
        speak(instruction)
    elif problem == "fever":
        instruction = "Press button 2"
        messagebox.showinfo("Instruction", instruction)
        speak(instruction)
    elif problem == "flu":
        instruction = "Press button 3"
        messagebox.showinfo("Instruction", instruction)
        speak(instruction)
    elif problem == "stomach ache":
        instruction = "Press button 4"
        messagebox.showinfo("Instruction", instruction)
        speak(instruction)
    else:
        warning = "We dont have solution for this"
        messagebox.showwarning("Unknown Problem", warning)
        speak(warning)

def button_action(problem, button_text):
    speak(button_text)
    show_instruction(problem)

root = Ctk.CTk()
root.title("Pharmacy Helper")
root.geometry("450x250")

label = Ctk.CTkLabel(root, text="Please choose a problem:", font=("Arial", 14))
label.pack(pady=20)

# Buttons for each health problem
Ctk.CTkButton(root, text="headache", command=lambda: button_action("headache", "headache"), width=100).pack(pady=5)
Ctk.CTkButton(root, text="fever", command=lambda: button_action("fever", "fever"), width=100).pack(pady=5)
Ctk.CTkButton(root, text="common cold", command=lambda: button_action("flu", "common cold"), width=100).pack(pady=5)
Ctk.CTkButton(root, text="stomach ache", command=lambda: button_action("stomach ache", "stomach ache"), width=100).pack(pady=5)


root.mainloop()

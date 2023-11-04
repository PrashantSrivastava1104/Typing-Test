import time
import tkinter as tk
from tkinter import ttk
import random

# List of random sentences for typing challenge
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "To be or not to be, that is the question",
    "In three words I can sum up everything I've learned about life: it goes on",
    "All you need is love",
]

# Function to get a random sentence
def get_random_sentence():
    return random.choice(sentences)

# Function to start a new typing challenge
def start_typing_challenge():
    global string_to_type
    string_to_type = get_random_sentence()
    string_label.config(text=string_to_type)
    entry.delete(0, tk.END)
    entry.focus()
    result_label.config(text="")
    time_label.config(text="")

# Function to check if the typed string matches the original string
def check_string():
    global start_time
    global typed_string

    typed_string = entry.get()
    end_time = time.time()
    typing_time = end_time - start_time

    if typed_string == string_to_type:
        result_label.config(text="Congratulations, the strings match!", foreground="green")
    else:
        result_label.config(text="Sorry, the strings do not match", foreground="red")

    time_label.config(text=f"It took you {typing_time:.2f} seconds to type the string")

# Create a GUI window
root = tk.Tk()
root.title("Typing Challenge Game")

# Set the window size
root.geometry("500x250")

# Define the initial string to type
string_to_type = ""

# Create and display the string label with a colored background
string_label = ttk.Label(root, text=string_to_type, font=("Arial", 14), background="#FFE4E1")
string_label.pack(pady=10)

# Create an entry widget for typing
entry = ttk.Entry(root, font=("Arial", 12))
entry.pack(pady=10, padx=30, fill="x")

# Create a button to start a new challenge
start_button = ttk.Button(root, text="Start Challenge", command=start_typing_challenge, style="TButton")
start_button.pack(pady=10)

# Create a button to check the typed string with a custom style
check_button = ttk.Button(root, text="Check", command=check_string, style="TButton")
check_button.pack(pady=10)

# Create labels for the result and time with colored backgrounds
result_label = ttk.Label(root, text="", font=("Arial", 12), foreground="green", background="#FFE4E1")
result_label.pack()
time_label = ttk.Label(root, text="", font=("Arial", 12), background="#FFE4E1")
time_label.pack(pady=10)

# Create a custom style for the buttons with different colors
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="#FFA07A")

# Start a timer
start_time = time.time()
typed_string = ""

# Start the GUI main loop
root.mainloop()
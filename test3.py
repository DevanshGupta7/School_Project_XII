#Working Snellen Eye Service



import tkinter as tk
import random
import string
import time
import datetime

def next_level():
    global current_size, level, text1, failed_attempts
    if level < len(letter_sizes):
        failed_attempts = 3
        current_size = letter_sizes[level]
        level += 1
        text1 = random_letter()
        canvas.itemconfig(letter, font=("Arial", current_size), text=text1)
    else:
        status_label.config(text="Test Completed!")
        display_report()
        
def random_letter():
    random_letter = random.choice(string.ascii_uppercase)
    return random_letter

def display_report():
    report_window = tk.Toplevel(root)
    report_window.title("Eye Test Report")
    
    if level > 0:
        report_content = f"""
        Eye Test Report:
        ---------------------
        Best Level Achieved: Level {level}
        Smallest Letter Size: {letter_sizes[level-1]} pixels
        Estimated Visual Acuity: {vision_acuity[level-1]}
        ---------------------
        Recommendations:
        {"Your vision seems normal." if level >= len(letter_sizes) - 1 else "Consider consulting an optometrist."}
        """
    else:
        report_content = f"""
        Eye Test Report:
        ---------------------
        Best Level Achieved: Level {level}
        Smallest Letter Size: --
        Estimated Visual Acuity: --
        ---------------------
        Recommendations:
        {"Highly Consider consulting an optometrist."}
        """
        
    print(level)
    report_label = tk.Label(report_window, text=report_content, justify="left", font=("Arial", 12))
    report_label.pack(padx=20, pady=20)

    # Close Button
    close_button = tk.Button(report_window, text="Close", command=report_window.destroy)
    close_button.pack(pady=10)

# Distance setup
distance_from_screen = 3  # meters

# Letter heights in pixels for a 96 PPI screen
letter_sizes = [150, 120, 100, 75, 50, 30, 20, 10, 8, 7]  # Example pixel sizes for each level
vision_acuity = ["20/200", "20/100", "20/80", "20/60", "20/40", "20/20", "20/15", "20/10", "20/8", "20/7"]  
level = 0  # Start level
current_size = letter_sizes[level]

# Tkinter GUI setup
root = tk.Tk()
root.title("Eye Test")

canvas = tk.Canvas(root, width=800, height=400)
canvas.pack()

text1 = random_letter()
# Display the first letter
letter = canvas.create_text(400, 200, text=text1, font=("Arial", current_size), fill="black")

input_text = tk.Entry(root, width=20)
input_text.pack(pady=10)

failed_attempts = 3

def check():
    global text1, failed_attempts
    user_input = input_text.get().strip().upper()
    if user_input == text1:
        print("Successfull")
        input_text.delete(0, tk.END)
        next_level()
        
    else:
        failed_attempts -= 1
        input_text.delete(0, tk.END)
        if failed_attempts == 0:
            status_label.config(text="Test Failed!")
            display_report()
            

# Next level button
next_button = tk.Button(root, text="Next Level", command=check)
next_button.pack()

# Status label
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()

import tkinter as tk
import random

def generate_similar_colors(base_color, variation=10):
    base_rgb = window.winfo_rgb(base_color)
    base_rgb = [x // 256 for x in base_rgb]
    new_rgb = [
        max(0, min(255, base_rgb[i] + random.randint(-variation, variation)))
        for i in range(3)
    ]
    return f'#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}'

def draw_test(level):
    canvas.delete("all")
    base_color = "#e0e0e0"
    shape_color = generate_similar_colors(base_color, variation=max(5, 20 - level * 3))
    canvas.config(bg=base_color)
    x, y = random.randint(100, 400), random.randint(100, 400)
    canvas.create_rectangle(x, y, x+50, y+50, fill=shape_color, outline=shape_color)
    instruction.config(text="Identify the shape and its position!")

def submit_response():
    global level
    response = user_input.get()
    if response.lower() == "circle":
        result_label.config(text="Correct! Good color sensitivity!", fg="green")
        level += 1
    else:
        result_label.config(text="Try again!", fg="red")
        
def increase_difficulty(level):
    variation = max(5, 20 - level * 3)  # Reduce variation as level increases
    draw_test(variation)


window = tk.Tk()
window.title("Color Sensitivity Test")
window.geometry("500x500")

canvas = tk.Canvas(window, width=500, height=500, bg="white")
canvas.pack()
global level
level = 1
instruction = tk.Label(window, text="Press 'Start Test' to begin!", font=("Arial", 14))
instruction.pack()

button = tk.Button(window, text="Start Test", command=lambda: draw_test(level))
button.pack()

user_input = tk.Entry(window)
user_input.pack()

submit_button = tk.Button(window, text="Submit", command=submit_response)
submit_button.pack()

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

window.mainloop()

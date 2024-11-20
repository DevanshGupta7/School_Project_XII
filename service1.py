import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading
import random
import string
import matplotlib.pyplot as plt
import time

import main_screen
import services

class Service1:
    def __init__(self, root):
        self.root = root
        self.root.title("Eye Testing App")
        
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.rate = self.engine.getProperty("rate")
        self.engine.setProperty("voice", self.voices[0].id)
        self.engine.setProperty("rate", 150)
        
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        
        self.service1_text = '''Snellen
Eye
Chart'''

        self.service2_text = '''Ishihara
test'''

        self.service3_text = '''Color
Blindness
Test'''
        
    def speak(self, audio):
        def run_speak():
            self.engine.say(audio)
            self.engine.runAndWait()
            
        speak = threading.Thread(target=run_speak)
        speak.start()
        
    def service1_screen(self, width, height):        
        self.header = tk.Frame(self.root, width=width, height=150)
        self.header.place(relx=0, rely=0)
        
        header_image = Image.open("Images\\background-gradient-lights.jpg")
        header_width, header_image_height = header_image.size
        print(header_image_height)
        header_image = header_image.resize((width, header_image_height), Image.LANCZOS)
        self.header_photo = ImageTk.PhotoImage(header_image)
        self.header_photo_label = tk.Label(self.header, image=self.header_photo)
        self.header_photo_label.place(relx=0.50, rely=0.50, anchor=tk.CENTER)      
        
        self.main_heading = tk.Label(self.header, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(relx=0.15, rely=0.50, anchor=tk.CENTER)
        
        self.services_button = tk.Button(self.header, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_services())
        #self.services_button.bind("<Button-1>", self.on_press_main)
        #self.services_button.bind("<ButtonRelease-1>", self.on_release_main)
        self.services_button.place(relx=0.37, rely=0.50, anchor=tk.CENTER)
        
        self.about_button = tk.Button(self.header, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        #self.about_button.bind("<Button-1>", self.on_press_main)
        #self.about_button.bind("<ButtonRelease-1>", self.on_release_main)
        self.about_button.place(relx=0.505, rely=0.50, anchor=tk.CENTER)
        
        self.faq_button = tk.Button(self.header, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        #self.faq_button.bind("<Button-1>", self.on_press_main)
        #self.faq_button.bind("<ButtonRelease-1>", self.on_release_main)
        self.faq_button.place(relx=0.63, rely=0.50, anchor=tk.CENTER)
        
        self.home_button = tk.Button(self.header, text="Home", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_main())
        #self.home_button.bind("<Button-1>", self.on_press_main)
        #self.home_button.bind("<ButtonRelease-1>", self.on_release_main)
        self.home_button.place(relx=0.9, rely=0.50, anchor=tk.CENTER)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(x=0, y=header_image_height, width=width, height=height-header_image_height)
        
        self.canvas = tk.Canvas(self.main_frame, highlightthickness=0, bd=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        bg_image = Image.open("Images\\background_footer.jpg")
        bg_image = bg_image.resize((width, height-header_image_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)
        
        #self.service1_frame = tk.Button(self.inner_frame, bg="#22215b", bd=0)
        #self.service1_frame.place(relx=0.50, y=350, anchor=tk.CENTER)
        
        self.letter_sizes = [150, 120, 100, 75, 50, 30, 20, 10, 8, 7]
        self.vision_acuity = ["20/200", "20/100", "20/80", "20/60", "20/40", "20/20", "20/15", "20/10", "20/8", "20/7"]
        self.level = 0
        self.current_size = self.letter_sizes[self.level]
        self.levels_time = []
        
        self.text1 = self.random_letter()
        self.letter = self.canvas.create_text(width/2, height/2-200, text=self.text1, font=("Arial", self.current_size), fill="black")
        
        self.input_text = tk.Entry(self.canvas)
        self.input_text.place(relx=0.465, rely=0.6)
        
        self.failed_attempts = 3
        
        self.next_button = tk.Button(self.canvas, text="Next Level", command=lambda: self.check(width, height))
        self.next_button.pack()
        
        self.status_label = tk.Label(self.canvas, text="")
        self.status_label.pack()
        
        self.start_time = time.time()
        
    def random_letter(self):
        random_letter = random.choice(string.ascii_uppercase)
        return random_letter
    
    def check(self, width, height):
        user_input = self.input_text.get().strip().upper()
        if user_input == self.text1:
            print("Successfull")
            self.input_text.delete(0, tk.END)
            self.next_level(width, height)
            
        else:
            self.failed_attempts -= 1
            self.input_text.delete(0, tk.END)
            if self.failed_attempts == 0:
                self.status_label.config(text="Test Failed!")
                self.display_report(width, height)
                
    def next_level(self, width, height):
        self.end_time = time.time()
        self.each_level_time = self.end_time - self.start_time
        self.levels_time.append(self.each_level_time)
        
        if self.level < len(self.letter_sizes):
            self.failed_attempts = 3
            current_size = self.letter_sizes[self.level]
            self.level += 1
            self.text1 = self.random_letter()
            self.canvas.itemconfig(self.letter, font=("Arial", current_size), text=self.text1)
            self.start_time = time.time()
        else:
            self.status_label.config(text="Test Completed!")
            self.display_report(width, height)
            
    def display_report(self, width, height):
        self.clear_previous_widgets()
        
        if self.level > 0:
            self.report_content = f"""
            Eye Test Report:
            ---------------------
            Best Level Achieved: Level {self.level}
            Smallest Letter Size: {self.letter_sizes[self.level-1]} pixels
            Estimated Visual Acuity: {self.vision_acuity[self.level-1]}
            Avg Time Taken per Level: {round(sum(self.levels_time)/len(self.levels_time), 2)} s
            ---------------------
            Recommendations:
            {"Your vision seems normal." if self.level >= len(self.letter_sizes) - 1 else "Consider consulting an optometrist."}
            """
        else:
            self.report_content = f"""
            Eye Test Report:
            ---------------------
            Best Level Achieved: Level {self.level}
            Smallest Letter Size: --
            Estimated Visual Acuity: --
            ---------------------
            Recommendations:
            {"Highly Consider consulting an optometrist."}
            """
            
        self.report = self.canvas.create_text(width/2, height/2-200, text=self.report_content, font=("Arial", 20), fill="black")
        
        self.plot_progression(self.level)

        # Close Button
        self.close_button = tk.Button(self.canvas, text="Close")
        self.close_button.pack(pady=10)
        
    def plot_progression(self, levels):
        self.sizes = self.letter_sizes[:levels]
        plt.plot(range(1, levels + 1), self.sizes, marker='o')
        plt.gca().invert_yaxis()  # Invert to show smaller letters as better performance
        plt.title("Eye Test Progression")
        plt.xlabel("Level")
        plt.ylabel("Letter Size (Pixels)")
        plt.show()
    
    def clear_previous_widgets(self):
        # Remove the letter text
        if hasattr(self, 'letter') and self.letter:
            self.canvas.delete(self.letter)
            self.letter = None
        
        # Remove the text box (input)
        if hasattr(self, 'input_text') and self.input_text:
            self.input_text.destroy()
            self.input_text = None
        
        # Remove the next button
        if hasattr(self, 'next_button') and self.next_button:
            self.next_button.destroy()
            self.next_button = None
        
        # Remove the status label
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.destroy()
            self.status_label = None
            
    def load_screen_main(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        main_screen.Main(self.root).main_screen_logic(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        
    def load_screen_services(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        services.Services(self.root).services_screen(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
            
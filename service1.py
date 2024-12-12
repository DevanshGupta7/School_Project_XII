import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading
import random
import string
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

    def speak(self, audio):
        def run_speak():
            self.engine.say(audio)
            self.engine.runAndWait()
            
        speak = threading.Thread(target=run_speak)
        speak.start()
        
    def service1_screen(self, width, height):        
        self.header = tk.Frame(self.root, width=width, height=150)
        self.header.place(relx=0, rely=0)
        
        header_image = Image.open("assets\\Images\\background-gradient-lights.jpg")
        header_width, header_image_height = header_image.size
        header_image = header_image.resize((width, header_image_height), Image.LANCZOS)
        self.header_photo = ImageTk.PhotoImage(header_image)
        self.header_photo_label = tk.Label(self.header, image=self.header_photo)
        self.header_photo_label.place(relx=0.50, rely=0.50, anchor=tk.CENTER)      
        
        self.main_heading = tk.Label(self.header, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(relx=0.15, rely=0.50, anchor=tk.CENTER)
        
        self.services_button = tk.Button(self.header, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_services())
        self.services_button.place(relx=0.37, rely=0.50, anchor=tk.CENTER)
        
        self.about_button = tk.Button(self.header, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.about_button.place(relx=0.505, rely=0.50, anchor=tk.CENTER)
        
        self.faq_button = tk.Button(self.header, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.faq_button.place(relx=0.63, rely=0.50, anchor=tk.CENTER)
        
        self.home_button = tk.Button(self.header, text="Home", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_main())
        self.home_button.place(relx=0.9, rely=0.50, anchor=tk.CENTER)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(x=0, y=header_image_height, width=width, height=height-header_image_height)
        
        self.canvas = tk.Canvas(self.main_frame, highlightthickness=0, bd=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        bg_image = Image.open("assets\\Images\\background_footer.jpg")
        bg_image = bg_image.resize((width, height-header_image_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)
        
        self.instruction = self.canvas.create_text(width/2, height/2-200,
                                                   text="Please maintain a distance of 3 meters from the screen to test your eyes.",
                                                   font=("Helvetica", 25), fill="black")
        
        self.root.after(5000, lambda: self.start_eye_test(width, height))
        
    def random_letter(self):
        random_letter = random.choice(string.ascii_uppercase)
        return random_letter
    
    def check(self, width, height):
        self.status_label.config(text="")
        user_input = self.input_text.get().strip().upper()
        if user_input == self.text1:
            self.input_text.delete(0, tk.END)
            self.next_level(width, height)
            
        else:
            self.failed_attempts -= 1
            self.input_text.delete(0, tk.END)
            if self.failed_attempts == 0:
                self.status_label.config(text="Test Failed!")
                self.root.after(2000, lambda: self.display_report(width, height))
            else:
                self.status_label.config(text="Try Again!")
                
    def next_level(self, width, height):
        self.end_time = time.time()
        self.each_level_time = self.end_time - self.start_time
        self.levels_time.append(self.each_level_time)
        self.level += 1
        
        if self.level < len(self.letter_sizes)+1:
            self.failed_attempts = 3
            current_size = self.letter_sizes[self.level-1]
            
            while True:
                self.text1 = self.random_letter()
                if self.text1 not in self.levels_occured:
                    self.levels_occured.append(self.text1)
                    break
                
            self.canvas.itemconfig(self.letter, font=("Arial", current_size), text=self.text1)
            self.start_time = time.time()
        else:
            self.status_label.config(text="Test Completed!")
            self.root.after(2000, lambda: self.display_report(width, height))
            
    def display_report(self, width, height):
        self.clear_previous_widgets()
        if self.level > 1:
            self.report_content = f"""
            Eye Test Report:
            ---------------------
            Best Level Achieved: Level {self.level-1}
            Smallest Letter Size: {self.letter_sizes[self.level-2]} pixels
            Estimated Visual Acuity: {self.vision_acuity[self.level-2]}
            Avg Time Taken per Level: {round(sum(self.levels_time)/len(self.levels_time), 2)} s
            ---------------------
            Recommendations:
            {"Your vision seems normal." if self.level-1 >= len(self.letter_sizes) else "Consider consulting an optometrist."}
            """
        else:
            self.report_content = f"""
            Eye Test Report:
            ---------------------
            Best Level Achieved: Level {self.level-1}
            Smallest Letter Size: --
            Estimated Visual Acuity: --
            ---------------------
            Recommendations:
            {"Highly Consider consulting an optometrist."}
            """
          
        self.report = self.canvas.create_text(width/2, height/2-200, text=self.report_content, font=("Arial", 20), fill="black")

        self.close_button = tk.Button(self.canvas, text="Close", command= lambda: self.load_screen_services())
        self.close_button.place(relx=0.5, rely=0.6)
    
    def clear_previous_widgets(self):
        if hasattr(self, 'letter') and self.letter:
            self.canvas.delete(self.letter)
            self.letter = None
        
        if hasattr(self, 'input_text') and self.input_text:
            self.input_text.destroy()
            self.input_text = None
        
        if hasattr(self, 'next_button') and self.next_button:
            self.next_button.destroy()
            self.next_button = None
        
        if hasattr(self, 'status_label') and self.status_label:
            self.status_label.destroy()
            self.status_label = None
            
    def start_eye_test(self, width, height):
        if hasattr(self, 'instruction') and self.instruction:
            self.canvas.delete(self.instruction)
            self.instruction = None
        
        self.letter_sizes = [150, 120, 100, 75, 50, 30, 20, 10, 8, 7]
        self.vision_acuity = ["20/200", "20/100", "20/80", "20/60", "20/40", "20/20", "20/15", "20/10", "20/8", "20/7"]
        self.level = 1
        self.current_size = self.letter_sizes[self.level-1]
        self.levels_time = []
        self.levels_occured = []
        
        self.text1 = self.random_letter()
        self.levels_occured.append(self.text1)
        self.letter = self.canvas.create_text(width/2, height/2-200, text=self.text1, font=("Arial", self.current_size), fill="black")
        
        self.input_text = tk.Entry(self.canvas)
        self.input_text.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        
        self.failed_attempts = 3
        
        self.next_button = tk.Button(self.canvas, text="Next Level", command=lambda: self.check(width, height))
        self.next_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        
        self.status_label = tk.Label(self.canvas, text="")
        self.status_label.place(relx=0.5, rely=0.70, anchor=tk.CENTER)
        
        self.start_time = time.time()
            
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
  
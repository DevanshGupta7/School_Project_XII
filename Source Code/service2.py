import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading
import random
import time
import sys
import os

import main_screen
import services
import about_screen
import faqs_screen

class Service2:
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
        
    def service2_screen(self, width, height):        
        self.header = tk.Frame(self.root, width=width, height=150)
        self.header.place(relx=0, rely=0)
        
        header_image = Service2.resource_path("assets/Images/background-gradient-lights.jpg")
        header_image = Image.open(header_image)
        header_width, header_image_height = header_image.size
        header_image = header_image.resize((width, header_image_height), Image.LANCZOS)
        self.header_photo = ImageTk.PhotoImage(header_image)
        self.header_photo_label = tk.Label(self.header, image=self.header_photo)
        self.header_photo_label.place(relx=0.50, rely=0.50, anchor=tk.CENTER)      
        
        self.main_heading = tk.Label(self.header, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(relx=0.15, rely=0.50, anchor=tk.CENTER)
        
        self.services_button = tk.Button(self.header, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_services())
        self.services_button.place(relx=0.37, rely=0.50, anchor=tk.CENTER)
        
        self.about_button = tk.Button(self.header, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_about())
        self.about_button.place(relx=0.505, rely=0.50, anchor=tk.CENTER)
        
        self.faq_button = tk.Button(self.header, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_faqs())
        self.faq_button.place(relx=0.63, rely=0.50, anchor=tk.CENTER)
        
        self.home_button = tk.Button(self.header, text="Home", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_main())
        self.home_button.place(relx=0.9, rely=0.50, anchor=tk.CENTER)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(x=0, y=header_image_height, width=width, height=height-header_image_height)
        
        self.canvas = tk.Canvas(self.main_frame, highlightthickness=0, bd=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        bg_image = Service2.resource_path("assets/Images/background_footer.jpg")
        bg_image = Image.open(bg_image)
        bg_image = bg_image.resize((width, height-header_image_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)
        
        self.ishihara_plates_info = [["assets/IshiharaPlates/Circled Number2.png", 2],
                                     ["assets/IshiharaPlates/Circled Number34.png", 34],
                                     ["assets/IshiharaPlates/Circled Number53.png", 53],
                                     ["assets/IshiharaPlates/Circled Number58.png", 58],
                                     ["assets/IshiharaPlates/Circled Number64.png", 64],
                                     ["assets/IshiharaPlates/Circled Number102.png", 102],
                                     ["assets/IshiharaPlates/Circled Number346.png", 346],
                                     ["assets/IshiharaPlates/Circled Number348.png", 348],
                                     ["assets/IshiharaPlates/Circled Number455.png", 455],
                                     ["assets/IshiharaPlates/Circled Number584.png", 584],
                                     ["assets/IshiharaPlates/Circled Number765.png", 765],
                                     ["assets/IshiharaPlates/Circled Number879.png", 879]]
        self.level = 1
        self.levels_time = []
        self.levels_occured = []
        
        self.ishihara_plate_path = self.random_ishihara_plate()
        self.levels_occured.append(self.ishihara_plate_path)
        
        self.ishihara_image = Service2.resource_path(self.ishihara_plate_path)
        self.ishihara_image = Image.open(self.ishihara_image)
        self.ishihara_image = self.ishihara_image.resize((450, 450))
        self.ishihara_photo = ImageTk.PhotoImage(self.ishihara_image)
        self.ishihara_plate = self.canvas.create_image(width/2, height/2-180, image=self.ishihara_photo, anchor=tk.CENTER)
        
        self.input_text = tk.Entry(self.canvas)
        self.input_text.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        
        self.failed_attempts = 3
        
        self.next_button = tk.Button(self.canvas, text="Next Level", command=lambda: self.check(width, height))
        self.next_button.place(relx=0.5, rely=0.80, anchor=tk.CENTER)
        
        self.status_label = tk.Label(self.canvas, text="")
        self.status_label.place(relx=0.5, rely=0.835, anchor=tk.CENTER)
        self.start_time = time.time()
        
    def random_ishihara_plate(self):
        self.random_number = random.randint(0, len(self.ishihara_plates_info)-1)
        self.random_ishihara = self.ishihara_plates_info[self.random_number][0]
        return self.random_ishihara
    
    def check(self, width, height):
        self.status_label.config(text="")
        user_input = self.input_text.get().strip().upper()
            
        if int(user_input) == self.ishihara_plates_info[self.random_number][1]:
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
        
        if self.level < 6:
            self.failed_attempts = 3
            
            while True:
                self.ishihara_plate_path = self.random_ishihara_plate()
                if self.ishihara_plate_path not in self.levels_occured:
                    self.levels_occured.append(self.ishihara_plate_path)
                    break
                
            self.ishihara_plate_path = self.random_ishihara_plate()
            self.ishihara_image = Service2.resource_path(self.ishihara_plate_path)
            self.ishihara_image = Image.open(self.ishihara_image)
            self.ishihara_image = self.ishihara_image.resize((450, 450))
            self.ishihara_photo = ImageTk.PhotoImage(self.ishihara_image)
            self.ishihara_plate = self.canvas.create_image(width/2, height/2-180, image=self.ishihara_photo, anchor=tk.CENTER)
            self.start_time = time.time()
        else:
            self.status_label.config(text="Test Completed!")
            self.root.after(2000, lambda: self.display_report(width, height))
            
    def display_report(self, width, height):
        self.clear_previous_widgets()
        
        if self.level > 1:
            self.report_content = f"""
            Blindness Test Report:
            ---------------------
            Best Level Achieved: Level {self.level-1}
            Avg Time Taken per Level: {round(sum(self.levels_time)/len(self.levels_time), 2)} s
            ---------------------
            Recommendations:
            {"Normal Color Vision." if self.level-1 == 5 else "Mild Color Blindness."}
            """
        else:
            self.report_content = f"""
            Eye Test Report:
            ---------------------
            Best Level Achieved: Level {self.level-1}
            Avg Time Taken per Level: --
            ---------------------
            Recommendations:
            {"Severe Color Blindness"}
            """
            
        self.report = self.canvas.create_text(width/2, height/2-200, text=self.report_content, font=("Arial", 20), fill="black")

        self.close_button = tk.Button(self.canvas, text="Close", command= lambda: self.load_screen_services())
        self.close_button.place(relx=0.5, rely=0.6)
    
    def clear_previous_widgets(self):
        if hasattr(self, 'ishihara_plate') and self.ishihara_plate:
            self.canvas.delete(self.ishihara_plate)
            self.ishihara_plate = None

        if hasattr(self, 'input_text') and self.input_text:
            self.input_text.destroy()
            self.input_text = None

        if hasattr(self, 'next_button') and self.next_button:
            self.next_button.destroy()
            self.next_button = None

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
        
    def load_screen_about(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        about_screen.About(self.root).about_screen_logic(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        
    def load_screen_faqs(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        faqs_screen.Faqs(self.root).faqs_screen_logic(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

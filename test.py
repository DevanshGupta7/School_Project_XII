import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading


class Main_Screen:
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
        
    def main_screen_logic(self, width, height):
        'self.root.configure(bg="#8a2f61")'
        
        bg_image = Image.open("Images\\background.jpg")
        bg_image = bg_image.resize((width, height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.image = Image.open("Images\\speaker_icon1.png")
        self.res_image = self.image.resize((30, 30), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.res_image)
        
        self.main_heading = tk.Label(self.root, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(relx=0.15, rely=0.08, anchor=tk.CENTER)
        
        self.services = tk.Button(self.root, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_services_screen(width, height))
        self.services.bind("<Button-1>", self.on_press_main)
        self.services.bind("<ButtonRelease-1>", self.on_release_main)
        self.services.place(relx=0.37, rely=0.08, anchor=tk.CENTER)
        
        self.about = tk.Button(self.root, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.about.bind("<Button-1>", self.on_press_main)
        self.about.bind("<ButtonRelease-1>", self.on_release_main)
        self.about.place(relx=0.50, rely=0.08, anchor=tk.CENTER)
        
        self.faq = tk.Button(self.root, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.faq.bind("<Button-1>", self.on_press_main)
        self.faq.bind("<ButtonRelease-1>", self.on_release_main)
        self.faq.place(relx=0.63, rely=0.08, anchor=tk.CENTER)
        
        self.tips = tk.Label(self.root, text="Healthy Vision Tips", font=("Helvetica", 25, "bold", "underline"),bg="#8a2f61", fg="white")
        self.tips.place(relx=0.50, rely=0.25, anchor=tk.CENTER)
        
        self.aboutText = '''1. Drink plenty of water and get enough sleep
2. Eat right to protect your sight
3. Visit Eye Doctor Regularly
4. Avoid rubbing eyes
5. Eye massages'''

        self.about_text = tk.Label(self.root, text=self.aboutText, font=("Helventica", 20),bg="#8a2f61", fg="white")
        self.about_text.place(relx=0.50, rely=0.40, anchor=tk.CENTER)
        
        self.speak_button = tk.Button(self.root, image=self.photo, command=lambda: self.speak(f"Healthy Vision Tips... {self.aboutText}"))
        self.speak_button.place(relx=0.50, rely=0.55, anchor=tk.CENTER)

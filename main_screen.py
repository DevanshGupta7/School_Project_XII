import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading

import about_screen
import faqs_screen
import services

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Eye Testing App")
        self.root.attributes('-fullscreen', True)
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.rate = self.engine.getProperty("rate")
        self.engine.setProperty("voice", self.voices[0].id)
        self.engine.setProperty("rate", 150)
        
        self.main_screen_logic(width, height)
        
    def speak(self, audio):
        def run_speak():
            self.engine.say(audio)
            self.engine.runAndWait()
            
        speak = threading.Thread(target=run_speak)
        speak.start()
        
    def on_press_main(self, event):
        self.services.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.about.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.faq.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        
    def on_release_main(self, event):
        self.services.config(activebackground="#8a2f61", activeforeground="black")
        self.about.config(activebackground="#8a2f61", activeforeground="black")
        self.faq.config(activebackground="#8a2f61", activeforeground="black")
        
    def main_screen_logic(self, width, height):        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(x=0, y=0, width=width, height=height)
        
        self.canvas = tk.Canvas(self.main_frame, highlightthickness=0, bd=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        bg_image = Image.open("assets\\Images\\background.jpg")
        bg_image = bg_image.resize((width, height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_image_id = self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)
        
        self.image = Image.open("assets\\Images\\speaker_icon1.png")
        self.res_image = self.image.resize((30, 30), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.res_image)
        
        self.main_heading = tk.Label(self.main_frame, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(x=220, y=70, anchor=tk.CENTER)
        
        self.services = tk.Button(self.canvas, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_services())
        self.services.bind("<Button-1>", self.on_press_main)
        self.services.bind("<ButtonRelease-1>", self.on_release_main)
        self.services.place(relx=0.37, rely=0.08, anchor=tk.CENTER)
        
        self.about = tk.Button(self.canvas, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_about())
        self.about.bind("<Button-1>", self.on_press_main)
        self.about.bind("<ButtonRelease-1>", self.on_release_main)
        self.about.place(relx=0.50, rely=0.08, anchor=tk.CENTER)
        
        self.faq = tk.Button(self.canvas, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_faqs())
        self.faq.bind("<Button-1>", self.on_press_main)
        self.faq.bind("<ButtonRelease-1>", self.on_release_main)
        self.faq.place(relx=0.63, rely=0.08, anchor=tk.CENTER)
        
        self.tips = self.canvas.create_text(width/2, height/2-210, text="Healthy Vision Tips", font=("Helvetica", 25, "bold", "underline"), fill="white")
        
        self.tipsText = '''1. Drink plenty of water and get enough sleep
2. Eat right to protect your sight
3. Visit Eye Doctor Regularly
4. Avoid rubbing eyes
5. Eye massages'''
        
        self.tips_text = self.canvas.create_text(width/2, height/2-95, text=self.tipsText, font=("Helvetica", 20), fill="white")
        
        self.speak_button = tk.Button(self.canvas, image=self.photo, command=lambda: self.speak(f"Healthy Vision Tips... {self.tipsText}"))
        self.speak_button.place(relx=0.50, rely=0.55, anchor=tk.CENTER)
        
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

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()

import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk

import main_screen
import faqs_screen
import services

class About:
    def __init__(self, root):
        self.root = root
        self.root.title("Eye Testing App")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root.attributes('-fullscreen', True)
        
        self.about_text = """Welcome to the Eye Testing App, a Python-based application developed using Tkinter for an interactive and educational experience. This app is designed to simulate basic eye tests, making it a useful tool for preliminary eye health assessment.
    
Features:
- Snellen Chart Test: Assess your visual acuity by reading letters of varying sizes.
- Ishihara Plate Test: Identify color blindness through a series of color plates.

Purpose:
This app was created as a Class 12 Computer Science project. It aims to:
1. Demonstrate how technology can be used for basic eye health awareness.
2. Showcase programming skills using Python and the Tkinter library.
3. Provide users with an easy and interactive way to learn about eye testing.

Credits:
- Developer: Devansh Gupta
- Developer: Tejas Rohilla
Special thanks to teachers for their guidance and support.

Disclaimer:
This app is for educational and informational purposes only. It does not replace professional medical advice, diagnosis, or treatment. For any concerns about your vision, please consult a certified eye care professional."""
        
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.rate = self.engine.getProperty("rate")
        self.engine.setProperty("voice", self.voices[0].id)
        self.engine.setProperty("rate", 150)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
    def on_press(self, event):
        self.services_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.about_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.faq_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.home_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")

    def on_release(self, event):
        self.services_button.config(activebackground="#8a2f61", activeforeground="black")
        self.about_button.config(activebackground="#8a2f61", activeforeground="black")
        self.faq_button.config(activebackground="#8a2f61", activeforeground="black")
        self.home_button.config(activebackground="#8a2f61", activeforeground="black")

    def about_screen_logic(self, width, height):        
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
        self.services_button.bind("<Button-1>", self.on_press)
        self.services_button.bind("<ButtonRelease-1>", self.on_release)
        self.services_button.place(relx=0.37, rely=0.50, anchor=tk.CENTER)
        
        self.about_button = tk.Button(self.header, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.about_button.bind("<Button-1>", self.on_press)
        self.about_button.bind("<ButtonRelease-1>", self.on_release)
        self.about_button.place(relx=0.505, rely=0.50, anchor=tk.CENTER)
        
        self.faq_button = tk.Button(self.header, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_faqs())
        self.faq_button.bind("<Button-1>", self.on_press)
        self.faq_button.bind("<ButtonRelease-1>", self.on_release)
        self.faq_button.place(relx=0.63, rely=0.50, anchor=tk.CENTER)
        
        self.home_button = tk.Button(self.header, text="Home", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_main())
        self.home_button.bind("<Button-1>", self.on_press)
        self.home_button.bind("<ButtonRelease-1>", self.on_release)
        self.home_button.place(relx=0.9, rely=0.50, anchor=tk.CENTER)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(x=0, y=header_image_height, width=width, height=height-header_image_height)
        
        bg_image = Image.open("assets\\Images\\background_footer.jpg")
        bg_image = bg_image.resize((width, height-header_image_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_photo_label = tk.Label(self.main_frame, image=self.bg_photo, bd=0, highlightthickness=0)
        self.bg_photo_label.pack()
        
        tk.Label(self.main_frame, text="About This App", font=("Arial", 25, "bold"), bg="#8a2f61").place(x=width/2, y=60, anchor=tk.CENTER)

        self.text_widget = tk.Text(self.main_frame, wrap=tk.WORD, font=("Arial", 15), bg="#8a2f61")
        self.text_widget.insert(tk.END, self.about_text)
        self.text_widget.config(state="disabled")
        self.text_widget.place(x=width/2, y=height/2-50, anchor=tk.CENTER)

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
            
    def load_screen_faqs(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        faqs_screen.Faqs(self.root).faqs_screen_logic(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        
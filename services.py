import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk

import main_screen
import service1
import service2
import about_screen
import faqs_screen

class Services:
    def __init__(self, root):
        self.root = root
        self.root.title("Eye Testing App")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root.attributes('-fullscreen', True)
        
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.rate = self.engine.getProperty("rate")
        self.engine.setProperty("voice", self.voices[0].id)
        self.engine.setProperty("rate", 150)
        
        self.service1_text = '''Snellen
Eye
Chart'''

        self.service2_text = '''Ishihara
test'''

        self.service3_text = '''Color
Blindness
Test'''
        
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
    def on_press(self, event):
        self.services_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.about_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.faq_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.home_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.service1_frame.config(activebackground="#22215b", activeforeground="white")
        self.service2_frame.config(activebackground="#22215b", activeforeground="white")
        self.service1_Button.config(activebackground="#22215b", activeforeground="white")
        self.service2_Button.config(activebackground="#22215b", activeforeground="white")

    def on_release(self, event):
        self.services_button.config(activebackground="#8a2f61", activeforeground="black")
        self.about_button.config(activebackground="#8a2f61", activeforeground="black")
        self.faq_button.config(activebackground="#8a2f61", activeforeground="black")
        self.home_button.config(activebackground="#8a2f61", activeforeground="black")
        self.service1_frame.config(activebackground="#22215b", activeforeground="white")
        self.service2_frame.config(activebackground="#22215b", activeforeground="white")
        self.service1_Button.config(activebackground="#22215b", activeforeground="white")
        self.service2_Button.config(activebackground="#22215b", activeforeground="white")
        
    def services_screen(self, width, height):        
        self.header = tk.Frame(self.root, width=width, height=150)
        self.header.place(relx=0, rely=0)
        
        header_image = Image.open("Images\\background-gradient-lights.jpg")
        header_width, header_image_height = header_image.size
        header_image = header_image.resize((width, header_image_height), Image.LANCZOS)
        self.header_photo = ImageTk.PhotoImage(header_image)
        self.header_photo_label = tk.Label(self.header, image=self.header_photo)
        self.header_photo_label.place(relx=0.50, rely=0.50, anchor=tk.CENTER)        
        
        self.main_heading = tk.Label(self.header, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(relx=0.15, rely=0.50, anchor=tk.CENTER)
        
        self.services_button = tk.Button(self.header, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.services_button.bind("<Button-1>", self.on_press)
        self.services_button.bind("<ButtonRelease-1>", self.on_release)
        self.services_button.place(relx=0.37, rely=0.50, anchor=tk.CENTER)
        
        self.about_button = tk.Button(self.header, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0, command=lambda: self.load_screen_about())
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
        
        self.canvas = tk.Canvas(self.main_frame, highlightthickness=0, bd=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.inner_frame = tk.Frame(self.canvas)
        
        bg_image = Image.open("Images\\background_footer.jpg")
        bg_image = bg_image.resize((width, height-header_image_height+700), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_photo_label = tk.Label(self.inner_frame, image=self.bg_photo, bd=0, highlightthickness=0)
        self.bg_photo_label.pack()
        
        self.service1_frame = tk.Button(self.inner_frame, width=200, height=28, bg="#22215b", bd=0, command=lambda: self.load_screen_service1())
        self.service1_frame.bind("<Button-1>", self.on_press)
        self.service1_frame.bind("<ButtonRelease-1>", self.on_release)
        self.service1_frame.place(relx=0.50, y=350, anchor=tk.CENTER)
        
        self.service1_Button = tk.Button(self.inner_frame, text=self.service1_text, font=("Helvetica", 50, "italic"), bg="#22215b", fg="white", bd=0, command=lambda: self.load_screen_service1())
        self.service1_Button.bind("<Button-1>", self.on_press)
        self.service1_Button.bind("<ButtonRelease-1>", self.on_release)
        self.service1_Button.place(relx=0.25, y=350, anchor=tk.CENTER)
        
        snellen_chart = Image.open("Images\\snellen_chart.jpg")
        snellen_chart = snellen_chart.resize((200, 350), Image.LANCZOS)
        self.snellen_chart = ImageTk.PhotoImage(snellen_chart)
        
        self.service1_image = tk.Button(self.inner_frame, image=self.snellen_chart, bd=0, command=lambda: self.load_screen_service1())
        self.service1_image.place(relx=0.75, y=350, anchor=tk.CENTER)
        
        self.service2_frame = tk.Button(self.inner_frame, width=200, height=28, bg="#22215b", bd=0, command=lambda: self.load_screen_service2())
        self.service2_frame.bind("<Button-1>", self.on_press)
        self.service2_frame.bind("<ButtonRelease-1>", self.on_release)
        self.service2_frame.place(relx=0.50, y=1000, anchor=tk.CENTER)
        
        self.service2_Button = tk.Button(self.inner_frame, text=self.service2_text, font=("Helvetica", 50, "italic"), bg="#22215b", fg="white", bd=0, command=lambda: self.load_screen_service2())
        self.service2_Button.bind("<Button-1>", self.on_press)
        self.service2_Button.bind("<ButtonRelease-1>", self.on_release)
        self.service2_Button.place(relx=0.25, y=1000, anchor=tk.CENTER)
        
        ishira_image = Image.open("Images\\ishihara_image.png")
        ishira_image = ishira_image.resize((320, 320), Image.LANCZOS)
        self.ishira_image = ImageTk.PhotoImage(ishira_image)
        
        self.service2_image = tk.Button(self.inner_frame, image=self.ishira_image, bd=0, command=lambda: self.load_screen_service2())
        self.service2_image.place(relx=0.75, y=1000, anchor=tk.CENTER)
        
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def load_screen_main(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        main_screen.Main(self.root).main_screen_logic(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        
    def load_screen_service1(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        service1.Service1(self.root).service1_screen(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        
    def load_screen_service2(self):
        for widget in self.root.winfo_children():
            if widget.winfo_exists():
                widget.destroy()
            
        service2.Service2(self.root).service2_screen(self.root.winfo_screenwidth(), self.root.winfo_screenheight())
        
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

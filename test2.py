"""import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading

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
        
        self.services_screen(width, height)
        
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
    def on_press(self, event):
        self.services_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.about_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.faq_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.service1_Button.config(activebackground="#22215b", activeforeground="white")
        self.service1_frame.config(activebackground="#22215b", activeforeground="white")

    def on_release(self, event):
        self.services_button.config(activebackground="#8a2f61", activeforeground="black")
        self.about_button.config(activebackground="#8a2f61", activeforeground="black")
        self.faq_button.config(activebackground="#8a2f61", activeforeground="black")
        self.service1_Button.config(activebackground="#22215b", activeforeground="white")
        self.service1_frame.config(activebackground="#22215b", activeforeground="white")
        
    def services_screen(self, width, height):        
        bg_image = Image.open("background.jpg")
        bg_image = bg_image.resize((width, height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        snellen_chart = Image.open("snellen_chart.jpg")
        snellen_chart = snellen_chart.resize((200, 350), Image.LANCZOS)
        self.snellen_chart = ImageTk.PhotoImage(snellen_chart)
        
        self.main_heading = tk.Label(self.root, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(relx=0.15, rely=0.08, anchor=tk.CENTER)
        
        self.services_button = tk.Button(self.root, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.services_button.bind("<Button-1>", self.on_press)
        self.services_button.bind("<ButtonRelease-1>", self.on_release)
        self.services_button.place(relx=0.37, rely=0.08, anchor=tk.CENTER)
        
        self.about_button = tk.Button(self.root, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.about_button.bind("<Button-1>", self.on_press)
        self.about_button.bind("<ButtonRelease-1>", self.on_release)
        self.about_button.place(relx=0.50, rely=0.08, anchor=tk.CENTER)
        
        self.faq_button = tk.Button(self.root, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.faq_button.bind("<Button-1>", self.on_press)
        self.faq_button.bind("<ButtonRelease-1>", self.on_release)
        self.faq_button.place(relx=0.63, rely=0.08, anchor=tk.CENTER)
        
        self.services_canvas = tk.Canvas(self.root, width=1400, height=420)
        self.services_canvas.place(relx=0.50, rely=0.50, anchor=tk.CENTER)
        
        self.service1_frame = tk.Button(self.services_canvas, width=200, height=28, bg="#22215b", bd=0)
        self.service1_frame.bind("<Button-1>", self.on_press)
        self.service1_frame.bind("<ButtonRelease-1>", self.on_release)
        self.service1_frame.place(relx=0.50, rely=0.50, anchor=tk.CENTER)
        
        self.service1_Button = tk.Button(self.services_canvas, text=self.service1_text, font=("Helvetica", 50, "italic"), bg="#22215b", fg="white", bd=0)
        self.service1_Button.bind("<Button-1>", self.on_press)
        self.service1_Button.bind("<ButtonRelease-1>", self.on_release)
        self.service1_Button.place(relx=0.25, rely=0.50, anchor=tk.CENTER)
        
        self.service1_image = tk.Button(self.services_canvas, image=self.snellen_chart, bd=0)
        self.service1_image.place(relx=0.75, rely=0.50, anchor=tk.CENTER)
        


if __name__ == "__main__":
    root = tk.Tk()
    app = Services(root)
    root.mainloop()"""
    
    
import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import threading

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
        
        self.services_screen(width, height)
        print(width, height)
        
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()
        
    def on_press(self, event):
        self.services_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.about_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.faq_button.config(activebackground="#FFFFFE", activeforeground="#8a2f61")
        self.service1_Button.config(activebackground="#22215b", activeforeground="white")
        self.service1_frame.config(activebackground="#22215b", activeforeground="white")

    def on_release(self, event):
        self.services_button.config(activebackground="#8a2f61", activeforeground="black")
        self.about_button.config(activebackground="#8a2f61", activeforeground="black")
        self.faq_button.config(activebackground="#8a2f61", activeforeground="black")
        self.service1_Button.config(activebackground="#22215b", activeforeground="white")
        self.service1_frame.config(activebackground="#22215b", activeforeground="white")
        
    def services_screen(self, width, height):
        '''self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)
        
        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.second_frame = tk.Frame(self.canvas)'''
        
        self.header = tk.Frame(self.root, width=width, height=150)
        self.header.place(relx=0, rely=0)
        
        header_image = Image.open("background-gradient-lights (10).jpg")
        original_width, original_height = header_image.size
        print(original_height)
        header_image = header_image.resize((width, original_height), Image.LANCZOS)
        self.header_photo = ImageTk.PhotoImage(header_image)
        self.header_photo_label = tk.Label(self.header, image=self.header_photo)
        self.header_photo_label.place(relx=0.50, rely=0.50, anchor=tk.CENTER)
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(x=0, y=original_height, width=width, height=height-original_height)
        
        self.canvas = tk.Canvas(self.main_frame, highlightthickness=0, bd=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.inner_frame = tk.Frame(self.canvas)
        
        bg_image = Image.open("background_footer.jpg")
        bg_image = bg_image.resize((width, height-original_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_photo_label = tk.Label(self.inner_frame, image=self.bg_photo, bd=0, highlightthickness=0)
        self.bg_photo_label.pack()
        
        snellen_chart = Image.open("snellen_chart.jpg")
        snellen_chart = snellen_chart.resize((200, 350), Image.LANCZOS)
        self.snellen_chart = ImageTk.PhotoImage(snellen_chart)
        
        self.main_heading = tk.Label(self.header, text="Eye Testing", font=("Helvetica", 35, "italic"),bg="#8a2f61", fg="#FFFF00")
        self.main_heading.place(relx=0.15, rely=0.50, anchor=tk.CENTER)
        
        self.services_button = tk.Button(self.header, text="Services", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.services_button.bind("<Button-1>", self.on_press)
        self.services_button.bind("<ButtonRelease-1>", self.on_release)
        self.services_button.place(relx=0.37, rely=0.50, anchor=tk.CENTER)
        
        self.about_button = tk.Button(self.header, text="About Us", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.about_button.bind("<Button-1>", self.on_press)
        self.about_button.bind("<ButtonRelease-1>", self.on_release)
        self.about_button.place(relx=0.505, rely=0.50, anchor=tk.CENTER)
        
        self.faq_button = tk.Button(self.header, text="FAQs", font=("Helvetica", 20, "bold", "italic"), bg="#8a2f61", fg="#FFFFFE", bd=0)
        self.faq_button.bind("<Button-1>", self.on_press)
        self.faq_button.bind("<ButtonRelease-1>", self.on_release)
        self.faq_button.place(relx=0.63, rely=0.50, anchor=tk.CENTER)
        
        """self.services_canvas = tk.Canvas(self.second_frame, width=1400, height=420)
        self.services_canvas.place(relx=0.50, rely=0.50, anchor=tk.CENTER)"""
        
        """self.service1_frame = tk.Button(self.services_canvas, width=200, height=28, bg="#22215b", bd=0)
        self.service1_frame.bind("<Button-1>", self.on_press)
        self.service1_frame.bind("<ButtonRelease-1>", self.on_release)
        self.service1_frame.place(relx=0.50, rely=0.50, anchor=tk.CENTER)"""
        
        self.service1_Button = tk.Button(self.services_canvas, text=self.service1_text, font=("Helvetica", 50, "italic"), bg="#22215b", fg="white", bd=0)
        self.service1_Button.bind("<Button-1>", self.on_press)
        self.service1_Button.bind("<ButtonRelease-1>", self.on_release)
        self.service1_Button.place(relx=0.25, rely=0.50, anchor=tk.CENTER)
        
        """self.service1_image = tk.Button(self.services_canvas, image=self.snellen_chart, bd=0)
        self.service1_image.place(relx=0.75, rely=0.50, anchor=tk.CENTER)"""
        
        '''self.canvas.create_window((0, 0), window=self.second_frame, anchor="nw")
        self.second_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))'''
        
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        


if __name__ == "__main__":
    root = tk.Tk()
    app = Services(root)
    root.mainloop()
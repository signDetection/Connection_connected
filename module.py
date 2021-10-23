from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageTk
from GUI.Menubar.Help.Feedback import feedback
from GUI.Menubar.Help.About_Developers import about_dv
from GUI.Menubar.Help.How_To_Use import how_to_use


class Project:

    def __init__(self, window):
        self.window = window

        # windowSize,title,icon & background of the window

        window.geometry("1500x730")
        window.title("Conversation Connected")
        self.logo = PhotoImage(file='GUI/image/LogoOfProject.png')
        window.iconphoto(True, self.logo)
        window.config(background="AliceBlue")
        window.state('zoomed')

        # Top menu of the window

        self.menubar = Menu(window)
        window.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Print Result")
        self.file_menu.add_command(label="History")
        self.settings_submenu = Menu(self.file_menu, tearoff=0)
        self.settings_submenu.add_command(label="change colour",
                                          command=lambda: main_frame.config(bg=colorchooser.askcolor()[1]))
        self.file_menu.add_cascade(label="settings", menu=self.settings_submenu)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)

        self.edit_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Tools", menu=self.edit_menu)
        self.edit_menu.add_command(label="Sign Language Detection")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Facial Expression Recognizer")
        self.edit_menu.add_command(label="Face Mask Detection")

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="How to use", command=how_to_use)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="check for update")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="About Developer", command=about_dv)
        self.help_menu.add_command(label="Contact Support...", command=self.mail_author)
        self.help_menu.add_command(label="Submit Feedback...", command=feedback)

        # content

        # canvas

        global main_frame
        main_frame = Frame(window, bg="AliceBlue")
        main_frame.pack(fill=BOTH, expand=1)

        global second_frame
        second_frame = Frame(main_frame, bg="AliceBlue")
        second_frame.pack(side=TOP, fill=BOTH)
        global main_canvas
        main_canvas = Canvas(second_frame, bg="AliceBlue")
        main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        global bg_image
        bg_image = PhotoImage(file="GUI/image/LogoOfProject.png")
        main_canvas.create_image(100, 100, anchor=NW, image=bg_image)

        # Frame for Buttons

        self.button_frame = Frame(second_frame, bg="AliceBlue")
        self.button_frame.pack(side=RIGHT, anchor=N)

        Button(self.button_frame,
               text=" WallPaper ",
               font=("Times New Roman", 25, "italic"),
               bg="AliceBlue",
               command=self.wallpaper,
               borderwidth=5,
               state=ACTIVE,
               ).pack(side=BOTTOM, padx=20, pady=40)
        Button(self.button_frame,
               text=" Face Expression Recognizer ",
               font=("Times New Roman", 25, "italic"),
               bg="AliceBlue",
               command=None,
               borderwidth=5,
               state=ACTIVE,
               ).pack(side=BOTTOM, padx=20, pady=40)
        Button(self.button_frame,
               text=" Face Mask Detection ",
               font=("Times New Roman", 25, "italic"),
               bg="AliceBlue",
               command=None,
               borderwidth=5,
               state=ACTIVE,
               ).pack(side=BOTTOM, padx=20, pady=40)
        Button(self.button_frame,
               text=" Sign Language Detection ",
               font=("Times New Roman", 25, "italic"),
               bg="AliceBlue",
               command=None,
               borderwidth=5,
               state=ACTIVE,
               ).pack(side=BOTTOM, padx=20, pady=40)

        global output_var
        output_var = StringVar()
        output_var.set("Look at Here for Conversation")
        global output_area
        output_area = Message(main_frame, textvariable=output_var,
                              relief=SUNKEN,
                              anchor="nw",
                              fg="#0d0d0d",
                              bg="white",
                              width=1500,
                              font=("Times New Roman", 35, "bold"),
                              aspect=200)
        output_area.pack(side=BOTTOM, fill=X, expand=1, padx=10, pady=(10, 40))

    def open_file(self):
        self.file_path = filedialog.askopenfilename(
            title="Open IMG file",
            filetypes=(("PNG", "*.png"),
                       ("All IMG Files", '*.jpeg,*.jpg,*.jpe,*.png'),
                       ("JPEG", "*.jpeg,*.jpe,*.jpg")))
        self.opened_image = Image.open(self.file_path)
        self.resized_image = self.opened_image.resize((600, 600), Image.ANTIALIAS)

        main_canvas.delete("all")
        self.open_image = ImageTk.PhotoImage(self.resized_image)
        main_canvas.create_image(0, 0, anchor=NW, image=self.open_image)
        output_var.set("you opened an Image")

    def mail_author(self):
        import webbrowser
        self.mail = webbrowser.open('mailto:jugalrpatel1704@gmail.com', new=1)

    def wallpaper(self):
        main_canvas.delete("all")
        global bg_image
        bg_image = PhotoImage(file="GUI/image/LogoOfProject.png")
        main_canvas.create_image(100, 100, anchor=NW, image=bg_image)
        output_var.set("You are viewing wallpaper")


def starting_project():
    global main_window
    main_window = Tk()
    Project(main_window)
    main_window.mainloop()


starting_project()

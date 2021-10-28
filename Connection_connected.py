from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

from PIL import Image, ImageTk
from cv2 import *
from time import *
from pygame import mixer

from GUI.Menubar.Help.About_Developers import about_dv
from GUI.Menubar.Help.Feedback import feedback
from GUI.Menubar.Help.How_To_Use import how_to_use
from GUI.Menubar.Help.Keymap_reference import keymap_reference
from GUI.Menubar.Camera.Camera import MyVideoCapture

camera_running = False
paused = False
play = False
mixer.init()


class Project:

    def __init__(self, window):

        # WindowSize,title,icon & background of the window

        window.geometry("1500x730")
        window.title("Conversation Connected")
        self.logo = PhotoImage(file='GUI/image/LogoOfProject.png')
        window.iconphoto(True, self.logo)
        window.config(background="AliceBlue")
        window.state('zoomed')

        #  Menubar of the window

        self.menubar = Menu(window)
        window.config(menu=self.menubar)

        self.file_menu = Menu(self.menubar, tearoff=0, fg="DarkSlateGray", bg="WhiteSmoke")
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Print Result")
        self.file_menu.add_command(label="History")
        self.settings_submenu = Menu(self.file_menu, tearoff=0, fg="DarkSlateGray", bg="WhiteSmoke")
        self.settings_submenu.add_command(label="change colour", command=self.color_change)
        self.file_menu.add_cascade(label="settings", menu=self.settings_submenu)

        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)

        self.edit_menu = Menu(self.menubar, tearoff=0, fg="DarkSlateGray", bg="WhiteSmoke")
        self.menubar.add_cascade(label="Tools", menu=self.edit_menu)
        self.edit_menu.add_command(label="Sign Language Detection")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Facial Expression Recognizer")
        self.edit_menu.add_command(label="Face Mask Detection")

        self.help_menu = Menu(self.menubar, tearoff=0, fg="DarkSlateGray", bg="WhiteSmoke")
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="User Manual", command=how_to_use)
        self.help_menu.add_command(label="Keymap Reference ", command=keymap_reference)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="check for update")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="About Developer", command=about_dv)
        self.help_menu.add_command(label="Contact Support...", command=self.mail_author)
        self.help_menu.add_command(label="Submit Feedback...", command=feedback)

        # Main Content

        # Dummy frame and canvas for adding scrollbar to window

        self.scrollbar_frame = Frame(window)
        self.scrollbar_frame.pack(fill=BOTH, expand=1)

        self.scrollbar_canvas = Canvas(self.scrollbar_frame, bg="AliceBlue", highlightthickness=0)

        self.ver_scrollbar = Scrollbar(self.scrollbar_frame, orient=VERTICAL, command=self.scrollbar_canvas.yview)
        self.ver_scrollbar.pack(side=RIGHT, fill=Y)

        self.hor_scrollbar = Scrollbar(self.scrollbar_frame, orient=HORIZONTAL, command=self.scrollbar_canvas.xview)
        self.hor_scrollbar.pack(side=BOTTOM, fill=X)
        self.scrollbar_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.scrollbar_canvas.configure(yscrollcommand=self.ver_scrollbar.set)
        self.scrollbar_canvas.configure(xscrollcommand=self.hor_scrollbar.set)
        self.scrollbar_canvas.bind("<Configure>",
                                   lambda e: self.scrollbar_canvas.configure(
                                       scrollregion=self.scrollbar_canvas.bbox("all")))

        # Mouse and Keyboard Binding to window and scrollbar_canvas

        window.bind_all("<MouseWheel>",
                        lambda e: self.scrollbar_canvas.yview_scroll(int(-1 * (e.delta / 120)),
                                                                     "units"))
        window.bind_all("<Shift-MouseWheel>",
                        lambda e: self.scrollbar_canvas.xview_scroll(int(-1 * (e.delta / 120)),
                                                                     "units"))
        window.bind("<Left>", lambda event: self.scrollbar_canvas.xview_scroll(-1, "units"))
        window.bind("<Right>", lambda event: self.scrollbar_canvas.xview_scroll(1, "units"))
        window.bind("<Up>", lambda event: self.scrollbar_canvas.yview_scroll(-1, "units"))
        window.bind("<Down>", lambda event: self.scrollbar_canvas.yview_scroll(1, "units"))

        window.bind("w", self.wallpaper)
        window.bind("c", self.camera)
        window.bind("s", self.capture)
        window.bind("l", self.sign_language_detection)
        window.bind("m", self.face_mask_detection)
        window.bind("e", self.facial_expression_recognizer)
        window.bind("<space>", self.play_music)
        window.bind("<Control-o>", self.open_file)
        window.bind("<Control-k>", keymap_reference)
        window.bind("<Control-c>", self.color_change)
        window.bind("<Control-u>", how_to_use)

        # Main frame

        self.main_frame = Frame(self.scrollbar_canvas, bg="AliceBlue")
        self.scrollbar_canvas.create_window((0, 0), window=self.main_frame, anchor=NW)

        # Second frame for putting main canvas and button frame in it

        self.second_frame = Frame(self.main_frame, bg="AliceBlue")
        self.second_frame.pack(side=TOP, fill=BOTH)
        global main_canvas
        main_canvas = Canvas(self.second_frame, bg="white", width=1400, height=900, highlightthickness=0)
        main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.bg_image = PhotoImage(file="GUI/image/LogoOfProject.png")
        main_canvas.create_image(100, 100, anchor=NW, image=self.bg_image)

        # Frame for Buttons

        self.button_frame = Frame(self.second_frame, bg="AliceBlue")
        self.button_frame.pack(side=RIGHT, anchor=N)

        # Wallpaper and audio buttons and it's frame

        self.audio_frame = Frame(self.button_frame, bg="AliceBlue")
        self.audio_frame.pack(side=BOTTOM)

        Button(self.audio_frame,
               text=" WallPaper ",
               font=("Times New Roman", 25, "italic"),
               fg="DarkSlateGray",
               bg="WhiteSmoke",
               command=self.wallpaper,
               borderwidth=5,
               state=ACTIVE).pack(side=LEFT, padx=20, pady=40)

        self.sound_on_image = PhotoImage(file="GUI/sound/play.png")
        self.sound_button = Button(self.audio_frame,
                                   image=self.sound_on_image,
                                   font=("Times New Roman", 25, "italic"),
                                   fg="DarkSlateGray",
                                   bg="WhiteSmoke",
                                   command=self.play_music,
                                   borderwidth=5,
                                   state=ACTIVE)
        self.sound_button.pack(side=RIGHT, padx=20, pady=40)

        # Camera and capture button and it's frame

        self.camera_frame = Frame(self.button_frame, bg="AliceBlue")
        self.camera_frame.pack(side=BOTTOM)
        Button(self.camera_frame,
               text=" Camera ",
               font=("Times New Roman", 25, "italic"),
               fg="DarkSlateGray",
               bg="WhiteSmoke",
               command=self.camera,
               borderwidth=5,
               state=ACTIVE).pack(side=LEFT, padx=20, pady=40)

        Button(self.camera_frame,
               text=" Capture ",
               font=("Times New Roman", 25, "italic"),
               fg="DarkSlateGray",
               bg="WhiteSmoke",
               command=self.capture,
               borderwidth=5,
               state=ACTIVE).pack(side=RIGHT, padx=20, pady=40)

        # Main feature functions

        Button(self.button_frame,
               text=" Facial Expression Recognizer ",
               font=("Times New Roman", 25, "italic"),
               fg="DarkSlateGray",
               bg="WhiteSmoke",
               command=self.facial_expression_recognizer,
               borderwidth=5,
               state=ACTIVE).pack(side=BOTTOM, padx=20, pady=40)

        Button(self.button_frame,
               text=" Face Mask Detection ",
               font=("Times New Roman", 25, "italic"),
               fg="DarkSlateGray",
               bg="WhiteSmoke",
               command=self.face_mask_detection,
               borderwidth=5,
               state=ACTIVE).pack(side=BOTTOM, padx=20, pady=40)

        Button(self.button_frame,
               text=" Sign Language Detection ",
               font=("Times New Roman", 25, "italic"),
               fg="DarkSlateGray",
               bg="WhiteSmoke",
               command=self.sign_language_detection,
               borderwidth=5,
               state=ACTIVE).pack(side=BOTTOM, padx=20, pady=40)

        # Output box at bottom of the window

        global output_var
        output_var = StringVar()
        output_var.set("Look at Here for Conversation")

        global output_area
        output_area = Message(self.main_frame, textvariable=output_var,
                              relief=SUNKEN,
                              anchor="nw",
                              fg="DarkSlateGray",
                              bg="WhiteSmoke",
                              width=1500,
                              font=("Times New Roman", 35, "bold"),
                              aspect=200)
        output_area.pack(side=BOTTOM, fill=X, padx=10, pady=(10, 40))

    # All needed functions are mention here section by section

    # Menubar and other functions

    def color_change(self, *args):
        self.bg_color = colorchooser.askcolor()[1]
        self.button_frame.config(bg=self.bg_color)
        self.main_frame.config(bg=self.bg_color)
        self.scrollbar_canvas.config(bg=self.bg_color)
        self.camera_frame.config(bg=self.bg_color)
        self.audio_frame.config(bg=self.bg_color)
        self.second_frame.config(bg=self.bg_color)

    def open_file(self, *args):
        self.file_path = filedialog.askopenfilename(
            title="Open IMG file",
            filetypes=(("All Image Files", "*.png;*.bmp;*.dib;*.jpg;*.jpeg;*.jpe;*.jfif;*.gif;*.ico;*.webp"),
                       ("PNG", "*.png"),
                       ("Bitmap Files", "*.bmp;*.dib"),
                       ("JPEG", "*.jpg;*.jpeg;*.jpe;*.jfif"),
                       ("ICO", "*.ico"),
                       ("WEBP", "*.webp"),
                       ("All Files", "*.*")))

        if self.file_path:
            self.opened_image = Image.open(self.file_path)
            self.resized_image = self.opened_image.resize((1100, 900), Image.ANTIALIAS)

            global camera_running
            camera_running = False

            main_canvas.delete("all")
            self.open_image = ImageTk.PhotoImage(self.resized_image)
            main_canvas.create_image(150, 0, anchor=NW, image=self.open_image)
            output_var.set("you opened an Image.")

    def mail_author(self):
        import webbrowser
        self.mail = webbrowser.open('mailto:jugalrpatel1704@gmail.com', new=1)

    # Button functions

    # Entertainment functions

    def play_music(self, *args):
        global play
        if play is False:
            global paused
            if paused is False:
                mixer.music.load("GUI/sound/background_music.mp3")
                mixer.music.play(loops=1)
                mixer.music.set_volume(0.2)
                play = True
                self.sound_off_image = PhotoImage(file="GUI/sound/mute.png")
                self.sound_button.config(image=self.sound_off_image)

            else:
                mixer.music.unpause()
                play = True
                self.sound_button.config(image=self.sound_off_image)

        else:
            mixer.music.pause()
            self.sound_button.config(image=self.sound_on_image)
            paused = True
            play = False

    def wallpaper(self, *args):
        global camera_running
        camera_running = False
        main_canvas.delete("all")
        self.wallpaper_image = PhotoImage(file="GUI/image/LogoOfProject.png")
        main_canvas.create_image(100, 100, anchor=NW, image=self.wallpaper_image)
        output_var.set("You are viewing wallpaper of software.")

    def camera(self, *args):
        global camera_running
        if camera_running is True:
            pass
        else:
            main_canvas.delete("all")
            global running_video
            running_video = MyVideoCapture(0)
            output_var.set("You are using camera")
            camera_running = True
            self.video_loop()

    def video_loop(self):
        global camera_running
        if camera_running is True:
            ret, frame = running_video.get_frame()

            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                main_canvas.create_image(380, 210, image=self.photo, anchor=NW)

            self.main_frame.after(20, self.video_loop)
        else:
            running_video.__del__()

    def capture(self, *args):
        global camera_running
        if camera_running is True:
            output_var.set("you captured your Photo")
            output_area.update()
            ret, frame = running_video.get_frame()

            if ret:
                cv2.imwrite("ImageGallery/Photo" + strftime("%d-%m-%Y_%H-%M-%S") + ".jpg",
                            cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            sleep(0.25)
            output_var.set("you are using camera")
        else:
            output_var.set("Please turn on Camera before using this button.")

    # Main functions

    def face_mask_detection(self, *args):
        output_var.set("You are on Face Mask Detection. ")

    def sign_language_detection(self, *args):
        output_var.set("You are on Sign Language Detection. ")

    def facial_expression_recognizer(self, *args):
        output_var.set("You are on Facial Expression Recognizer")


def starting_project():
    global project_window
    project_window = Tk()
    Project(project_window)
    project_window.mainloop()


starting_project()

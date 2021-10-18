from tkinter import *
from tkinter import filedialog
from Menubar.Help.Feedback import feedback
from Menubar.Help.About_Developers import about_dv
from Menubar.Help.How_To_Use import how_to_use


def open_file():
    filepath = filedialog.askopenfilename(
        initialdir="C:\\Users\\Public\\Downloads",
        title="Open IMG file",
        filetypes=(("PNG", "*.png"),
                   ("All IMG Files", '*.jpeg,*.jpg,*.jpe,*.png'),
                   ("JPEG", "*.jpeg,*.jpe,*.jpg")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()


def mail_author():
    import webbrowser
    webbrowser.open('mailto:jugalrpatel1704@gmail.com', new=1)


def wallpaper():
    main_canvas.itemconfig(item_in_canvas, image=bg_img)
    print("this is work")


window = Tk()  # instantiate an instance of a window

# windowSize,title,icon & background of the window
window.geometry("1500x700")
window.title("Conversation Connected")
logo = PhotoImage(file='image/LogoOfProject.png')
window.iconphoto(True, logo)
window.config(background="AliceBlue")
# window.state('zoomed')

# Top menu of the window

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Print Result")
fileMenu.add_command(label="History")
fileMenu.add_command(label="Settings...")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=editMenu)
editMenu.add_command(label="Sign Language Detection")
editMenu.add_separator()
editMenu.add_command(label="Facial Expression Recognizer")
editMenu.add_command(label="Face Mask Detection")

helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="How to use", command=how_to_use)
helpMenu.add_separator()
helpMenu.add_command(label="check for update")
helpMenu.add_separator()
helpMenu.add_command(label="About Developer", command=about_dv)
helpMenu.add_command(label="Contact Support...", command=mail_author)
helpMenu.add_command(label="Submit Feedback...", command=feedback)

# content
# canvas
main_frame = Frame(window, bg="AliceBlue")
main_frame.pack(fill=BOTH, expand=1)

main_canvas = Canvas(main_frame, bg="AliceBlue")
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

bg_img = PhotoImage(file="image/LogoOfProject.png")
item_in_canvas = main_canvas.create_image(100, 100, anchor=NW, image=bg_img)

# Frame for Buttons

button_frame = Frame(main_frame, bg="AliceBlue")
button_frame.pack(side=RIGHT, anchor=N)

Button(button_frame,
       text=" WallPaper ",
       font=("Times New Roman", 30, "italic"),
       bg="AliceBlue",
       command=wallpaper,
       borderwidth=5,
       state=ACTIVE,
       ).pack(side=BOTTOM, padx=20, pady=40)
Button(button_frame,
       text=" Face Expression Recognizer ",
       font=("Times New Roman", 30, "italic"),
       bg="AliceBlue",
       command=None,
       borderwidth=5,
       state=ACTIVE,
       ).pack(side=BOTTOM, padx=20, pady=40)
Button(button_frame,
       text=" Face Mask Detection ",
       font=("Times New Roman", 30, "italic"),
       bg="AliceBlue",
       command=None,
       borderwidth=5,
       state=ACTIVE,
       ).pack(side=BOTTOM, padx=20, pady=40)
Button(button_frame,
       text=" Sign Language Detection ",
       font=("Times New Roman", 30, "italic"),
       bg="AliceBlue",
       command=None,
       borderwidth=5,
       state=ACTIVE,
       ).pack(side=BOTTOM, padx=20, pady=40)

window.mainloop()  # place window on computer screen. listen for events

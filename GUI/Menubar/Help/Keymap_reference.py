from tkinter import *

keymap_reference_option_window = None


class Keymap_reference:

    def __init__(self, keymap_reference_window):
        keymap_reference_window.title('Keymap for working with Conversion Connected')
        keymap_reference_window.resizable(False, False)
        keymap_reference_window.configure(background="AliceBlue")

        self.main_frame = Frame(keymap_reference_window, bg="AliceBlue")  # header frame
        self.main_frame.pack()

        # main header
        Label(self.main_frame,
              text="Conversation Connected !!!",
              font=('Times New Roman', 20, 'bold'),
              fg="DarkSlateGray",
              bg="AliceBlue",
              justify="center").pack(pady=(15, 20))

        self.main_canvas = Canvas(self.main_frame, bg="white", highlightthickness=0)
        self.main_canvas.pack(side=LEFT, fill=BOTH, padx=40)

        # sub header 1
        Label(self.main_canvas,
              text='KeyBoard and Mouse Bindings :',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 15, 'bold')).grid(row=1, column=0, padx=5, pady=(15, 10))

        Label(self.main_canvas,
              text='Scroll wheel ---> Vertical Scrolling into window ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=2, column=0, padx=(25, 0), sticky=W)
        Label(self.main_canvas,
              text='Shift + Scroll wheel ---> Horizontal Scrolling into window ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=3, column=0, padx=(25, 0), sticky=W)
        Label(self.main_canvas,
              text='Arrow Keys ---> Scrolling into window ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=4, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='L ---> Sign Language Detection  ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=7, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='H ---> Hand Gesture Recognizer ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=8, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='M ---> Face Mask Detection ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=9, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='C ---> Camera ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=10, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='S ---> SnapShot(capture) ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=11, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='W ---> Wallpaper ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=12, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='Control + O ---> Open file ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=13, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='Control + U ---> user manual ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=14, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='Control + K ---> keyboard references ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=15, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='Control + C ---> Theme color change ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=16, column=0, padx=(25, 0), sticky=W)

        Label(self.main_canvas,
              text='SpaceBar ---> play/pause music ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=17, column=0, padx=(25, 0), sticky=W)


        # Close button
        Button(keymap_reference_window,
               text='Close',
               fg="DarkSlateGray",
               font=("Times New Roman", 15, "italic"),
               bg="WhiteSmoke",
               borderwidth=3,
               command=keymap_reference_window.destroy).pack(side=RIGHT, padx=15, pady=15)


def keymap_reference(*args):
    global keymap_reference_option_window
    keymap_reference_option_window = Tk()
    keymap_reference_option_window.geometry("470x520")
    Keymap_reference(keymap_reference_option_window)
    keymap_reference_option_window.mainloop()


if __name__ == "__main__":
    keymap_reference()

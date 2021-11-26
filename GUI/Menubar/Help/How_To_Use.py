from tkinter import *

how_to_use_option_window = None


class How_to_use:

    def __init__(self, how_to_use_window):
        how_to_use_window.title('User guide for working with Conversion Connected')
        how_to_use_window.resizable(False, False)
        how_to_use_window.configure(background="AliceBlue")

        self.main_frame = Frame(how_to_use_window, bg="AliceBlue")  # header frame
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
              text='Sign Language Detection :',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 15, 'bold')).grid(row=5, column=0, padx=5, pady=(15, 10))

        Label(self.main_canvas,
              text='Click on the  Sign Language Detection button. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=6, column=0, padx=5)

        Label(self.main_canvas,
              text='Now Do some American Hand Language Action in front of camera. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=7, column=0, padx=5)

        Label(self.main_canvas,
              text='The letter or word displayed at the bottom of the screen. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=8, column=0, padx=5)
        # sub header 2
        Label(self.main_canvas,
              text='Hand Gesture Recognizer :',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 15, 'bold')).grid(row=15, column=0, padx=5,
                                                         pady=(35, 10))
        Label(self.main_canvas,
              text='Click on the Hand Gesture Recognizer button. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=16, column=0, padx=5)

        Label(self.main_canvas,
              text='do some action in front of the camera. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=17, column=0, padx=5)

        Label(self.main_canvas,
              text='Your current gesture was displayed on the bottom of the screen. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=18, column=0, padx=5)
        # sub Header 3
        Label(self.main_canvas,
              text='Face Mask Detection :',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 15, 'bold')).grid(row=25, column=0, padx=5, pady=(35, 10))

        Label(self.main_canvas,
              text='Click on the Face Mask Detection button. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=26, column=0, padx=5)

        Label(self.main_canvas,
              text='Now look at the camera. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=27, column=0, padx=5)
        Label(self.main_canvas,
              text='Your status of wearing mask or not is displayed on the bottom of the screen. ',
              fg="DarkSlateGray",
              bg="white",
              font=('Times New Roman', 11)).grid(row=28, column=0, padx=5)
        # Close button
        Button(how_to_use_window,
               text='Close',
               fg="DarkSlateGray",
               font=("Times New Roman", 15, "italic"),
               bg="WhiteSmoke",
               borderwidth=3,
               command=how_to_use_window.destroy).pack(side=RIGHT, padx=15, pady=15)


def how_to_use(*args):
    global how_to_use_option_window
    how_to_use_option_window = Tk()
    how_to_use_option_window.geometry("550x590")
    How_to_use(how_to_use_option_window)
    how_to_use_option_window.mainloop()


if __name__ == "__main__":
    how_to_use()

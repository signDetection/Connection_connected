from tkinter import *

how_to_use_option_window = None


class How_to_use:

    def __init__(self, how_to_use_window):
        how_to_use_window.title('User guide for working with Conversion Connected')
        how_to_use_window.resizable(False, False)
        how_to_use_window.configure(background="AliceBlue")

        self.frame = Frame(how_to_use_window, bg="AliceBlue")  # header frame
        self.frame.pack()

        # main header
        Label(self.frame,
              text="Conversation Connected !!!",
              font=('Times New Roman', 18, 'bold'),
              fg="DarkSlateGray",
              bg="AliceBlue",
              justify="center").grid(row=0, column=0)
        # sub header 1
        Label(self.frame,
              text='Sign Language Detection :',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 15, 'bold')).grid(row=5, column=0, padx=5, pady=(35, 10))

        Label(self.frame,
              text='Go to Tools --> Sign Language Detection. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=6, column=0, padx=5)

        Label(self.frame,
              text='Now Do some American Hand Language Action in front of camera. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=7, column=0, padx=5)

        Label(self.frame,
              text='The letter or word displayed at the bottom of the screen ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=8, column=0, padx=5)
        # sub header 2
        Label(self.frame,
              text='Facial Expression Recognizer :',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 15, 'bold')).grid(row=15, column=0, padx=5,
                                                         pady=(35, 10))
        Label(self.frame,
              text='Go to Tools --> Facial Expression Recognizer. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=16, column=0, padx=5)

        Label(self.frame,
              text='Now look at the camera. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=17, column=0, padx=5)

        Label(self.frame,
              text='Your current mood was displayed on the bottom of the screen. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=18, column=0, padx=5)
        # sub Header 3
        Label(self.frame,
              text='Face Mask Detection :',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 15, 'bold')).grid(row=25, column=0, padx=5, pady=(35, 10))

        Label(self.frame,
              text='Go to Tools --> Face Mask Detection. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=26, column=0, padx=5)

        Label(self.frame,
              text='Now look at the camera. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=27, column=0, padx=5)
        Label(self.frame,
              text='Your status of wearing mask or not is displayed on the bottom of the screen. ',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 11)).grid(row=28, column=0, padx=5)
        # Close button
        Button(how_to_use_window,
               text='Close',
               fg="DarkSlateGray",
               font=("Times New Roman", 15, "italic"),
               bg="WhiteSmoke",
               borderwidth=3,
               command=how_to_use_window.destroy).pack(side=RIGHT, padx=15, pady=15)


def how_to_use():
    global how_to_use_option_window
    how_to_use_option_window = Tk()
    how_to_use_option_window.geometry("480x530")
    How_to_use(how_to_use_option_window)
    how_to_use_option_window.mainloop()


if __name__ == "__main__":
    how_to_use()

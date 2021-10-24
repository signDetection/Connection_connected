from tkinter import *

about_dev_window = None


class About_dv:

    def __init__(self, about_dv_window):
        about_dv_window.title('About Developers of conversation connected')
        about_dv_window.resizable(False, False)
        about_dv_window.configure(background="AliceBlue")

        self.frame = Frame(about_dv_window, bg="AliceBlue")  # header frame
        self.frame.pack()

        Label(self.frame, text="Conversation Connected !!!",
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 20, 'bold'),
              justify="center").grid(row=0, column=0)

        Label(self.frame,
              text='Developers :',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 16, 'bold')).grid(row=5, column=0, padx=5, pady=(35, 10))
        Label(self.frame,
              text='Jugal Patel',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 12)).grid(row=8, column=0, padx=5)
        Label(self.frame,
              text='Jay Parekh',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 12)).grid(row=9, column=0, padx=5)
        Label(self.frame,
              text='Dhruv Chauhan',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 12)).grid(row=10, column=0, padx=5)
        Label(self.frame,
              text='We are from The Maharaja Sayajirao University.',
              fg="DarkSlateGray",
              bg="AliceBlue",
              font=('Times New Roman', 16, 'bold')).grid(row=11, column=0, padx=5, pady=35)

        Button(about_dv_window,
               text='Close',
               fg="DarkSlateGray",
               font=("Times New Roman", 15, "bold"),
               bg="WhiteSmoke",
               borderwidth=3,
               command=about_dv_window.destroy).pack(side=RIGHT, padx=15, pady=(15, 15))


def about_dv():
    global about_dev_window
    about_dev_window = Tk()
    about_dev_window.geometry("450x350")
    About_dv(about_dev_window)
    about_dev_window.mainloop()


if __name__ == "__main__":
    about_dv()

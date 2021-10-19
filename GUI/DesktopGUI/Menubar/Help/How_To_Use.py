from tkinter import *
from tkinter import ttk

how_to_use_option_window = None


class How_to_use:

    def __init__(self, how_to_use_window):
        how_to_use_window.title('User guide for working with Conversion Connected')
        how_to_use_window.resizable(False, False)
        how_to_use_window.configure(background="AliceBlue")

        self.style = ttk.Style()
        self.style.configure('TFrame', background="AliceBlue")
        self.style.configure('TLabel', background="AliceBlue", font=('Times New Roman', 11))
        self.style.configure('h1.TLabel', font=('Times New Roman', 18, 'bold'))
        self.style.configure('h2.TLabel', font=('Times New Roman', 15, 'bold'))

        self.frame = ttk.Frame(how_to_use_window, style='TFrame')  # header frame
        self.frame.pack()

        ttk.Label(self.frame, text="Conversation Connected !!!", style='h1.TLabel', justify="center").grid(
            row=0, column=0)

        ttk.Label(self.frame, text='Sign Language Detection :', style='h2.TLabel').grid(row=5, column=0, padx=5,
                                                                                        pady=(35, 10))
        ttk.Label(self.frame, text='Go to Tools --> Sign Language Detection. ', style='TLabel').grid(row=6, column=0,
                                                                                                     padx=5)
        ttk.Label(self.frame, text='Now Do some American Hand Language Action in front of camera. ',
                  style='TLabel').grid(row=7, column=0, padx=5)
        ttk.Label(self.frame, text='The letter or word displayed at the bottom of the screen ', style='TLabel').grid(
            row=8, column=0, padx=5)
        ttk.Label(self.frame, text='Facial Expression Recognizer :', style='h2.TLabel').grid(row=15, column=0, padx=5,
                                                                                             pady=(35, 10))
        ttk.Label(self.frame, text='Go to Tools --> Facial Expression Recognizer. ', style='TLabel').grid(row=16,
                                                                                                          column=0,
                                                                                                          padx=5)
        ttk.Label(self.frame, text='Now look at the camera. ', style='TLabel').grid(row=17, column=0, padx=5)
        ttk.Label(self.frame, text='Your current mood was displayed on the bottom of the screen. ',
                  style='TLabel').grid(row=18, column=0, padx=5)
        ttk.Label(self.frame, text='Face Mask Detection :', style='h2.TLabel').grid(row=25, column=0, padx=5,
                                                                                    pady=(35, 10))
        ttk.Label(self.frame, text='Go to Tools --> Face Mask Detection. ', style='TLabel').grid(row=26, column=0,
                                                                                                 padx=5)
        ttk.Label(self.frame, text='Now look at the camera. ', style='TLabel').grid(row=27, column=0, padx=5)
        ttk.Label(self.frame, text='Your status of wearing mask or not is displayed on the bottom of the screen. ',
                  style='TLabel').grid(row=28, column=0, padx=5)

        ttk.Button(how_to_use_window, text='Close', command=how_to_use_window.destroy).pack(side=RIGHT, padx=5, pady=5)


def how_to_use():
    global how_to_use_option_window
    how_to_use_option_window = Tk()
    how_to_use_option_window.geometry("480x530")
    How_to_use(how_to_use_option_window)
    how_to_use_option_window.mainloop()


if __name__ == "__main__":
    how_to_use()

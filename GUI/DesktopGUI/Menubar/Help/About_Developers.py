from tkinter import *
from tkinter import ttk

about_dev_window = None


class About_dv:

    def __init__(self, about_dv_window):
        about_dv_window.title('Information about Developers of conversation connected')
        about_dv_window.resizable(False, False)
        about_dv_window.configure(background="AliceBlue")

        self.style = ttk.Style()
        self.style.configure('TFrame', background="AliceBlue")
        self.style.configure('TLabel', background="AliceBlue", font=('Times New Roman', 11))
        self.style.configure('h1.TLabel', font=('Times New Roman', 20, 'bold'))
        self.style.configure('h2.TLabel', font=('Times New Roman', 16, 'bold'))

        self.frame = ttk.Frame(about_dv_window, style='TFrame')  # header frame
        self.frame.pack()

        ttk.Label(self.frame, text="Conversation Connected !!!", style='h1.TLabel', justify="center").grid(
            row=0, column=0)

        ttk.Label(self.frame, text='Developers :', style='h2.TLabel').grid(row=5, column=0, padx=5, pady=35)
        ttk.Label(self.frame, text='Jugal Patel', style='TLabel').grid(row=8, column=0, padx=5)
        ttk.Label(self.frame, text='Jay Parekh', style='TLabel').grid(row=9, column=0, padx=5)
        ttk.Label(self.frame, text='Dhruv Chauhan', style='TLabel').grid(row=10, column=0, padx=5)
        ttk.Label(self.frame, text='We are from The Maharaja Sayajirao University.', style='h2.TLabel').grid(row=11,
                                                                                                             column=0,
                                                                                                             padx=5,
                                                                                                             pady=35)

        ttk.Button(about_dv_window, text='Close', command=about_dv_window.destroy).pack(side=RIGHT, padx=5, pady=5)


def about_dv():
    global about_dev_window
    about_dev_window = Tk()
    about_dev_window.geometry("500x350")
    About_dv(about_dev_window)
    about_dev_window.mainloop()


if __name__ == "__main__":
    about_dv()
